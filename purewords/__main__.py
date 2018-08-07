import argparse
import glob
import os.path
from joblib import Parallel, delayed

import purewords
from purewords.filter_collection import document_filters
from purewords.filter_collection import token_filters


def parse():
    parser = argparse.ArgumentParser(
        description=(
            'Purewords command line interface\n' +
            'Clean text from files.'),
        usage='python -m purewords input_file_path',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-d', '--dir', action='store_true',
                        help="set it up to process all txt files in the directory")
    parser.add_argument('-j', '--job_number', metavar='job_number',
                        default=4, type=int, nargs='?',
                        help="the thread number used in preprocessing")
    parser.add_argument('-max', '--max_len', metavar='max_len',
                        default=200, type=int, nargs='?',
                        help="the maximun length of a sentence")
    parser.add_argument('-min', '--min_len', metavar='min_len',
                        default=1, type=int, nargs='?',
                        help="the minimun length of a sentence")
    parser.add_argument('-bs', '--batch_size', metavar='batch_size',
                        default=8000, type=int, nargs='?',
                        help="the average number of processed sentence per thread")
    parser.add_argument('-v', '--verbose', metavar='verbose',
                        default=1, type=int, nargs='?',
                        help="the verbose level in multiprocessing")
    parser.add_argument('-o', '--output', metavar='output_file_path',
                        default=None, type=str, nargs='?',
                        help="the cleaned output file path")
    parser.add_argument('input_path', type=str, help="data file path")
    return parser.parse_args()


def sentences_generator(file_path, batch_size):
    sentences = []
    with open(file_path, 'rb') as f:
        line_num = 0
        for line in f:
            sentences.append(line.decode('utf-8').strip())
            line_num += 1
            if line_num >= batch_size:
                yield sentences
                sentences = []
                line_num = 0
        if line_num > 0:
            yield sentences
    f.close()


def main():
    args = parse()

    if args.dir:
        textfile_paths = glob.glob(os.path.join(args.input_path, '*.txt'))
    else:
        textfile_paths = [args.input_path]

    if args.output is None:
        output_path = os.path.basename(
            args.input_path) + '_tokenized_corpus.txt'
    else:
        output_path = args.output

    out_file = open(output_path, 'wb')

    for textfile in textfile_paths:
        generate_tokenized_corpus(args, textfile, out_file)

    out_file.close()


def generate_tokenized_corpus(args, input_file_path, out_file):

    batch_size = args.job_number * args.batch_size
    processed_number = 0

    print('processing ' + os.path.basename(input_file_path) + '...')
    info = ""

    for raw_document_list in sentences_generator(input_file_path, batch_size):
        corpus = Parallel(n_jobs=args.job_number, verbose=args.verbose)(
            delayed(purewords.static_clean_document)
            (
                document,
                document_filters,
                token_filters,
                args.min_len,
                args.max_len
            ) for document in raw_document_list
        )

        return_info = ""
        for _ in range(len(info)):
            return_info += '\r'
        print(return_info, end='', flush=True)

        processed_number += len(raw_document_list)
        info = str(processed_number) + ' sentences have been processed'
        print(info, end='')

        #####  write  #####
        for doc in corpus:
            for sentence in doc:
                out_file.write(sentence.encode('utf-8') + b'\n')

    print('\nprocessing ' + os.path.basename(input_file_path) + ' completed')


if __name__ == '__main__':
    main()
