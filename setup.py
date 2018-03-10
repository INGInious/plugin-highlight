#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import inginious_highlight

setup(
    name="inginious_highlight",
    version=inginious_highlight.__version__,
    description="Plugin to highlight lines in code problems",
    packages=find_packages(),
    install_requires=["inginious>=0.5.dev0"],
    tests_require=[],
    extras_require={},
    scripts=[],
    include_package_data=True,
    author="The INGInious authors",
    author_email="inginious@info.ucl.ac.be",
    license="AGPL 3",
    url="https://github.com/UCL-INGI/INGInious-highlight-plugin"
)