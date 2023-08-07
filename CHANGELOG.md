# CHANGELOG

## v6.1.0 (2023-08-07)

### Feature

- Add official support for python 3.12 (#791) ([`2eead31`](https://github.com/browniebroke/deezer-python/commit/2eead316d78128c85d365b664c2e3a926c65913a))

### Documentation

- Switch to furo theme (#766) ([`51cfb08`](https://github.com/browniebroke/deezer-python/commit/51cfb082c0df50a8726e1ae26ebfeca389e5d952))

## v6.0.0 (2023-06-27)

### Feature

- Drop support for Python 3.7 ([#758](https://github.com/browniebroke/deezer-python/issues/758)) ([`d80f1e7`](https://github.com/browniebroke/deezer-python/commit/d80f1e75fc4e979938a3241d8244bc3fbbd31c23))

### Breaking

- Drop support for Python 3.7 as it reached EOL on June 27, 2023. More infos: https://devguide.python.org/versions/ ([`d80f1e7`](https://github.com/browniebroke/deezer-python/commit/d80f1e75fc4e979938a3241d8244bc3fbbd31c23))

## v5.12.0 (2023-05-11)

### Feature

- Add `User.create_playlist` method ([`c768a8b`](https://github.com/browniebroke/deezer-python/commit/c768a8be4b116c09325a3c0cfb19c941adbd257b))
- Add `User.remove_playlist` method ([`289f021`](https://github.com/browniebroke/deezer-python/commit/289f0216f485573b484a76b533adfceb2d7a803e))
- Add `User.add_playlist` method ([`7ec9bc9`](https://github.com/browniebroke/deezer-python/commit/7ec9bc99e3529680561d00c8c5d4d36c5fda176c))
- Add `User.unfollow` method ([`59b9329`](https://github.com/browniebroke/deezer-python/commit/59b9329b4c41a5d9c6a2906e0575758eb9e93c26))
- Add `User.follow` method ([`949918a`](https://github.com/browniebroke/deezer-python/commit/949918a39fdf6feff7ab5482d0fb7de6ac44dc59))
- Add `User.remove_artist` method ([`70825bf`](https://github.com/browniebroke/deezer-python/commit/70825bfc1ed6521df1ca5802661f66a6d7e9eb20))
- Add `User.add_artist` method ([`3ad512b`](https://github.com/browniebroke/deezer-python/commit/3ad512be6abd3e4dce16ae1a4deb25ef26a1072f))
- Add `User.remove_Track` method ([`ccc7b76`](https://github.com/browniebroke/deezer-python/commit/ccc7b76bbdb8aebca50511043d87c057f39d07ec))
- Add `User.add_track` method ([`1d9d3d2`](https://github.com/browniebroke/deezer-python/commit/1d9d3d2e0bfb7a1a9b613608ded879173a646c5b))
- Add `User.remove_album` method ([`103c58b`](https://github.com/browniebroke/deezer-python/commit/103c58bf69b573d2b1170ebcc60dee97db2f1a06))
- Add `User.add_album` method ([`013adde`](https://github.com/browniebroke/deezer-python/commit/013addeeebfe70388953c439986e60e15ff8eea9))

## v5.11.1 (2023-05-10)

### Fix

- Rename argument for `Playlist.reorder_tracks` back to `order` to match parameter name from REST API ([`ea469e9`](https://github.com/browniebroke/deezer-python/commit/ea469e9f61b78cba741b8a577bf0a80d23e8cab5))

## v5.11.0 (2023-05-09)

### Feature

- Add ability to remove a bookmark on an episode ([`4eb896a`](https://github.com/browniebroke/deezer-python/commit/4eb896a207c36609bf08498e58ecbcf670ec8fbc))
- Add ability to add a bookmark to an episode ([`6dc32ac`](https://github.com/browniebroke/deezer-python/commit/6dc32ac7f90839483504f6312be799a64f607b6e))
- Add ability to mark a playlist as seen ([`dac1530`](https://github.com/browniebroke/deezer-python/commit/dac1530d278097b545bdb7f942ab3c4e701ca097))

## v5.10.0 (2023-05-08)

### Feature

- **playlists:** Add functions to create, edit, reorder and delete playlists and edit user library playlists ([#709](https://github.com/browniebroke/deezer-python/issues/709)) ([`5257988`](https://github.com/browniebroke/deezer-python/commit/525798801e341ddbc43bad974aa0b4c58a1e63a8))

## v5.9.0 (2023-04-13)

### Feature

- **search:** Add search function for playlists ([`318d524`](https://github.com/browniebroke/deezer-python/commit/318d5249bd51de6f007ad5f839b6339069415fc0))
- **recommendations:** Add flow and recommendation functions ([`a03ac81`](https://github.com/browniebroke/deezer-python/commit/a03ac81f9c3d3b46265746b4be8d980fc93ada28))

### Documentation

- Add Un10ck3d as a contributor for code, doc, and test ([#693](https://github.com/browniebroke/deezer-python/issues/693)) ([`0371bc4`](https://github.com/browniebroke/deezer-python/commit/0371bc4e95949b85b286ea882eba6f11dc98c715))
- Move docs in a single folder ([#634](https://github.com/browniebroke/deezer-python/issues/634)) ([`bb7b3d1`](https://github.com/browniebroke/deezer-python/commit/bb7b3d15a37af411a5c66db2bf569e49e8f965ce))
- Improve links between docs and source code ([#632](https://github.com/browniebroke/deezer-python/issues/632)) ([`7258900`](https://github.com/browniebroke/deezer-python/commit/7258900b6df3c44d3b05eb5a205996c1fe173609))

## v5.8.1 (2022-12-02)

### Fix

- Add Twitter and Mastodon links to PyPI ([#631](https://github.com/browniebroke/deezer-python/issues/631)) ([`1a57b64`](https://github.com/browniebroke/deezer-python/commit/1a57b64e2bc0d38dd70e18dd815afbc8376c6d1f))

## v5.8.0 (2022-11-20)

### Feature

- Officially support Python 3.11 ([#617](https://github.com/browniebroke/deezer-python/issues/617)) ([`f737d5b`](https://github.com/browniebroke/deezer-python/commit/f737d5b0011339fefdeacf2fae80834c39ddf293))

## v5.7.0 (2022-11-11)

### Feature

- Manage user's friends ([#610](https://github.com/browniebroke/deezer-python/issues/610)) ([`6e116f5`](https://github.com/browniebroke/deezer-python/commit/6e116f5dfaab8f122a77c2c01d53fa0f7d8cac5e))

## v5.6.0 (2022-09-06)

### Feature

- Show a content preview of the paginated list in the CLI ([#568](https://github.com/browniebroke/deezer-python/issues/568)) ([`283d190`](https://github.com/browniebroke/deezer-python/commit/283d190fe42f2272036fe3e17c4f9de11881b0e8))

### Documentation

- Fix links to resources and pagination classes ([#567](https://github.com/browniebroke/deezer-python/issues/567)) ([`1adce18`](https://github.com/browniebroke/deezer-python/commit/1adce18c671020fc3f4ca3b8b0e0e4d1e2eb4f43))
- Fix errors in search usage documentation ([#566](https://github.com/browniebroke/deezer-python/issues/566)) ([`d5c2e84`](https://github.com/browniebroke/deezer-python/commit/d5c2e84ed52338fd4e39abf62068942e01f2c553))

## v5.5.0 (2022-07-26)

### Feature

- Infer episode link & share from ID when missing ([#544](https://github.com/browniebroke/deezer-python/issues/544)) ([`f38a038`](https://github.com/browniebroke/deezer-python/commit/f38a03812c73f74eedf8077ffd29a1b2b7a67188))

## v5.4.0 (2022-07-25)

### Feature

- Fetch resource if accessing missing field on simplified instance ([#541](https://github.com/browniebroke/deezer-python/issues/541)) ([`df5e81b`](https://github.com/browniebroke/deezer-python/commit/df5e81bd36e458af6a1bca9e02c8e341bba5b4c5))

## v5.3.3 (2022-06-06)

### Fix

- **deps:** Revert PSR upgrade ([`f5119fc`](https://github.com/browniebroke/deezer-python/commit/f5119fc3f1c562f3f875adde5810b08e4fa394b3))

## v5.3.2 (2022-04-28)

### Fix

- Remove rate album methods ([`3000fa7`](https://github.com/browniebroke/deezer-python/commit/3000fa7d34c6d9e5dc90f9c60c54308e2a7e6beb))

## v5.3.1 (2022-04-23)

### Fix

- Add a few missing classes to top level API ([`98ef1a1`](https://github.com/browniebroke/deezer-python/commit/98ef1a1a0b146f34e80a87308cfb1909d5d0eb7a))

### Documentation

- Reference each class from the top level ([`042ee17`](https://github.com/browniebroke/deezer-python/commit/042ee17e34a5bb5cbf28225e3634c5e414cc442c))

## v5.3.0 (2022-04-23)

### Feature

- Get charts for a specified genre ID ([`dad1d94`](https://github.com/browniebroke/deezer-python/commit/dad1d94f6a5f6c52d107aab855509cdc382d38c7))

## v5.2.0 (2022-02-09)

### Feature

- Get the top podcasts ([`f8f3438`](https://github.com/browniebroke/deezer-python/commit/f8f3438f38ce3ecb380bffd122b299880560d654))
- Get all podcasts for a genre ([`8f220fd`](https://github.com/browniebroke/deezer-python/commit/8f220fd7b4351766b57dbe38876855b73f62aab7))
- Get a list of artist's playlists ([`bd0f5ee`](https://github.com/browniebroke/deezer-python/commit/bd0f5eedbd610c0cf4da9fdabbbd9560a2669bf1))

## v5.1.1 (2022-02-07)

### Fix

- Make `Client.list_radios` return a `list` ([`cfb3f98`](https://github.com/browniebroke/deezer-python/commit/cfb3f983d3753904c6f7668faab6348cf15c6331))
- Make `Client.list_genres` return a `list` ([`ca83963`](https://github.com/browniebroke/deezer-python/commit/ca839632ef178001398e786652de59e4bbbeb09e))

### Documentation

- Complete `Client.get_user_albums` return type ([`46846dc`](https://github.com/browniebroke/deezer-python/commit/46846dc6b7b801846c528798f0fdd88e0a57d5d0))

## v5.1.0 (2022-02-02)

### Feature

- Add `Editorial` resource ([`b98888e`](https://github.com/browniebroke/deezer-python/commit/b98888ec131f015f5e3ba14d3be45f52fdb60e11))

### Documentation

- Update contributions for prndrbr ([`eae4bfb`](https://github.com/browniebroke/deezer-python/commit/eae4bfb6599f52f17238f5f86595a6c41af55377))

## v5.0.1 (2022-01-28)

### Fix

- `Genre` methods return a list ([`2c15056`](https://github.com/browniebroke/deezer-python/commit/2c15056c22226ef68a9c694363a3b6e915e7cff5))

### Documentation

- Fix type hints and add documentation ([`beeacc4`](https://github.com/browniebroke/deezer-python/commit/beeacc46b6fc3ad4c99d791bfce832cdf22af167))
- Fix a few urls in README.md ([`c12120b`](https://github.com/browniebroke/deezer-python/commit/c12120bee9b45da5aa6c6fa2bf9e111cce5ae141))
- Add prndrbr as a contributor for doc ([#442](https://github.com/browniebroke/deezer-python/issues/442)) ([`4387822`](https://github.com/browniebroke/deezer-python/commit/4387822f6317a8fb92f4f055173a8c9cb7c0b59a))
- Fix a few typos ([`69755f2`](https://github.com/browniebroke/deezer-python/commit/69755f2ff1382694cb93eab89d1daf7321129441))
- Update contributing guide ([`a673690`](https://github.com/browniebroke/deezer-python/commit/a673690ee781ab9af7c46001d7ac9f087cc2f406))
- Update contributing guide ([`ca60f3c`](https://github.com/browniebroke/deezer-python/commit/ca60f3cbc5a1e654e5c0e288ac55c850145f2e99))
- Fix outdated installation instruction ([`1129210`](https://github.com/browniebroke/deezer-python/commit/1129210ae60685385484fdb2ffeba51f11f1bd54))

## v5.0.0 (2022-01-17)

### Feature

- Add `PaginationList` to improve how we deal with pagination ([#425](https://github.com/browniebroke/deezer-python/issues/425)) ([`6a4ccf2`](https://github.com/browniebroke/deezer-python/commit/6a4ccf2f3c2a50109a6aaded2510b16d64e354ac))
- Remove the tornado-based `AsyncClient` ([#427](https://github.com/browniebroke/deezer-python/issues/427)) ([`96df7b8`](https://github.com/browniebroke/deezer-python/commit/96df7b861881732f313bd19e53c7b5a27fcb84bb))

### Breaking

- support for Python 3.6 is dropped ([`6562a4c`](https://github.com/browniebroke/deezer-python/commit/6562a4c53810c283a9682931408160aa542f4de2))
- paginated responses are now managed via a `PaginatedList` wrapper class. As a result, the `iter_...` methods have been removed from all resources and merged into the corresponding `get_...` method. Search result also make use of these new paginated responses. ([`6a4ccf2`](https://github.com/browniebroke/deezer-python/commit/6a4ccf2f3c2a50109a6aaded2510b16d64e354ac))
- the `AsyncClient`, based on Tornado, has been removed. If you still need it, stay on earlier version or vendor it into your codebase. ([`96df7b8`](https://github.com/browniebroke/deezer-python/commit/96df7b861881732f313bd19e53c7b5a27fcb84bb))

### Documentation

- Show resources attributes and their type ([`383ffa3`](https://github.com/browniebroke/deezer-python/commit/383ffa312d71cc1036ba7a57adb27947a487a671))
- Split documentation for resources into multiple pages ([`4e96f75`](https://github.com/browniebroke/deezer-python/commit/4e96f75f1b3dc93651e07bcc4e2d2d4df89d42d8))
- Fix mention of `as_dict()` method ([`0bfb849`](https://github.com/browniebroke/deezer-python/commit/0bfb849d5ab4bcd90ea913f849bd2c70e3226ac9))
- Fix a few typos and reformat files ([`91b8f5c`](https://github.com/browniebroke/deezer-python/commit/91b8f5c938b367b736c65252d04eee72e668aea3))
- Reword section about authentication ([`1e7b9e3`](https://github.com/browniebroke/deezer-python/commit/1e7b9e3b75622f930398240a2c6b45d07dd45c3d))

## v4.3.0 (2022-01-03)

### Feature

- Parse track contributors ([`719e42a`](https://github.com/browniebroke/deezer-python/commit/719e42aff6f0c21bd92aaa063bf94076021f1a42))
- Parse album contributors ([`bd02ec4`](https://github.com/browniebroke/deezer-python/commit/bd02ec41c20ddbff2cc399f496f64b8f095c4854))

## v4.2.1 (2021-12-11)

### Fix

- **deps:** Update dependency myst-parser to ^0.16 ([`2fe0e71`](https://github.com/browniebroke/deezer-python/commit/2fe0e714aa9e35db2a3aa89911ae086b54cf58e7))

## v4.2.0 (2021-12-07)

### Feature

- Deserialize date in `Resource.as_dict()` method ([#399](https://github.com/browniebroke/deezer-python/issues/399)) ([`6337967`](https://github.com/browniebroke/deezer-python/commit/6337967a370bfb6a4fb057f84fe94f0b932fa421))

### Fix

- Follow Deezer's format when deserializing datetime ([#411](https://github.com/browniebroke/deezer-python/issues/411)) ([`3be65e4`](https://github.com/browniebroke/deezer-python/commit/3be65e4242343dbf9014d76f3c46d1d424975be6))

### Documentation

- Add bjacquin as a contributor for code ([#410](https://github.com/browniebroke/deezer-python/issues/410)) ([`138d317`](https://github.com/browniebroke/deezer-python/commit/138d317f026e6ce00f4040cd873bf30f89a21b9a))

## v4.1.0 (2021-10-20)

### Feature

- Add all documented fields to resources and type annotate them ([`9b093b2`](https://github.com/browniebroke/deezer-python/commit/9b093b26590e00f3b0a956cc4f4c54e9c24a43a7))
- Add support for getting the current user ([`5e9b56e`](https://github.com/browniebroke/deezer-python/commit/5e9b56ea8f13845c81f18f7442e89a2afe28babd))

## v4.0.0 (2021-10-17)

### Feature

- Port `Client`'s `request` method to `AsyncClient` ([`bd9edb2`](https://github.com/browniebroke/deezer-python/commit/bd9edb2bff0fb450ed7c438b13df40eed0a970f0))
- Refactor existing methods to use newer request ([`0ddc5c2`](https://github.com/browniebroke/deezer-python/commit/0ddc5c21cec62d06e38ba42e4e82df8ff35bd73d))

### Fix

- Remove `Comment` resource as it's no longer in the Deezer API ([`6bb0647`](https://github.com/browniebroke/deezer-python/commit/6bb064734e8104d0cb23b666143f010be421982f))
- Make `Resource.get_relation` work with Tornado client ([`0980055`](https://github.com/browniebroke/deezer-python/commit/0980055d7754c53e5cc437b187b74329a9cffc95))

### Breaking

- the `advanced_search` method no longer exists and has been merged into the regular `search` method. ([`46cf5f1`](https://github.com/browniebroke/deezer-python/commit/46cf5f1453692e1ee61c15e1fd87093ea99b636f))
- The `get_object`, `object_url` and `url` methods have been removed from the `Client` and `AsyncClient` classes ([`3b7c167`](https://github.com/browniebroke/deezer-python/commit/3b7c16725114e3aea25584014617b298b8483e31))
- The `Client.get_radios` method has been removed and replaced by `Client.list_radios` ([`b7d940f`](https://github.com/browniebroke/deezer-python/commit/b7d940fcf16450a804adfb8552a1cba6ab97a8c6))
- The `Client.get_genres` method has been removed and replaced by `Client.list_genres` ([`2e284af`](https://github.com/browniebroke/deezer-python/commit/2e284af9d15941ac842fdb24e74eaa8ae3abb5d3))
- A `DeezerErrorResponse` is now raised in case of error, instead of `ValueError` ([`0ddc5c2`](https://github.com/browniebroke/deezer-python/commit/0ddc5c21cec62d06e38ba42e4e82df8ff35bd73d))

## v3.2.0 (2021-10-15)

### Feature

- Get current user's listening history ([`43ea8ca`](https://github.com/browniebroke/deezer-python/commit/43ea8cab43a2b1b778f478d9dc8df1a478454bf9))

### Documentation

- Update contributing guide with recent simplifications ([`0181cda`](https://github.com/browniebroke/deezer-python/commit/0181cda9cf420dbdffbcfadd731e3a8069eb199e))
- Add Carababusha as a contributor for code ([#390](https://github.com/browniebroke/deezer-python/issues/390)) ([`257a48f`](https://github.com/browniebroke/deezer-python/commit/257a48fedb2f068fac42e6d9bde7709d24846bb4))
- Update contributing guide to avoid leaking API tokens ([`784146e`](https://github.com/browniebroke/deezer-python/commit/784146e759db6750d415ba6611aea443137b275b))

## v3.1.0 (2021-10-09)

### Feature

- Ability to manage tracks from the user's library ([`59b0f57`](https://github.com/browniebroke/deezer-python/commit/59b0f578127a99622632f51359ba88cc23dcaa1b))
- Ability to manage artists from the user's library ([`10f2967`](https://github.com/browniebroke/deezer-python/commit/10f29678c262be6349703ed093f0dbb96eea256a))
- Ability to manage albums from the user's library ([`45f9bba`](https://github.com/browniebroke/deezer-python/commit/45f9bbac416a359a06cc7c2b270161dff8119a8d))
- Add support to rate an album ([`c8dc771`](https://github.com/browniebroke/deezer-python/commit/c8dc771b6c11c927cd599dc88563b9ec6db2f994))
- Add support to rate an album ([`1c72557`](https://github.com/browniebroke/deezer-python/commit/1c725572fa66839ddc1f7ed3b1f7a529a8d0572d))
- Basic structure to support POST method ([`9da4e81`](https://github.com/browniebroke/deezer-python/commit/9da4e81ed80c516d806502eed4b1671eb944b75c))

## v3.0.0 (2021-10-09)

### Breaking

- remove deprecated `asdict` method on `Resource` class ([`daeee61`](https://github.com/browniebroke/deezer-python/commit/daeee6131d249106a2233e432a179aba40cdbbc8))
- remove deprecated `host` and `use_ssl` arguments for `Client` ([`2bd2c39`](https://github.com/browniebroke/deezer-python/commit/2bd2c39988066999d3ae34995e1e98c31d6c5a17))

### Documentation

- Use https in link ([`f7eb114`](https://github.com/browniebroke/deezer-python/commit/f7eb114e4d1d0dba9e8a65f25cb2ce842270036e))

## v2.4.0 (2021-10-07)

### Feature

- Add official python 3.10 support ([`b29b0cb`](https://github.com/browniebroke/deezer-python/commit/b29b0cb87e025bc52663c8d81d0f1dd94277badc))

## v2.3.1 (2021-09-13)

### Fix

- **deps:** Update dependency sphinx-rtd-theme to v1 ([`af43757`](https://github.com/browniebroke/deezer-python/commit/af43757238760ca8fa23ff67cafa11cd8dd74eea))

### Documentation

- Fix docstrings ([`0e87749`](https://github.com/browniebroke/deezer-python/commit/0e87749c182f59b40341f85b61dbb73578ed6567))

## v2.3.0 (2021-06-27)

### Feature

- Deprecate the `asdict` method from the `Resource` class ([`412b954`](https://github.com/browniebroke/deezer-python/commit/412b954791f9759028ad8320528f56347cc89d1b))

## v2.2.4 (2021-06-13)

### Fix

- **deps:** Update dependency myst-parser to ^0.15 ([`81ed3d8`](https://github.com/browniebroke/deezer-python/commit/81ed3d88389a321d4fb2d980d1154a055060e8c8))

## v2.2.3 (2021-05-04)

### Fix

- **deps:** Update dependency myst-parser to ^0.14 ([`9fbc55a`](https://github.com/browniebroke/deezer-python/commit/9fbc55a7371dd6c2bba1d9dd2d9b9f6650c37df2))

## v2.2.2 (2021-04-06)

### Fix

- Release in a separate environment ([`4d987d0`](https://github.com/browniebroke/deezer-python/commit/4d987d0076c2e763424eeadd9c6cbbbf71706498))
- **deps:** Update dependency sphinx-autobuild to v2021 ([`f70a1bd`](https://github.com/browniebroke/deezer-python/commit/f70a1bda9c28e1cf2d1d1140a0fbf482ae0bc6cb))
- **deps:** Update dependency myst-parser to ^0.13 ([`73255fb`](https://github.com/browniebroke/deezer-python/commit/73255fb3c79f28155744ff7ff37511761e17abd6))

## v2.2.1 (2020-10-23)

### Fix

- Set minimum python version to 3.6 ([`4ff223d`](https://github.com/browniebroke/deezer-python/commit/4ff223df0e144ecddcd0eb2918b2ed161776490a))
- Poetry extras ([`cc36e0f`](https://github.com/browniebroke/deezer-python/commit/cc36e0ffa70267efee6aeeff169d7dd186a73ea6))

## v2.2.0 (2020-10-13)

### Feature

- Switch to Poetry (#196) ([`92030dd`](https://github.com/browniebroke/deezer-python/commit/92030dd9409ba906716cea3f7f49e30a9a5a8cf7))

### Fix

- Build command for PSR ([`c76b8ea`](https://github.com/browniebroke/deezer-python/commit/c76b8ea5f396586ab9eddf4bdd265438d0410351))

## v2.1.0 (2020-10-10)

### Feature

- Add support for python 3.9 ([`b4669ee`](https://github.com/browniebroke/deezer-python/commit/b4669ee0e1f698529b78a37c64d6daf210d8970a))

### Documentation

- Add naveen521kk as a contributor (#171) ([`0df16d3`](https://github.com/browniebroke/deezer-python/commit/0df16d34c1005ade3751f6f762e06387440894a8))

## v2.0.0 (2020-10-01)

### Feature

- Drop support for Python 3.5 ([`20d999b`](https://github.com/browniebroke/deezer-python/commit/20d999ba370cf0bc643434d8257cfd9821ef26de))

### Fix

- Include docs/\*.md files in package ([`5fcc38d`](https://github.com/browniebroke/deezer-python/commit/5fcc38df6e9137fd9d4d362141e428727a632565))

### Breaking

- dropping EOL Python version ([`20d999b`](https://github.com/browniebroke/deezer-python/commit/20d999ba370cf0bc643434d8257cfd9821ef26de))

## v1.6.2 (2020-09-21)

### Fix

- Remove universal wheel option ([`5f31f14`](https://github.com/browniebroke/deezer-python/commit/5f31f14ce77f9363b33ba42130ad190cbd4fe4ce))
- Fix missing requirements when running tests ([`cb7d421`](https://github.com/browniebroke/deezer-python/commit/cb7d421ddaa166f168dcaff42c2944fd3334437a))
- Fix configuration for python-semantic-release ([`dd446d2`](https://github.com/browniebroke/deezer-python/commit/dd446d2d438c6045ea2640776f80d7ee7ce29e66))

## [v1.6.1](https://github.com/browniebroke/deezer-python/tree/1.6.1) (2020-08-27)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/1.6.0...1.6.1)

### 🐛 Bug Fixes:

- Fix Playlist.iter_fans, improve tests to catch similar errors [\#139](https://github.com/browniebroke/deezer-python/pull/139) ([hithomasmorelli](https://github.com/hithomasmorelli))

## [v1.6.0](https://github.com/browniebroke/deezer-python/tree/1.6.0) (2020-08-20)

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

## [v1.5.0](https://github.com/browniebroke/deezer-python/tree/1.5.0) (2020-07-01)

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

## [v1.4.0](https://github.com/browniebroke/deezer-python/tree/1.4.0) (2020-05-02)

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

## [v1.3.0](https://github.com/browniebroke/deezer-python/tree/1.3.0) (2019-11-09)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/1.2.0...1.3.0)

### 🚀 Enhancements:

- Add Python 3.8 support [\#71](https://github.com/browniebroke/deezer-python/pull/71) ([jnth](https://github.com/jnth))

### 🐛 Bug Fixes:

- Get method error handling [\#64](https://github.com/browniebroke/deezer-python/pull/64) ([nrebena](https://github.com/nrebena))

### ✅ Testing:

- Add isort [\#72](https://github.com/browniebroke/deezer-python/pull/72) ([browniebroke](https://github.com/browniebroke))
- Remove appveyor.yml [\#70](https://github.com/browniebroke/deezer-python/pull/70) ([browniebroke](https://github.com/browniebroke))
- Move deploy step to a separate stage on Travis [\#61](https://github.com/browniebroke/deezer-python/pull/61) ([browniebroke](https://github.com/browniebroke))

## [v1.2.0](https://github.com/browniebroke/deezer-python/tree/1.2.0) (2019-09-25)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/1.1.2...1.2.0)

### 🚀 Enhancements:

- Add a header kwarg in Client to force session headers [\#60](https://github.com/browniebroke/deezer-python/pull/60) ([jnth](https://github.com/jnth))
- Add user's favorite albums, artists, tracks and playlists in user resource. [\#53](https://github.com/browniebroke/deezer-python/pull/53) ([jnth](https://github.com/jnth))

### 📖 Documentation updates:

- Update Travis CI badge: travis.org -\> travis.com [\#57](https://github.com/browniebroke/deezer-python/pull/57) ([browniebroke](https://github.com/browniebroke))
- Create .config for all-contributors bot [\#51](https://github.com/browniebroke/deezer-python/pull/51) ([browniebroke](https://github.com/browniebroke))

### ✅ Testing:

- Create pythonpackage.yml to enable GitHub actions [\#58](https://github.com/browniebroke/deezer-python/pull/58) ([browniebroke](https://github.com/browniebroke))

## [v1.1.0](https://github.com/browniebroke/deezer-python/tree/1.1.0) (2019-05-25)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/1.0.0...1.1.0)

### 💥 Breaking Changes:

- Drop support for EOL Python 3.4 [\#47](https://github.com/browniebroke/deezer-python/pull/47) ([hugovk](https://github.com/hugovk))

### 📖 Documentation updates:

- Update template to match filename [\#48](https://github.com/browniebroke/deezer-python/pull/48) ([hugovk](https://github.com/hugovk))

### ✅ Testing:

- Python 3.7+ support [\#44](https://github.com/browniebroke/deezer-python/pull/44) ([browniebroke](https://github.com/browniebroke))
- Test with `vcrpy` [\#43](https://github.com/browniebroke/deezer-python/pull/43) ([jnth](https://github.com/jnth))

## [v1.0.0](https://github.com/browniebroke/deezer-python/tree/1.0.0) (2019-02-11)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.9.0...1.0.0)

### 💥 Breaking Changes:

- Drop Python 2 support [\#41](https://github.com/browniebroke/deezer-python/pull/41) ([hugovk](https://github.com/hugovk))

## [v0.9.0](https://github.com/browniebroke/deezer-python/tree/0.9.0) (2019-02-10)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.8.0...0.9.0)

### 🚀 Enhancements:

- Add advanced search method [\#37](https://github.com/browniebroke/deezer-python/pull/37) ([jnth](https://github.com/jnth))

## [v0.8.0](https://github.com/browniebroke/deezer-python/tree/0.8.0) (2018-10-30)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.7.0...0.8.0)

### 🚀 Enhancements:

- Auto-format code using black [\#35](https://github.com/browniebroke/deezer-python/pull/35) ([browniebroke](https://github.com/browniebroke))
- Make tornado an optional requirements [\#34](https://github.com/browniebroke/deezer-python/pull/34) ([browniebroke](https://github.com/browniebroke))
- Pagination feature [\#32](https://github.com/browniebroke/deezer-python/pull/32) ([MDCEY](https://github.com/MDCEY))

## [v0.7.0](https://github.com/browniebroke/deezer-python/tree/0.7.0) (2018-10-03)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.6.1...0.7.0)

### 💥 Breaking Changes:

- Change name files names and docs from async [\#28](https://github.com/browniebroke/deezer-python/pull/28) ([horstmannmat](https://github.com/horstmannmat))

### 🚀 Enhancements:

- Store the session in the client [\#24](https://github.com/browniebroke/deezer-python/pull/24) ([sheregeda](https://github.com/sheregeda))

### ✅ Testing:

- Add a CI step for check-manifest [\#30](https://github.com/browniebroke/deezer-python/pull/30) ([browniebroke](https://github.com/browniebroke))
- Update build matrices [\#29](https://github.com/browniebroke/deezer-python/pull/29) ([browniebroke](https://github.com/browniebroke))
- Appveyor tests [\#25](https://github.com/browniebroke/deezer-python/pull/25) ([browniebroke](https://github.com/browniebroke))

## [v0.6.1](https://github.com/browniebroke/deezer-python/tree/0.6.1) (2017-06-19)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.6.0...0.6.1)

### 🚀 Enhancements:

- Add access token to request kwargs [\#20](https://github.com/browniebroke/deezer-python/pull/20) ([sheregeda](https://github.com/sheregeda))

### 📖 Documentation updates:

- Update README.rst [\#18](https://github.com/browniebroke/deezer-python/pull/18) ([khamaileon](https://github.com/khamaileon))

## [v0.6.0](https://github.com/browniebroke/deezer-python/tree/0.6.0) (2016-12-27)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.5.0...0.6.0)

### 🚀 Enhancements:

- Refactoring: replace urlopen by requests [\#16](https://github.com/browniebroke/deezer-python/pull/16) ([browniebroke](https://github.com/browniebroke))

## [v0.5.0](https://github.com/browniebroke/deezer-python/tree/0.5.0) (2016-12-26)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.4.0...0.5.0)

### 📖 Documentation updates:

- Docs enhancements [\#13](https://github.com/browniebroke/deezer-python/pull/13) ([browniebroke](https://github.com/browniebroke))

### ✅ Testing:

- Run Flake8 on Travis [\#14](https://github.com/browniebroke/deezer-python/pull/14) ([browniebroke](https://github.com/browniebroke))
- Use tox-travis to integrate environments better [\#12](https://github.com/browniebroke/deezer-python/pull/12) ([browniebroke](https://github.com/browniebroke))

## [v0.4.0](https://github.com/browniebroke/deezer-python/tree/0.4.0) (2016-12-08)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.3.0...0.4.0)

### 🚀 Enhancements:

- Improve chart integration [\#11](https://github.com/browniebroke/deezer-python/pull/11) ([pfouque](https://github.com/pfouque))
- Add pypy to the build matrix [\#10](https://github.com/browniebroke/deezer-python/pull/10) ([browniebroke](https://github.com/browniebroke))
- Implement chart methods [\#8](https://github.com/browniebroke/deezer-python/pull/8) ([pfouque](https://github.com/pfouque))

### ✅ Testing:

- Switch from coveralls to codecov [\#9](https://github.com/browniebroke/deezer-python/pull/9) ([browniebroke](https://github.com/browniebroke))
- Correct a couple of flake8 warning [\#7](https://github.com/browniebroke/deezer-python/pull/7) ([browniebroke](https://github.com/browniebroke))
- Add basic flake8 config to setup.cfg [\#6](https://github.com/browniebroke/deezer-python/pull/6) ([browniebroke](https://github.com/browniebroke))

## [v0.3.0](https://github.com/browniebroke/deezer-python/tree/0.3.0) (2016-11-09)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.2.3...0.3.0)

### 🚀 Enhancements:

- add resource parameters and iterators [\#5](https://github.com/browniebroke/deezer-python/pull/5) ([pfouque](https://github.com/pfouque))
- Async client for Tornado, search [\#1](https://github.com/browniebroke/deezer-python/pull/1) ([misuzu](https://github.com/misuzu))

## [v0.2.1](https://github.com/browniebroke/deezer-python/tree/0.2.1) (2015-09-14)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.2...0.2.1)

### 🚀 Enhancements:

- Run tests against Python 3.5 [\#3](https://github.com/browniebroke/deezer-python/pull/3) ([browniebroke](https://github.com/browniebroke))

## [v0.2](https://github.com/browniebroke/deezer-python/tree/0.2) (2015-01-31)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/0.1...0.2)

### 🚀 Enhancements:

- Methods for resources [\#2](https://github.com/browniebroke/deezer-python/pull/2) ([misuzu](https://github.com/misuzu))

## [v0.1](https://github.com/browniebroke/deezer-python/tree/0.1) (2014-11-23)

[Full Changelog](https://github.com/browniebroke/deezer-python/compare/e87692f7aeb80bc0ed858ccdf6165f0ac8f9c2ec...0.1)

\* _This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)_
