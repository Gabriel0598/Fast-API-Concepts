from setuptools import setup, find_packages

setup(
name='fast_api_packages',
version='1.0',
author='Gabriel Augusto Ferreira',
author_email='REDACTED',
description='Packages for Fast API Project',
long_description=open('README.md').read(),
long_description_content_type='text/markdown',
url='https://github.com/Gabriel0598/Fast-API-Concepts',
packages=find_packages(),
install_requires=[
'pytest>=8.3.5',
'setuptools>=78.1.0'
],
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.11',
)