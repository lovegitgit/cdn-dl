#!/usr/bin/env python3

from setuptools import setup, find_packages
import os


this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='cdn-dl',
    version='0.3',
    description='通过cdn 下载文件',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="nobitaqaq",
    author_email="xiaoleigs@gmail.com",
    keywords=["cdn-dl", "cdn 文件下载器"],
    packages=find_packages(include=['cdndl']),
    entry_points={
        'console_scripts': [
            'cdn-dl = cdndl.main:main',
        ]
    },
    python_requires=">=3.8",
    install_requires=[
        'tqdm',
        'urllib3'
    ],
)
