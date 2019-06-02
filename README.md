Deezer Python Client
====================

[![Build status](https://img.shields.io/travis/browniebroke/deezer-python.svg?style=flat-square&logo=travis)](https://travis-ci.org/browniebroke/deezer-python)
[![Build status](https://img.shields.io/appveyor/ci/browniebroke/deezer-python.svg?logo=appveyor&style=flat-square)](https://ci.appveyor.com/project/browniebroke/deezer-python)
[![Test coverage percentage](https://img.shields.io/codecov/c/github/browniebroke/deezer-python.svg?logo=codecov&style=flat-square)](https://codecov.io/gh/browniebroke/deezer-python)
[![Maintainability](https://api.codeclimate.com/v1/badges/bfbf562a06742972c694/maintainability)](https://codeclimate.com/github/browniebroke/deezer-python/maintainability)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

[![Documentation Status](https://img.shields.io/readthedocs/deezer-python.svg?logo=read-the-docs&style=flat-square)](https://deezer-python.readthedocs.io)
[![PyPi Status](https://img.shields.io/pypi/v/deezer-python.svg?logo=python&logoColor=fff&style=flat-square)](https://pypi.org/project/deezer-python/)
![pyversions](https://img.shields.io/pypi/pyversions/deezer-python.svg?style=flat-square)
![license](https://img.shields.io/pypi/l/deezer-python.svg?style=flat-square)
[![LoC](https://tokei.rs/b1/github/browniebroke/deezer-python/)](https://github.com/browniebroke/deezer-python)

A friendly wrapper around the [Deezer
API](http://developers.deezer.com/api).

Installation
------------

The package is published on
[PyPI](https://pypi.org/project/deezer-python/) and can be installed by
running:

    pip install deezer-python

Basic Use
---------

So far you can only retrieve the data for the public objects, for which
no login is required. The objects are translated to python resources,
which are basically python objects encapsulating the json dictionary
returned by the API.

``` {.python}
>>> client = deezer.Client()
>>> client.get_album(12).title
'Monkey Business'
```

Ready for more? The detailed [API
reference](https://deezer-python.readthedocs.io/api_reference/toc.html)
is available in the
[documentation](http://deezer-python.readthedocs.io/) on RTD.
