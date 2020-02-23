"""
This is the setup file which allows pip to install and uninstall
the module "amod". Strangely, no clean uninstall is possible.

Also, you can import amod without installing it first.
"""

from setuptools import setup

setup(
        name="amod",
        py_modules=["amod"]
)
