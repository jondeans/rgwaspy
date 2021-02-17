from setuptools import find_packages, setup

import rgwaspy

PACKAGENAME = "rgwaspy"
VERSION = rgwaspy.__version__

INSTALL_REQUIRES = [
    "numpy" "pandas",
    "pip",
    "python>=3.8",
    "setuptools",
]

setup(
    name=PACKAGENAME,
    version=VERSION,
    description="Python implementation of RGWAS.",
    url="http://github.com/jondeans/rgwaspy",
    author="Jon Deans",
    packages=find_packages(),
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
)
