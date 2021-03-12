#!/usr/bin/env python

from setuptools import setup, find_packages
import os.path

setup(name='tap-purecloud',
      version='0.0.6',
      description='Singer.io tap for extracting data from the Genesys Purecloud API',
      author='Fishtown Analytics',
      url='http://fishtownanalytics.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_purecloud'],
      install_requires=[
          'singer-python==5.12.0',
          'backoff==1.10.0',
          'requests==2.25.1',
          'python-dateutil==2.8.1',
          'PureCloudPlatformClientV2==111.0.0',
          'websockets==8.1'
      ],
      entry_points='''
          [console_scripts]
          tap-purecloud=tap_purecloud:main
      ''',
      packages=['tap_purecloud']
)
