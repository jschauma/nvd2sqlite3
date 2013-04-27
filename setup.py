#!/usr/bin/env python

version = (0, 0, 1)
__version__ = '.'.join([str(b) for b in version])
__author__ = 'Jan Schaumann'
__email__ = 'jschauma@netmeister.org'

from distutils.core import setup

setup(
  name='nvd2sqlite3',
  version=__version__,
  description='NIST Vulnerability Database to Sqlite syncing tool',
  author=__author__,
  author_email=__email__,
  url='https://git.twitter.biz/nvd2sqlite3',
  scripts = ['src/nvd2sqlite3'],
  data_files = [ ('man/man1', [ 'doc/nvd2sqlite3.1.gz' ])]
  )
