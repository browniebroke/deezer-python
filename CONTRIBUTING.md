# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs on the [issues
page](https://github.com/browniebroke/deezer-python/issues). If you are
reporting a bug, please include:

-   Any details about your local setup that might be helpful in
    troubleshooting.
-   Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" is
open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
"feature" is open to whoever wants to implement it.

### Write Documentation

This module could always use more documentation, whether as part of the
official docs, in docstrings, or other.

### Submit Feedback

The best way to send feedback is to file an ticket on the [issues
page](https://github.com/browniebroke/deezer-python/issues). If you are
proposing a feature:

-   Explain how it would work.
-   Keep the scope as narrow as possible, to make it easier to
    implement.
-   Remember that this is a volunteer-driven project, and that
    contributions are welcome 🙂

## Get Started!

Ready to contribute? Here's how to set up `deezer-python` for local
development.

1.  Fork the repo on GitHub.

2.  Clone your fork locally:

        $ git clone git@github.com:your_name_here/deezer-python.git

3.  Install your local copy into a virtualenv. Assuming you have
    virtualenvwrapper installed, this is how you set up your fork for
    local development:

        $ mkvirtualenv deezer-python
        $ cd deezer-python/

4.  Create a branch for local development:

        $ git checkout -b name-of-your-bugfix-or-feature

    Now you can make your changes locally.

5.  When you're done making changes, check that your changes pass our
    tests and that the doc builds. The easiest way to do that is by
    running [tox](http://tox.readthedocs.io/en/stable/index.html)
    environments:

        $ tox -e lint,docs,py38

    It will run our linters
    ([flake8](http://flake8.pycqa.org/en/latest/) and
    [black](https://github.com/ambv/black)), build the docs and run the
    tests

6.  Commit your changes, quoting GitHub issue in the commit message, if
    applicable, and push your branch to GitHub:

        $ git add .
        $ git commit -m "feat(something): your detailed description of your changes"
        $ git push origin name-of-your-bugfix-or-feature
    
    Note: the commit message should follow [the conventional commits guidelines][1],
    this is to enable the automation of releases. We run [`commitlint` on CI][2] 
    which will validate the commit messages.

7.  Submit a pull request on GitHub.

[1]: https://www.conventionalcommits.org
[2]: https://github.com/marketplace/actions/commit-linter

## Pull Request Guidelines

Feel free to open the pull request as soon as possible, but please be
explicit if it's still a work in progress, we recommend draft pull
requests. Please try to:

1.  Include tests for feature or bug fixes.
2.  Update the documentation if for any significant API changes.
3.  Ensure tests are passing on continuous integration.

## Create a New Release

The deployment should be automated and can be triggered from the Semantic Release 
workflow in Github. The next version will be based on [the commit logs][3]. 
This is done by [python-semantic-release][4] via a Github action.

[3]: https://python-semantic-release.readthedocs.io/en/latest/commit-log-parsing.html#commit-log-parsing
[4]: https://python-semantic-release.readthedocs.io/en/latest/index.html
