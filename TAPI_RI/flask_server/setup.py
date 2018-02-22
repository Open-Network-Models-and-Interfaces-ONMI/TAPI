# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "tapi_server"
VERSION = "2.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="tapi-connectivity API",
    author_email="",
    url="",
    keywords=["Swagger", "tapi-connectivity API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['tapi_server=tapi_server.__main__:main']},
    long_description="""\
    tapi-connectivity API generated from tapi-connectivity.yang
    """
)

