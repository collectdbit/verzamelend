#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pip.req import parse_requirements

from setuptools import find_packages, setup

exec(open('verzamelend/version.py').read())
setup(name='verzamelend',
      version=__version__,
      description='Python verzamelend package.',
      author='Pedro Salgado',
      author_email='steenzout@ymail.com',
      maintainer='Pedro Salgado',
      maintainer_email='steenzout@ymail.com',
      url='https://github.com/steenzout/verzamelend',
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
      install_requires=[str(pkg.req) for pkg in parse_requirements('requirements.txt')],
      tests_require=[str(pkg.req) for pkg in parse_requirements('test-requirements.txt')],)
