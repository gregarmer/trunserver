#!/usr/bin/env python

from setuptools import setup, find_packages
from os.path import join, dirname


setup(
      name='trunserver',

      version='0.0.3',
      license = 'MIT License',
      platforms='Linux',
      
      description=('Twisted based Django runserver replacement'),
      long_description=open(join(dirname(__file__), 'README.rst')).read(),
      
      author='Gregory Armer',
      url='https://github.com/gregarmer/trunserver/',
      
      packages=find_packages(),
      install_requires=['twisted',],
      
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing'
        ],
      
     )
