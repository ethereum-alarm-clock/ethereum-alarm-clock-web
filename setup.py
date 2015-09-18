#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


setup(
    name='eth_alarm',
    version='0.1.0',
    author='',
    author_email='pipermerriam@gmail.com',
    url='https://github.com/pipermerriam/ethereum-alarm-clock-web',
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=[
        # TODO
    ],
    zip_safe=False,
    license="MIT",
    scripts=['eth_alarm/manage.py'],
)
