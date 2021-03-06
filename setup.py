from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Advanced Math'
LONG_DESCRIPTION = 'A package that allows to operate various mathematical operations that are not in-built in python.'

# Setting up
setup(
    name="adv_math",
    version=VERSION,
    author="MrigKrafts",
    author_email="<mrigkrafts@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'math'],
    classifiers=[
        "Development Status :: 1 - Under Development",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
