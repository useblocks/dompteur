# -*- coding: utf-8 -*-
import os
from io import open
from setuptools import setup, find_packages

directory = os.path.dirname(os.path.abspath(__file__))


README_PATH = os.path.join(directory, 'README.rst')


setup(
    name='domnteur',
    version='0.0.1',
    url='https://github.com/useblocks/domteur',
    license='MIT',
    author='team useblocks',
    author_email='info@useblocks.com',
    description='A configuration tool for Sphinx projects',
    long_description=open(README_PATH, encoding='utf-8').read(),
    zip_safe=False,
    packages=['sphinx_simplepdf',
              'sphinx_simplepdf.builders',
              'sphinx_simplepdf.directives',
              'sphinx_simplepdf.themes/simplepdf_theme',
              ],
    package_data={'sphinx_simplepdf/themes/simplepdf_theme': [
        'theme.conf',
        '*.html',
        'static/styles/*.css',
        'static/js/*.js',
        'static/fonts/*.*'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points={
        'sphinx.html_themes': [
            'simplepdf_theme = sphinx_simplepdf.themes.simplepdf_theme',
        ],
        'sphinx.builders': [
            'simplepdf = sphinx_simplepdf.builders.simplepdf'
        ]
    },
    install_requires=[
        'sphinx',
        'weasyprint',       # the used PDF builder
        'libsass',           # needed to generate css on the fly
        'beautifulsoup4',    # needed for HTML manipulations
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
