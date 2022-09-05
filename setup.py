#!/usr/bin/env python
import os.path
import re
from distutils.core import setup

# Find version info from module (without importing the module):
self = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(self, "ovmfvartool/__init__.py")) as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

# Use the README.md content for the long description:
readme = os.path.join(self, "README.md")
with open(readme, encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ovmfvartool",
    version=version,
    description="Generate and dump OVMF_VARS.fd files to/from YAML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Hugo Landau",
    author_email="hlandau@devever.net",
    url="https://github.com/hlandau/ovmfvartool",
    packages=["ovmfvartool"],
    license="GPL3",
    entry_points={
        "console_scripts": [
            "ovmfvartool = ovmfvartool:run",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3",
        "Programming Language :: Python :: 3",
    ],
)
