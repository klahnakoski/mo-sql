# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from setuptools import setup
setup(
    author='Kyle Lahnakoski',
    author_email='kyle@lahnakoski.com',
    classifiers=["Development Status :: 4 - Beta","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)","Topic :: Database","Topic :: Utilities","Programming Language :: SQL","Programming Language :: Python :: 3.8","Programming Language :: Python :: 3.9","Programming Language :: Python :: 3.10","Programming Language :: Python :: 3.11","Programming Language :: Python :: 3.12"],
    description='More SQL!  For safely assembling SQL',
    extras_require={"tests":["mo-testing>=7.562.24075"]},
    include_package_data=True,
    install_requires=["mo-dots==9.578.24081","mo-future==7.546.24057","mo-json==6.579.24081","mo-logs==8.579.24081"],
    license='MPL 2.0',
    long_description='# More SQL!\n\nA number of generator functions for type-safe SQL composition.\n\n\n[![PyPI Latest Release](https://img.shields.io/pypi/v/jx-sqlite.svg)](https://pypi.org/project/mo-sql/)\n[![Build Status](https://app.travis-ci.com/klahnakoski/mo-sql.svg?branch=master)](https://travis-ci.com/github/klahnakoski/mo-sql)\n\n## Summary',
    long_description_content_type='text/markdown',
    name='mo-sql',
    packages=["mo_sql"],
    url='https://github.com/klahnakoski/mo-sql',
    version='4.579.24081'
)