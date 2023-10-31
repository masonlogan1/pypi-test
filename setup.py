from setuptools import setup, find_packages
import codecs
import os
import sys

print(sys.argv)

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as reader:
    long_description = '\n'.join(reader.readlines())

VERSION = '0.0.0'
DESCRIPTION = 'test package for testing github workflow'
LONG_DESCRIPTION = long_description

# Setting up
# noinspection SpellCheckingInspection
setup(
    version=os.environ.get('BUILD_VERSION') or VERSION,
    name="malogan-pypi-test",
    author="malogan (Mason Logan)",
    author_email="<dev@masonlogan.com>",
    url='https://github.com/masonlogan1/pypi-test',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    data_files=[],
    include_package_data=True,
    keywords=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
