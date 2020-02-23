"""
This is the setup file which allows pip to install and uninstall
the package "apkg". This cannot be imported before installation.
"""

from setuptools import setup, find_packages

setup(
        name="apkg",
        description="Just a demo for packaging and distribution",

        version="1.0",
        author="Brian Okken",
        author_email="brian@pythontesting.net",
        url="https://pragprog.com/book/bopytest/python-testing-with-pytest",

        packages=find_packages(where="src"),
        package_dir={'': "src"},
)
