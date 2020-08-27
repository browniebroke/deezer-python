# Changelog

## [Unreleased](https://github.com/browniebroke/deezer-python/tree/HEAD)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/1.6.0...HEAD)

### 🐛 Bug Fixes:

- Fix Playlist.iter\_fans, improve tests to catch similar errors [\#139](https://github.com/browniebroke/deezer-python/pull/139) ([hithomasmorelli](https://github.com/hithomasmorelli))

## [1.6.0](https://github.com/browniebroke/deezer-python/tree/1.6.0) (2020-08-20)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/1.5.0...1.6.0)

### 🚀 Enhancements:

- Fix crash for unknown resource, add Podcast & Episode resources [\#134](https://github.com/browniebroke/deezer-python/pull/134) ([hithomasmorelli](https://github.com/hithomasmorelli))
- 📦 Move package metadata to setup.cfg [\#91](https://github.com/browniebroke/deezer-python/pull/91) ([browniebroke](https://github.com/browniebroke))

### 📖 Documentation updates:

- Add hithomasmorelli as a contributor [\#138](https://github.com/browniebroke/deezer-python/pull/138) ([allcontributors[bot]](https://github.com/apps/allcontributors))

### ✅ Testing:

- Use codecov-action to upload coverage report [\#97](https://github.com/browniebroke/deezer-python/pull/97) ([browniebroke](https://github.com/browniebroke))
- Pin dependencies in requirements files [\#94](https://github.com/browniebroke/deezer-python/pull/94) ([browniebroke](https://github.com/browniebroke))
- ☂️ Increase test coverage to 100% [\#92](https://github.com/browniebroke/deezer-python/pull/92) ([browniebroke](https://github.com/browniebroke))

## [1.5.0](https://github.com/browniebroke/deezer-python/tree/1.5.0) (2020-07-01)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/1.4.0...1.5.0)

### 🚀 Enhancements:

- Add `get\_tracks` and `get\_fans` methods to `Playlist` resources [\#90](https://github.com/browniebroke/deezer-python/pull/90) ([browniebroke](https://github.com/browniebroke))

### 📖 Documentation updates:

- Migrate most of the docs to Markdown with MyST [\#85](https://github.com/browniebroke/deezer-python/pull/85) ([browniebroke](https://github.com/browniebroke))
- Improve documentation for resources [\#84](https://github.com/browniebroke/deezer-python/pull/84) ([browniebroke](https://github.com/browniebroke))

### ✅ Testing:

- Refactor tests to use the pytest style [\#89](https://github.com/browniebroke/deezer-python/pull/89) ([browniebroke](https://github.com/browniebroke))
- Split resources tests into multiple classes [\#88](https://github.com/browniebroke/deezer-python/pull/88) ([browniebroke](https://github.com/browniebroke))
- 🛠 Move CI to Github actions [\#86](https://github.com/browniebroke/deezer-python/pull/86) ([browniebroke](https://github.com/browniebroke))

## [1.4.0](https://github.com/browniebroke/deezer-python/tree/1.4.0) (2020-05-02)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/1.3.0...1.4.0)

### 🚀 Enhancements:

- Use explicit kwargs for the Client class [\#79](https://github.com/browniebroke/deezer-python/pull/79) ([browniebroke](https://github.com/browniebroke))

### 📖 Documentation updates:

- Documentation reworking and explain usage [\#78](https://github.com/browniebroke/deezer-python/pull/78) ([browniebroke](https://github.com/browniebroke))
- Auto generate changelog [\#75](https://github.com/browniebroke/deezer-python/pull/75) ([browniebroke](https://github.com/browniebroke))

### ✅ Testing:

- Clean-up config for coverage [\#80](https://github.com/browniebroke/deezer-python/pull/80) ([browniebroke](https://github.com/browniebroke))
- Use Python 3.8 on Travis \(drop the -dev\) [\#77](https://github.com/browniebroke/deezer-python/pull/77) ([browniebroke](https://github.com/browniebroke))
- Update names in Github action & run on Python 3.8 [\#76](https://github.com/browniebroke/deezer-python/pull/76) ([browniebroke](https://github.com/browniebroke))

## [1.3.0](https://github.com/browniebroke/deezer-python/tree/1.3.0) (2019-11-09)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/1.2.0...1.3.0)

### 🚀 Enhancements:

- Add Python 3.8 support [\#71](https://github.com/browniebroke/deezer-python/pull/71) ([jnth](https://github.com/jnth))

### 🐛 Bug Fixes:

- Get method error handling [\#64](https://github.com/browniebroke/deezer-python/pull/64) ([nrebena](https://github.com/nrebena))

### ✅ Testing:

- Add isort [\#72](https://github.com/browniebroke/deezer-python/pull/72) ([browniebroke](https://github.com/browniebroke))
- Remove appveyor.yml [\#70](https://github.com/browniebroke/deezer-python/pull/70) ([browniebroke](https://github.com/browniebroke))
- Move deploy step to a separate stage on Travis [\#61](https://github.com/browniebroke/deezer-python/pull/61) ([browniebroke](https://github.com/browniebroke))

## [1.2.0](https://github.com/browniebroke/deezer-python/tree/1.2.0) (2019-09-25)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/1.1.2...1.2.0)

### 🚀 Enhancements:

- Add a header kwarg in Client to force session headers [\#60](https://github.com/browniebroke/deezer-python/pull/60) ([jnth](https://github.com/jnth))
- Add user's favorite albums, artists, tracks and playlists in user resource. [\#53](https://github.com/browniebroke/deezer-python/pull/53) ([jnth](https://github.com/jnth))

### 📖 Documentation updates:

- Update Travis CI badge: travis.org -\> travis.com [\#57](https://github.com/browniebroke/deezer-python/pull/57) ([browniebroke](https://github.com/browniebroke))
- Create .config for all-contributors bot [\#51](https://github.com/browniebroke/deezer-python/pull/51) ([browniebroke](https://github.com/browniebroke))

### ✅ Testing:

- Create pythonpackage.yml to enable GitHub actions [\#58](https://github.com/browniebroke/deezer-python/pull/58) ([browniebroke](https://github.com/browniebroke))

## [1.1.0](https://github.com/browniebroke/deezer-python/tree/1.1.0) (2019-05-25)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/1.0.0...1.1.0)

### 💥 Breaking Changes:

- Drop support for EOL Python 3.4 [\#47](https://github.com/browniebroke/deezer-python/pull/47) ([hugovk](https://github.com/hugovk))

### 📖 Documentation updates:

- Update template to match filename [\#48](https://github.com/browniebroke/deezer-python/pull/48) ([hugovk](https://github.com/hugovk))

### ✅ Testing:

- Python 3.7+ support [\#44](https://github.com/browniebroke/deezer-python/pull/44) ([browniebroke](https://github.com/browniebroke))
- Test with `vcrpy` [\#43](https://github.com/browniebroke/deezer-python/pull/43) ([jnth](https://github.com/jnth))

## [1.0.0](https://github.com/browniebroke/deezer-python/tree/1.0.0) (2019-02-11)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.9.0...1.0.0)

### 💥 Breaking Changes:

- Drop Python 2 support [\#41](https://github.com/browniebroke/deezer-python/pull/41) ([hugovk](https://github.com/hugovk))

## [0.9.0](https://github.com/browniebroke/deezer-python/tree/0.9.0) (2019-02-10)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.8.0...0.9.0)

### 🚀 Enhancements:

- Add advanced search method [\#37](https://github.com/browniebroke/deezer-python/pull/37) ([jnth](https://github.com/jnth))

## [0.8.0](https://github.com/browniebroke/deezer-python/tree/0.8.0) (2018-10-30)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.7.0...0.8.0)

### 🚀 Enhancements:

- Auto-format code using black [\#35](https://github.com/browniebroke/deezer-python/pull/35) ([browniebroke](https://github.com/browniebroke))
- Make tornado an optional requirements [\#34](https://github.com/browniebroke/deezer-python/pull/34) ([browniebroke](https://github.com/browniebroke))
- Pagination feature [\#32](https://github.com/browniebroke/deezer-python/pull/32) ([MDCEY](https://github.com/MDCEY))

## [0.7.0](https://github.com/browniebroke/deezer-python/tree/0.7.0) (2018-10-03)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.6.1...0.7.0)

### 💥 Breaking Changes:

- Change name files names and docs from async [\#28](https://github.com/browniebroke/deezer-python/pull/28) ([horstmannmat](https://github.com/horstmannmat))

### 🚀 Enhancements:

- Store the session in the client [\#24](https://github.com/browniebroke/deezer-python/pull/24) ([sheregeda](https://github.com/sheregeda))

### ✅ Testing:

- Add a CI step for check-manifest [\#30](https://github.com/browniebroke/deezer-python/pull/30) ([browniebroke](https://github.com/browniebroke))
- Update build matrices [\#29](https://github.com/browniebroke/deezer-python/pull/29) ([browniebroke](https://github.com/browniebroke))
- Appveyor tests [\#25](https://github.com/browniebroke/deezer-python/pull/25) ([browniebroke](https://github.com/browniebroke))

## [0.6.1](https://github.com/browniebroke/deezer-python/tree/0.6.1) (2017-06-19)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.6.0...0.6.1)

### 🚀 Enhancements:

- Add access token to request kwargs [\#20](https://github.com/browniebroke/deezer-python/pull/20) ([sheregeda](https://github.com/sheregeda))

### 📖 Documentation updates:

- Update README.rst [\#18](https://github.com/browniebroke/deezer-python/pull/18) ([khamaileon](https://github.com/khamaileon))

## [0.6.0](https://github.com/browniebroke/deezer-python/tree/0.6.0) (2016-12-27)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.5.0...0.6.0)

### 🚀 Enhancements:

- Refactoring: replace urlopen by requests [\#16](https://github.com/browniebroke/deezer-python/pull/16) ([browniebroke](https://github.com/browniebroke))

## [0.5.0](https://github.com/browniebroke/deezer-python/tree/0.5.0) (2016-12-26)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.4.0...0.5.0)

### 📖 Documentation updates:

- Docs enhancements [\#13](https://github.com/browniebroke/deezer-python/pull/13) ([browniebroke](https://github.com/browniebroke))

### ✅ Testing:

- Run Flake8 on Travis [\#14](https://github.com/browniebroke/deezer-python/pull/14) ([browniebroke](https://github.com/browniebroke))
- Use tox-travis to integrate environments better [\#12](https://github.com/browniebroke/deezer-python/pull/12) ([browniebroke](https://github.com/browniebroke))

## [0.4.0](https://github.com/browniebroke/deezer-python/tree/0.4.0) (2016-12-08)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.3.0...0.4.0)

### 🚀 Enhancements:

- Improve chart integration [\#11](https://github.com/browniebroke/deezer-python/pull/11) ([pfouque](https://github.com/pfouque))
- Implement chart methods [\#8](https://github.com/browniebroke/deezer-python/pull/8) ([pfouque](https://github.com/pfouque))

### ✅ Testing:

- Switch from coveralls to codecov [\#9](https://github.com/browniebroke/deezer-python/pull/9) ([browniebroke](https://github.com/browniebroke))
- Correct a couple of flake8 warning [\#7](https://github.com/browniebroke/deezer-python/pull/7) ([browniebroke](https://github.com/browniebroke))
- Add basic flake8 config to setup.cfg [\#6](https://github.com/browniebroke/deezer-python/pull/6) ([browniebroke](https://github.com/browniebroke))

## [0.3.0](https://github.com/browniebroke/deezer-python/tree/0.3.0) (2016-11-09)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.2.3...0.3.0)

### 🚀 Enhancements:

- add resource parameters and iterators [\#5](https://github.com/browniebroke/deezer-python/pull/5) ([pfouque](https://github.com/pfouque))

## [0.2.1](https://github.com/browniebroke/deezer-python/tree/0.2.1) (2015-09-14)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.2...0.2.1)

### 🚀 Enhancements:

- Add pypy to the build matrix [\#10](https://github.com/browniebroke/deezer-python/pull/10) ([browniebroke](https://github.com/browniebroke))
- Run tests against Python 3.5 [\#3](https://github.com/browniebroke/deezer-python/pull/3) ([browniebroke](https://github.com/browniebroke))

## [0.2](https://github.com/browniebroke/deezer-python/tree/0.2) (2015-01-31)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.1...0.2)

### 🚀 Enhancements:

- Methods for resources [\#2](https://github.com/browniebroke/deezer-python/pull/2) ([misuzu](https://github.com/misuzu))

## [0.1](https://github.com/browniebroke/deezer-python/tree/0.1) (2014-11-23)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/e87692f7aeb80bc0ed858ccdf6165f0ac8f9c2ec...0.1)

### 🚀 Enhancements:

- Async client for Tornado, search [\#1](https://github.com/browniebroke/deezer-python/pull/1) ([misuzu](https://github.com/misuzu))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
