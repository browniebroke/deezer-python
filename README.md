Deezer Python Client
====================

<p align="center">
  <a href="https://github.com/browniebroke/deezer-python/actions?query=workflow%3ACI">
    <img alt="CI Status" src="https://img.shields.io/github/workflow/status/browniebroke/deezer-python/CI?label=CI&logo=github&style=flat-square">
  </a>
  <a href="https://deezer-python.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/deezer-python.svg?logo=read-the-docs&amp;style=flat-square" alt="Documentation Status">
  </a>
  <a href="https://codecov.io/gh/browniebroke/deezer-python">
    <img src="https://img.shields.io/codecov/c/github/browniebroke/deezer-python.svg?logo=codecov&amp;style=flat-square" alt="Test coverage percentage">
  </a>
  <a href="https://codeclimate.com/github/browniebroke/deezer-python/maintainability">
    <img src="https://api.codeclimate.com/v1/badges/bfbf562a06742972c694/maintainability" alt="Maintainability"></a>
  <a href="https://github.com/ambv/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?amp;style=flat-square" alt="black">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">
  </a>
</p>
<p align="center">
  <a href="https://mybinder.org/v2/gh/browniebroke/deezer-python/master?filepath=demo.ipynb">
    <img src="https://mybinder.org/badge_logo.svg" alt="Launch demo on Binder">
  </a>
  <a href="https://pypi.org/project/deezer-python/">
    <img src="https://img.shields.io/pypi/v/deezer-python.svg?logo=python&amp;logoColor=fff&amp;style=flat-square" alt="PyPi Status">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/deezer-python.svg?style=flat-square" alt="pyversions">
  <img src="https://img.shields.io/pypi/l/deezer-python.svg?style=flat-square" alt="license">
  <a href="https://github.com/browniebroke/deezer-python">
    <img src="https://tokei.rs/b1/github/browniebroke/deezer-python/" alt="LoC">
  </a>
</p>

A friendly Python wrapper around the [Deezer API](http://developers.deezer.com/api).

Installation
------------

The package is published on
[PyPI](https://pypi.org/project/deezer-python/) and can be installed by running:

    pip install deezer-python

Basic Use
---------

Easily query the Deezer API from you Python code. The data returned by the Deezer
API is mapped to python resources:

```python
>>> client = deezer.Client()
>>> client.get_album(680407).title
'Monkey Business'
```

Ready for more? Look at our whole [documentation](http://deezer-python.readthedocs.io/)
on Read The Docs or have a play in pre-populated Jupyter notebook
[on Binder](https://mybinder.org/v2/gh/browniebroke/deezer-python/master?filepath=demo.ipynb).


Contributors
------------

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://www.twitter.com/_BrunoAlla"><img src="https://avatars1.githubusercontent.com/u/861044?v=4" width="100px;" alt=""/><br /><sub><b>Bruno Alla</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=browniebroke" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=browniebroke" title="Documentation">📖</a> <a href="#ideas-browniebroke" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-browniebroke" title="Maintenance">🚧</a> <a href="#platform-browniebroke" title="Packaging/porting to new platform">📦</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=browniebroke" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/misuzu"><img src="https://avatars1.githubusercontent.com/u/248143?v=4" width="100px;" alt=""/><br /><sub><b>misuzu</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=misuzu" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=misuzu" title="Documentation">📖</a> <a href="#ideas-misuzu" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=misuzu" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/pfouque"><img src="https://avatars1.githubusercontent.com/u/8300001?v=4" width="100px;" alt=""/><br /><sub><b>Pascal</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=pfouque" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=pfouque" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/khamaileon"><img src="https://avatars2.githubusercontent.com/u/1322166?v=4" width="100px;" alt=""/><br /><sub><b>khamaileon</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=khamaileon" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/sheregeda"><img src="https://avatars3.githubusercontent.com/u/2856444?v=4" width="100px;" alt=""/><br /><sub><b>Nikolay Sheregeda</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=sheregeda" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=sheregeda" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/horstmannmat"><img src="https://avatars1.githubusercontent.com/u/11761333?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Horstmann</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=horstmannmat" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=horstmannmat" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/MDCEY"><img src="https://avatars2.githubusercontent.com/u/3812864?v=4" width="100px;" alt=""/><br /><sub><b>Kieran Wynne</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=MDCEY" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/jnth"><img src="https://avatars0.githubusercontent.com/u/7796167?v=4" width="100px;" alt=""/><br /><sub><b>Jonathan Virga</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=jnth" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=jnth" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/hugovk"><img src="https://avatars2.githubusercontent.com/u/1324225?v=4" width="100px;" alt=""/><br /><sub><b>Hugo</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=hugovk" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/all-contributors/all-contributors-bot"><img src="https://avatars3.githubusercontent.com/u/46843839?v=4" width="100px;" alt=""/><br /><sub><b>allcontributors[bot]</b></sub></a><br /><a href="#infra-allcontributors" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/nrebena"><img src="https://avatars3.githubusercontent.com/u/49879400?v=4" width="100px;" alt=""/><br /><sub><b>nrebena</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/issues?q=author%3Anrebena" title="Bug reports">🐛</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=nrebena" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=nrebena" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/spvkgn"><img src="https://avatars0.githubusercontent.com/u/4147135?v=4" width="100px;" alt=""/><br /><sub><b>Pavel</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/issues?q=author%3Aspvkgn" title="Bug reports">🐛</a></td>
    <td align="center"><a href="http://www.idiap.ch || www.edeltech.ch"><img src="https://avatars0.githubusercontent.com/u/898010?v=4" width="100px;" alt=""/><br /><sub><b>Samuel Gaist</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=sgaist" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=sgaist" title="Tests">⚠️</a> <a href="#security-sgaist" title="Security">🛡️</a></td>
    <td align="center"><a href="https://github.com/hithomasmorelli"><img src="https://avatars0.githubusercontent.com/u/22722644?v=4" width="100px;" alt=""/><br /><sub><b>Thomas Morelli</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/issues?q=author%3Ahithomasmorelli" title="Bug reports">🐛</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=hithomasmorelli" title="Code">💻</a> <a href="#ideas-hithomasmorelli" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://naveen.syrusdark.website"><img src="https://avatars1.githubusercontent.com/u/49693820?v=4" width="100px;" alt=""/><br /><sub><b>Naveen M K</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=naveen521kk" title="Code">💻</a> <a href="#infra-naveen521kk" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://allcontributors.org) specification.
Contributions of any kind are welcome!
