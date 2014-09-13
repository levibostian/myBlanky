#!/usr/bin/env python

from setuptools import setup

from myBlanky import _version

setup(name="myBlanky",
      version=_version.__version__,
      description="Creates blank project structures for various projects. Get building faster!",
      long_description=open("README.md").read(),
      author="Levi Bostian",
      author_email="levi.bostian@gmail.com",
      url="https://github.com/levibostian/myBlanky",
      license="MIT",
      packages=["myBlanky"],
      keywords = "blanky myblanky productivity structure",
      entry_points={"console_scripts": ["myblanky = myBlanky.myblanky:main"]},
      install_requires=['docopt==0.6.1'])
