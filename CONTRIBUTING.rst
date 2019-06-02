============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs on the `issues page`_. If you are reporting a bug, please include:

* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

This module could always use more documentation, whether as part of the
official docs, in docstrings, or other.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an ticket on the `issues page`_. If you
are proposing a feature:

* Explain how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome 🙂

Get Started!
------------

Ready to contribute? Here's how to set up ``deezer-python`` for local development.

1. Fork the repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/deezer-python.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper
   installed, this is how you set up your fork for local development::

    $ mkvirtualenv deezer-python
    $ cd deezer-python/

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass our
   tests and that the doc builds. The easiest way to do that is by running
   `tox`_ environments::

        $ tox -e lint,docs,py36

   It will run our linters (`flake8`_ and `black`_), build the docs and run the tests

6. Commit your changes, quoting GitHub issue in the commit message, if applicable,
   and push your branch to GitHub::

    $ git add .
    $ git commit -m "Fix #XX - My awesome fix"
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request on GitHub.

Pull Request Guidelines
-----------------------

Feel free to open the pull request as soon as possible, but please be explicit
if it's still a work in progress. To be mergeable, pull requests should follow the
following guidelines:

1. It should include tests for feature or bug fixes.
2. If it adds functionality, the docs should be updated.
3. It should work for Python 3.5, 3.6, 3.7 and for PyPy3.
   Check `Travis`_ as well as `AppVeyor`_ and make sure that the tests
   pass for all supported Python versions.
4. If your change is worthwhile a mention in the changelog, update the
   Unreleased section of ``HISTORY.rst``.

Create a New Release
--------------------

This project is configured to use `bumpversion`_, only prerequisite
is to have it installed. When the tests have passed and you're happy with the code base,
you can bump the version everywhere needed, commit and create a git tag by running::

  $ bumpversion [major|minor|patch]

Then, do a git push, without forgetting about git tags::

  $ git push --tags

`Travis`_ will take care of creating the release, and upload it to PyPI.

.. _issues page: https://github.com/browniebroke/deezer-python/issues
.. _Travis: https://travis-ci.org/browniebroke/deezer-python/pull_requests
.. _AppVeyor: https://ci.appveyor.com/project/browniebroke/deezer-python
.. _tox: http://tox.readthedocs.io/en/stable/index.html
.. _flake8: http://flake8.pycqa.org/en/latest/
.. _black: https://github.com/ambv/black
.. _bumpversion: https://github.com/peritus/bumpversion
