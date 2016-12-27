.. :changelog:

History
=======

Unreleased
----------

0.6.0 (2016-12-27)
------------------

- Refactoring to use `requests`_ instead of urllib, mocking using
  Requests mock instead of manual patching. Use `six`_ for Python
  2 and 3 compatibility.

.. _requests: http://docs.python-requests.org/
.. _six: https://pythonhosted.org/six/

0.5.0 (2016-12-26)
------------------

- Python 3.6 support
- Remove Python 3.2 classifier, support was dropped since 0.2.3
- Updated docs and testing setup

0.4.0 (2016-12-08)
------------------

- Add the `chart`_ resource. Thanks to `Pascal`_.
- Documentation updates regarding changelog and list of authors.

0.3.0 (2016-11-09)
------------------

- Enriching the API for resources to get related resources as iterators.
  Thanks to `Pascal`_.

0.2.3 (2016-11-07)
------------------

- Drop support for Python 3.2. It should still work, but we are not testing
  it anymore, as this version as reached end of life.

0.2.2 (2015-09-14)
------------------

- Python 3.5 support
- Various doc updates

0.2.0 (2015-01-31)
------------------

- Enriching the API for resources to get artists for a genre,
  top tracks of an artist, etc... Thanks to `Misuzu`_.

0.1.0 (2014-11-22)
------------------

- Initial release.

.. _Misuzu: https://github.com/misuzu
.. _Pascal: https://github.com/pfouque
.. _chart: https://developers.deezer.com/api/chart
