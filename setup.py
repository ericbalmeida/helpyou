#!/usr/bin/env python
from setuptools import setup, find_packages

requires = [
        'django'
        ]

setup(name='helpyou',
      version='1.0',
      packages=find_packages(),
      install_requires=requires,
      scripts=['./projeto_eduardo/manage.py'])


