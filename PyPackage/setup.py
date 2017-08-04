# -------------------------------------------------------------------
# - NAME:        setup.py
# - AUTHOR:      Reto Stauffer
# - DATE:        2017-02-05
# -------------------------------------------------------------------
# - DESCRIPTION: Installer for the GFSV2 python package.
# -------------------------------------------------------------------
# - EDITORIAL:   2017-02-05, RS: Created file on thinkreto.
# -------------------------------------------------------------------
# - L@ST MODIFIED: 2017-08-04 16:49 on thinkreto
# -------------------------------------------------------------------
from setuptools import setup

setup(name='GFSV2',     # This is the package name
      version='0.1-1',            # Current package version, what else
      description='GFS reforecast version 2 downloader',
      long_description='No long description necessary',
      classifiers=[
        'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        'Closed source',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='GFS reforecast',
      url='https://git.uibk.ac.at/retos/GFSreforecastV2/',
      author='Reto Stauffer',
      author_email='reto.stauffer@uibk.ac.at',
      license='GPL-2',
      packages=['GFSV2'],
      install_requires=[
         'ConfigParser',
         'logging'
      ],
      #scripts=['bin/profiler_parsefile',
      #         'bin/sodar_parsefile'],
      include_package_data=True,
      czip_safe=False)

