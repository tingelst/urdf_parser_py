#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='urdf_parser_py',
      packages=['urdf_parser_py', 'urdf_parser_py.xml_reflection'],
      package_dir={'': 'src'},
      install_requires=[
          'pyyaml',
          'lxml'
      ],
      )
