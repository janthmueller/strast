# Copyright (c) 2023 Jan T. Müller <mail@jantmueller.com>

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="strast",
    version="0.1.0",
    packages=find_packages(),
    author="Jan T. Müller",
    author_email="mail@jantmueller.com",
    description="Transforms a string representation of a Python literal into the corresponding Python object.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/janthmueller/strast",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=[
        "string",
        "ast",
        "python",
        "literal",
        "transformation",
        "literal transformation",
        "literal conversion",
        "string transformation",
        "string to literal",
        "string to dict",
        "string to set",
        "string to list",
        "string to tuple",
        "string to int",
        "string to float",
        "string to bool",
        "string to None",
        "string to",
        "string to anything",
        "eval",
    ],
    python_requires=">=3.6",
)
