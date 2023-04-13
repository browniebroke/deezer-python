# Deezer Python Client

<p align="center">
  <a href="https://github.com/browniebroke/deezer-python/actions/workflows/ci.yml?query=branch%3Amain">
    <img alt="CI Status" src="https://img.shields.io/github/actions/workflow/status/browniebroke/deezer-python/ci.yml?branch=main&logo=github&style=flat-square">
  </a>
  <a href="https://readthedocs.org/projects/deezer-python/builds/">
    <img src="https://img.shields.io/readthedocs/deezer-python.svg?logo=read-the-docs&style=flat-square" alt="Documentation Status">
  </a>
  <a href="https://codecov.io/gh/browniebroke/deezer-python">
    <img src="https://img.shields.io/codecov/c/github/browniebroke/deezer-python.svg?logo=codecov&style=flat-square" alt="Test coverage percentage">
  </a>
</p>
<p align="center">
  <a href="https://python-poetry.org/">
    <img src="https://img.shields.io/badge/packaging-poetry-299bd7?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAASCAYAAABrXO8xAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJJSURBVHgBfZLPa1NBEMe/s7tNXoxW1KJQKaUHkXhQvHgW6UHQQ09CBS/6V3hKc/AP8CqCrUcpmop3Cx48eDB4yEECjVQrlZb80CRN8t6OM/teagVxYZi38+Yz853dJbzoMV3MM8cJUcLMSUKIE8AzQ2PieZzFxEJOHMOgMQQ+dUgSAckNXhapU/NMhDSWLs1B24A8sO1xrN4NECkcAC9ASkiIJc6k5TRiUDPhnyMMdhKc+Zx19l6SgyeW76BEONY9exVQMzKExGKwwPsCzza7KGSSWRWEQhyEaDXp6ZHEr416ygbiKYOd7TEWvvcQIeusHYMJGhTwF9y7sGnSwaWyFAiyoxzqW0PM/RjghPxF2pWReAowTEXnDh0xgcLs8l2YQmOrj3N7ByiqEoH0cARs4u78WgAVkoEDIDoOi3AkcLOHU60RIg5wC4ZuTC7FaHKQm8Hq1fQuSOBvX/sodmNJSB5geaF5CPIkUeecdMxieoRO5jz9bheL6/tXjrwCyX/UYBUcjCaWHljx1xiX6z9xEjkYAzbGVnB8pvLmyXm9ep+W8CmsSHQQY77Zx1zboxAV0w7ybMhQmfqdmmw3nEp1I0Z+FGO6M8LZdoyZnuzzBdjISicKRnpxzI9fPb+0oYXsNdyi+d3h9bm9MWYHFtPeIZfLwzmFDKy1ai3p+PDls1Llz4yyFpferxjnyjJDSEy9CaCx5m2cJPerq6Xm34eTrZt3PqxYO1XOwDYZrFlH1fWnpU38Y9HRze3lj0vOujZcXKuuXm3jP+s3KbZVra7y2EAAAAAASUVORK5CYII=" alt="Poetry">
  </a>
  <a href="https://github.com/ambv/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square" alt="black">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">
  </a>
</p>
<p align="center">
  <a href="https://mybinder.org/v2/gh/browniebroke/deezer-python/main?filepath=demo.ipynb">
    <img src="https://mybinder.org/badge_logo.svg" alt="Launch demo on Binder">
  </a>
  <a href="https://pypi.org/project/deezer-python/">
    <img src="https://img.shields.io/pypi/v/deezer-python.svg?logo=python&amp;logoColor=fff&amp;style=flat-square" alt="PyPi Status">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/deezer-python.svg?style=flat-square" alt="pyversions">
  <img src="https://img.shields.io/pypi/l/deezer-python.svg?style=flat-square" alt="license">
  <a href="https://github.com/browniebroke/deezer-python">
    <img src="https://tokei.rs/b1/github/browniebroke/deezer-python" alt="LoC">
  </a>
</p>

---

**Documentation**: <a href="https://deezer-python.readthedocs.io" target="_blank">https://deezer-python.readthedocs.io</a>

**Source Code**: <a href="https://github.com/browniebroke/deezer-python" target="_blank">https://github.com/browniebroke/deezer-python </a>

---

A friendly Python wrapper around the [Deezer API](https://developers.deezer.com/api).

## Installation

The package is published on
[PyPI](https://pypi.org/project/deezer-python/) and can be installed by running:

    pip install deezer-python

## Basic Use

Easily query the Deezer API from you Python code. The data returned by the Deezer
API is mapped to python resources:

```python
>>> client = deezer.Client()
>>> client.get_album(680407).title
'Monkey Business'
```

Ready for more? Look at our whole [documentation](http://deezer-python.readthedocs.io/)
on Read The Docs or have a play in pre-populated Jupyter notebook
[on Binder](https://mybinder.org/v2/gh/browniebroke/deezer-python/main?filepath=demo.ipynb).

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.twitter.com/_BrunoAlla"><img src="https://avatars1.githubusercontent.com/u/861044?v=4?s=100" width="100px;" alt="Bruno Alla"/><br /><sub><b>Bruno Alla</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=browniebroke" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=browniebroke" title="Documentation">📖</a> <a href="#ideas-browniebroke" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-browniebroke" title="Maintenance">🚧</a> <a href="#platform-browniebroke" title="Packaging/porting to new platform">📦</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=browniebroke" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/misuzu"><img src="https://avatars1.githubusercontent.com/u/248143?v=4?s=100" width="100px;" alt="misuzu"/><br /><sub><b>misuzu</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=misuzu" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=misuzu" title="Documentation">📖</a> <a href="#ideas-misuzu" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=misuzu" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/pfouque"><img src="https://avatars1.githubusercontent.com/u/8300001?v=4?s=100" width="100px;" alt="Pascal"/><br /><sub><b>Pascal</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=pfouque" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=pfouque" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/khamaileon"><img src="https://avatars2.githubusercontent.com/u/1322166?v=4?s=100" width="100px;" alt="khamaileon"/><br /><sub><b>khamaileon</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=khamaileon" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sheregeda"><img src="https://avatars3.githubusercontent.com/u/2856444?v=4?s=100" width="100px;" alt="Nikolay Sheregeda"/><br /><sub><b>Nikolay Sheregeda</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=sheregeda" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=sheregeda" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/horstmannmat"><img src="https://avatars1.githubusercontent.com/u/11761333?v=4?s=100" width="100px;" alt="Matheus Horstmann"/><br /><sub><b>Matheus Horstmann</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=horstmannmat" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=horstmannmat" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MDCEY"><img src="https://avatars2.githubusercontent.com/u/3812864?v=4?s=100" width="100px;" alt="Kieran Wynne"/><br /><sub><b>Kieran Wynne</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=MDCEY" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jnth"><img src="https://avatars0.githubusercontent.com/u/7796167?v=4?s=100" width="100px;" alt="Jonathan Virga"/><br /><sub><b>Jonathan Virga</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=jnth" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=jnth" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/hugovk"><img src="https://avatars2.githubusercontent.com/u/1324225?v=4?s=100" width="100px;" alt="Hugo"/><br /><sub><b>Hugo</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=hugovk" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/all-contributors/all-contributors-bot"><img src="https://avatars3.githubusercontent.com/u/46843839?v=4?s=100" width="100px;" alt="allcontributors[bot]"/><br /><sub><b>allcontributors[bot]</b></sub></a><br /><a href="#infra-allcontributors" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nrebena"><img src="https://avatars3.githubusercontent.com/u/49879400?v=4?s=100" width="100px;" alt="nrebena"/><br /><sub><b>nrebena</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/issues?q=author%3Anrebena" title="Bug reports">🐛</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=nrebena" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=nrebena" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/spvkgn"><img src="https://avatars0.githubusercontent.com/u/4147135?v=4?s=100" width="100px;" alt="Pavel"/><br /><sub><b>Pavel</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/issues?q=author%3Aspvkgn" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.idiap.ch || www.edeltech.ch"><img src="https://avatars0.githubusercontent.com/u/898010?v=4?s=100" width="100px;" alt="Samuel Gaist"/><br /><sub><b>Samuel Gaist</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=sgaist" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=sgaist" title="Tests">⚠️</a> <a href="#security-sgaist" title="Security">🛡️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/hithomasmorelli"><img src="https://avatars0.githubusercontent.com/u/22722644?v=4?s=100" width="100px;" alt="Thomas Morelli"/><br /><sub><b>Thomas Morelli</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/issues?q=author%3Ahithomasmorelli" title="Bug reports">🐛</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=hithomasmorelli" title="Code">💻</a> <a href="#ideas-hithomasmorelli" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://naveen.syrusdark.website"><img src="https://avatars1.githubusercontent.com/u/49693820?v=4?s=100" width="100px;" alt="Naveen M K"/><br /><sub><b>Naveen M K</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=naveen521kk" title="Code">💻</a> <a href="#infra-naveen521kk" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Carababusha"><img src="https://avatars.githubusercontent.com/u/64437819?v=4?s=100" width="100px;" alt="Carababusha"/><br /><sub><b>Carababusha</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=Carababusha" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/bjacquin"><img src="https://avatars.githubusercontent.com/u/5293357?v=4?s=100" width="100px;" alt="Bertrand Jacquin"/><br /><sub><b>Bertrand Jacquin</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=bjacquin" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/prndrbr"><img src="https://avatars.githubusercontent.com/u/96344856?v=4?s=100" width="100px;" alt="Pierre"/><br /><sub><b>Pierre</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=prndrbr" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=prndrbr" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://jonathanbangert.com"><img src="https://avatars.githubusercontent.com/u/74015378?v=4?s=100" width="100px;" alt="Jonathan"/><br /><sub><b>Jonathan</b></sub></a><br /><a href="https://github.com/browniebroke/deezer-python/commits?author=Un10ck3d" title="Code">💻</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=Un10ck3d" title="Documentation">📖</a> <a href="https://github.com/browniebroke/deezer-python/commits?author=Un10ck3d" title="Tests">⚠️</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://allcontributors.org) specification.
Contributions of any kind are welcome!
