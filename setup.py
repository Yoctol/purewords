# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="purewords",
    version="0.1.1",
    description="A NLP preprocessing package",
    license="MIT",
    author="EN, PLLiao",
    python_requires='>=3.5',
    packages=find_packages(),
    package_dir={'purewords': 'purewords'},
    package_data={'purewords': ['*.*', 'tokenizer/*', 'configs/*']},
    install_requires=[
        'jieba==0.39',
        'joblib==0.12.2',
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ]
)
