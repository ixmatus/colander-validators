import sys
from distutils.core import setup

version = '0.0.3'

with open("LICENSE", 'r') as f:
    LICENSE = f.read()

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
      license=LICENSE,
      packages=["colander_validators"]
      )
