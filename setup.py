# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="purewords",
    version="0.1.0",
    description="A NLP preprocessing package",
    license="MIT",
    author="EN, PLLiao",
    packages=['purewords'],
    package_dir={'purewords':'purewords'},
    package_data={'purewords':['*.*','tokenizer/*', 'configs/*']},
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
    ]
)
