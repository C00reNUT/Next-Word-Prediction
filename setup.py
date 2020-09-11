#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

# The text of the README file
with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name="next_word_prediction",
    version="0.1.0",
    description="Experiment on the Generative Pretrained Transformer 2 (GPT-2) for Language Modeling task using the PyTorch-Transformers library.",
    long_description=README,
    url="https://github.com/rdgozum/Next-Word-Prediction",
    author="Ryan Paul Gozum",
    author_email="ryanpaul.gozum@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
   ],
   keywords=["language model"],
   packages=["next_word_prediction"],
   include_package_data=True,
   install_requires=["numpy", "pytorch-transformers", "torch"],
)
