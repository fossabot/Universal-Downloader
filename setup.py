#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='MR-eBook-Downloader',
    version='1.3.0.dev',
    description='MR ebook downloader.',
    author='Iceflower S',
    author_email='iceflower@gmx.de',
    license='GPLv3',
    url='https://github.com/IceflowRE/MR-eBook-Downloader',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GPL License',
    ],
    packages=find_packages(),
    install_requires=[
        'urllib3',
        'certifi',
    ],
    extras_require={
        'dev': [
            'nose2',
        ]
    },
    package_data={
        'License': ['../LICENSE'],
        'ReadMe': ['../README.md'],
    }
)
