from setuptools import setup, find_packages
import sys, os

version = '0.3.0'

setup(name='gistapi',
      version=version,
      description="This is a python OO gist[hub] API module",
      long_description="""\
           This module was originally written by Kenneth Reitz.  This is a fork by Robb O'Driscoll.
""",
    classifiers=(
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    )

      keywords='',
      author='Kenneth Reitz',
      author_email='me@kennethreitz.com',
      url='http://github.com/kennethreitz/gistapi.py',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests',]),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'simplejson' 
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
