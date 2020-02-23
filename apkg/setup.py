"""
This is the setup file which allows pip to install and uninstall
the package "apkg". This cannot be imported before installation.
"""

from setuptools import setup, find_packages

setup(
        name="apkg",
        packages=find_packages(where="src"),
        package_dir={'': "src"},
)
