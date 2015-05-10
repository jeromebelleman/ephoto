#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='ephoto',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Export from iPhoto",
    long_description="Export faces and organise iPhoto rolls.",
    scripts=['faces', 'rolls'],
    py_modules=['ephoto'],
    data_files=[('share/man/man1', ['ephoto.1'])],
)
