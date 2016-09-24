"""
Command line utility for DalmatinerDB
"""

import os
import re
from setuptools import find_packages, setup


def fread(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    VERSIONFILE = "gr/_version.py"
    verstrline = fread(VERSIONFILE).strip()
    vsre = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(vsre, verstrline, re.M)
    if mo:
        VERSION = mo.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s." %
                           (VERSIONFILE, ))
    return VERSION


dependencies = ['click', 'requests', 'pyyaml']

setup(
    name='golden-retriever',
    version=get_version(),
    url='https://github.com/dataloop/golden-retriever',
    download_url="https://github.com/dataloop/golden-retriever/tarball/v" + get_version(),
    license="Apache License, Version 2.0",
    author='Steven Acreman',
    author_email='steven.acreman@dataloop.io',
    description='Command line utility for Dataloop.IO',
    long_description=fread('README.rst'),
    keywords="dataloop monitoring",
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'gr = gr.gr:main',
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
    ])
