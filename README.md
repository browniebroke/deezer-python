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

Contributors
------------

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table><tr><td align="center"><a href="https://www.twitter.com/_BrunoAlla"><img src="https://avatars1.githubusercontent.com/u/861044?v=4" width="100px;" alt="Bruno Alla"/><br /><sub><b>Bruno Alla</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=browniebroke" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=browniebroke" title="Documentation">📖</a> <a href="#ideas-browniebroke" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-browniebroke" title="Maintenance">🚧</a> <a href="#platform-browniebroke" title="Packaging/porting to new platform">📦</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=browniebroke" title="Tests">⚠️</a></td><td align="center"><a href="https://github.com/misuzu"><img src="https://avatars1.githubusercontent.com/u/248143?v=4" width="100px;" alt="misuzu"/><br /><sub><b>misuzu</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=misuzu" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=misuzu" title="Documentation">📖</a> <a href="#ideas-misuzu" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=misuzu" title="Tests">⚠️</a></td><td align="center"><a href="https://github.com/pfouque"><img src="https://avatars1.githubusercontent.com/u/8300001?v=4" width="100px;" alt="Pascal"/><br /><sub><b>Pascal</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=pfouque" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=pfouque" title="Tests">⚠️</a></td><td align="center"><a href="https://github.com/khamaileon"><img src="https://avatars2.githubusercontent.com/u/1322166?v=4" width="100px;" alt="khamaileon"/><br /><sub><b>khamaileon</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=khamaileon" title="Documentation">📖</a></td><td align="center"><a href="https://github.com/sheregeda"><img src="https://avatars3.githubusercontent.com/u/2856444?v=4" width="100px;" alt="Nikolay Sheregeda"/><br /><sub><b>Nikolay Sheregeda</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=sheregeda" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=sheregeda" title="Tests">⚠️</a></td><td align="center"><a href="https://github.com/horstmannmat"><img src="https://avatars1.githubusercontent.com/u/11761333?v=4" width="100px;" alt="Matheus Horstmann"/><br /><sub><b>Matheus Horstmann</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=horstmannmat" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=horstmannmat" title="Documentation">📖</a></td><td align="center"><a href="https://github.com/MDCEY"><img src="https://avatars2.githubusercontent.com/u/3812864?v=4" width="100px;" alt="Kieran Wynne"/><br /><sub><b>Kieran Wynne</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=MDCEY" title="Code">💻</a></td></tr><tr><td align="center"><a href="https://github.com/jnth"><img src="https://avatars0.githubusercontent.com/u/7796167?v=4" width="100px;" alt="Jonathan Virga"/><br /><sub><b>Jonathan Virga</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=jnth" title="Code">💻</a></td><td align="center"><a href="https://github.com/hugovk"><img src="https://avatars2.githubusercontent.com/u/1324225?v=4" width="100px;" alt="Hugo"/><br /><sub><b>Hugo</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=hugovk" title="Code">💻</a></td></tr></table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://allcontributors.org) specification.
Contributions of any kind are welcome!
