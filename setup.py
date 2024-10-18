# coding: utf-8

"""
    Product Partner API

    Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.

    The version of the OpenAPI document: v1
    Contact: chris@productpartner.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "pp_sdk"
VERSION = "0.2.23"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Product Partner API",
    author="OpenAPI Generator community",
    author_email="chris@productpartner.ai",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Product Partner API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT License",
    long_description_content_type='text/markdown',
    long_description="""\
    Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.
    """,  # noqa: E501
    package_data={"pp_sdk": ["py.typed"]},
)
