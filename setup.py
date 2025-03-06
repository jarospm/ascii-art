#!/usr/bin/env python3
"""
Setup script for ASCII Art Studio.
"""

from setuptools import setup, find_packages
import os

# Read the long description from README.md
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ascii-art-studio",
    version="0.1.0",
    description="Convert images to ASCII art",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ASCII Art Studio Team",
    packages=find_packages(),
    install_requires=[
        "Pillow",
    ],
    entry_points={
        "console_scripts": [
            "ascii-art-studio=ascii_art_studio.__main__:main",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Multimedia :: Graphics",
    ],
) 