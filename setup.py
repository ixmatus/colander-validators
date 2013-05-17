import sys
from setuptools import setup, find_packages

version = '0.0.2'

setup(name="colander-validators",
      version=version,
      description="Better validators for Colander based on FormEncode's validators",
      classifiers=["Intended Audience :: Developers",
                   "License :: OSI Approved :: Python Software Foundation License",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
      author="Parnell Springmeyer",
      author_email="ixmatus@gmail.com",
      url="http://github.com/ixmatus/colander-validators",
      license="PSF",
      zip_safe=False,
      packages=find_packages(),
      include_package_data=True
      )
