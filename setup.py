import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mech-nimbus",
    version = "0.0.1",
    author = "Ian Itow",
    author_email = "Itow0001@gmail.com",
    description = ("the upper portion of a cumulus cloud characterized by dense, sharply defined, cauliflowerlike upper parts and sometimes by great verticality. "
                                   ""),
    license = "BSD",
    keywords = " testing infrastructure",
    url = "http://packages.python.org/thunderhead",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: testing infrastructure",
        "License :: OSI Approved :: BSD License",
    ],
)
