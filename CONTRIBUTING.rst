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
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `deezer-python` for local development.

1. Fork the `deezer-python` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/deezer-python.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper
   installed, this is how you set up your fork for local development::

    $ mkvirtualenv deezer-python
    $ cd deezer-python/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass `flake8`_ and the
   tests, including testing other Python versions with `tox`_::

        $ flake8
        $ tox

   To get `flake8`_ and `tox`_, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for Python 2.7, 3.3, 3.4, 3.5 and for PyPy. Check
   `Travis`_ and make sure that the tests pass for all supported Python versions.

Create a New Release
--------------------

This project is configured to use `bumpversion
<https://github.com/peritus/bumpversion>`_, only prerequisite
is to have it installed. When the tests have passed and you're happy with the code base, just need to run::

  $ bumpversion [major|minor|patch]

Depending on which digit of the version needs to be updated, and then push with tags::

  $ git push --tags

`Travis`_ will take care of creating the release, and upload it to PyPI.

.. _issues page: https://github.com/browniebroke/deezer-python/issues
.. _Travis: https://travis-ci.org/browniebroke/deezer-python/pull_requests
.. _tox: http://tox.readthedocs.io/en/stable/index.html
.. _flake8: http://flake8.pycqa.org/en/latest/
