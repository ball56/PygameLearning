 -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='PygameLearning',
    version='0.1.0',
    description='something for me to learn pygame',
    long_description=readme,
    author='ball56',
    author_email='ball56@gmail.com',
    url='https://github.com/ball56/PygameLearning',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
