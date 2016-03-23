#!/usr/bin/env python

#
# setup-ified it
#
from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

setup(
    name = 'pyx509',
    version = '0.6.0', # Would really like to link this to a tag/branch/whatever
    install_requires = ['pyasn1>=0.1.4',],
    author = 'Ondrej Mikle',
    author_email = 'ondrej.mikle@gmail.com',
    license = 'GPL',
    description = 'X.509 Certificate Parser for Python',
    url = 'https://github.com/hiviah/pyx509',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
    ],
    packages = find_packages(),
    ext_modules = cythonize([
        Extension("pyx509.pkcs7.asn1_models.general_types", ["pyx509/pkcs7/asn1_models/general_types.pyx"]),
    ]),
    scripts = ['x509_parse.py',],
)
