# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "tapi_server"
VERSION = "2.1.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.0.0",
    "swagger-ui-bundle==0.0.2",
    "python_dateutil==2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="tapi-oam,tapi-photonic-media,tapi-path-computation,tapi-connectivity,tapi-dsr,tapi-notification,tapi-topology,tapi-common,tapi-odu API",
    author_email="",
    url="",
    keywords=["OpenAPI", "tapi-oam,tapi-photonic-media,tapi-path-computation,tapi-connectivity,tapi-dsr,tapi-notification,tapi-topology,tapi-common,tapi-odu API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['tapi_server=tapi_server.__main__:main']},
    long_description="""\
    tapi-oam,tapi-photonic-media,tapi-path-computation,tapi-connectivity,tapi-dsr,tapi-notification,tapi-topology,tapi-common,tapi-odu API generated from yang definitions
    """
)

