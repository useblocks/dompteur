# -*- coding: utf-8 -*-
import os
from io import open
from setuptools import setup, find_packages

directory = os.path.dirname(os.path.abspath(__file__))


README_PATH = os.path.join(directory, 'README.rst')


setup(
    name='dompteur',
    version='0.0.1',
    url='https://github.com/useblocks/dompteur',
    license='MIT',
    author='team useblocks',
    author_email='info@useblocks.com',
    description='A configuration tool for Sphinx projects',
    long_description=open(README_PATH, encoding='utf-8').read(),
    zip_safe=False,
    packages=[],
    package_data={},
    include_package_data=True,
    entry_points={
    },
    install_requires=[],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
