#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip.download


from collectdbit import verzamelend

from pip.req import parse_requirements

from setuptools import find_packages, setup

setup(name=verzamelend.__name__,
      version=verzamelend.__version__,
      description='Python verzamelend package.',
      author='Pedro Salgado',
      author_email='steenzout@ymail.com',
      maintainer='Pedro Salgado',
      maintainer_email='steenzout@ymail.com',
      url='https://github.com/collectdbit/verzamelend',
      namespace_packages=('collectdbit',),
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests', 'collectdbit')),
      install_requires=[
            str(pkg.req) for pkg in parse_requirements(
                    'requirements.txt', session=pip.download.PipSession())],
      tests_require=[
            str(pkg.req) for pkg in parse_requirements(
                    'test-requirements.txt', session=pip.download.PipSession())],)

