# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='replace_line',
    version='0.1.0',
    description='Replace line with specified characters',
    long_description=readme,
    author='kons16',
    author_email='river.field.1126@gmail.com',
    url='https://github.com/kons16/replace_line',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
