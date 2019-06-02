import os

import codecs
from setuptools import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with codecs.open(os.path.join(*paths), "r", "utf-8") as f:
        return f.read()


version = "1.1.2"

setup(
    name="deezer-python",
    version=version,
    description="A friendly wrapper library for the Deezer API",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Bruno Alla",
    author_email="alla.brunoo@gmail.com",
    url="https://github.com/browniebroke/deezer-python",
    download_url="https://github.com/browniebroke/deezer-python/tarball/{}".format(
        version
    ),
    license="MIT",
    packages=["deezer"],
    install_requires=["requests"],
    extras_require={"tornado": ["tornado"]},
    tests_require=["requests-mock"],
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
