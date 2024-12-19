# Contributing

Contributions are welcome, and they are greatly appreciated! Every little helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs on [our issues page][gh-issues]. If you are reporting a bug, please include:

- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" is open to whoever wants to implement it.

### Write Documentation

This module could always use more documentation, whether as part of the official docs, in docstrings, or other.

### Submit Feedback

The best way to send feedback is to file a ticket on [our issues page][gh-issues]. If you are proposing a feature:

- Explain how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are welcome 🙂

## Get Started!

Ready to contribute? Here's how to set up `deezer-python` for local development.

1. Fork the repo on GitHub.

2. Clone your fork locally:

   ```shell
   $ git clone git@github.com:your_name_here/deezer-python.git
   ```

3. Install the dependencies with [uv](https://docs.astral.sh/uv/)

   ```shell
   $ uv sync -E docs
   ```

4. Create a branch for local development:

   ```shell
   $ git checkout -b name-of-your-bugfix-or-feature
   ```

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass our tests:

   ```shell
   $ uv run pytest
   ```

6. Linting is done through [pre-commit](https://pre-commit.com). Provided you have the tool installed globally, you can run them all as one-off:

   ```shell
   $ pre-commit run -a
   ```

   Or better, install the hooks once and have them run automatically each time you commit:

   ```shell
   $ pre-commit install
   ```

7. Commit your changes, quoting GitHub issue in the commit message, if applicable, and push your branch to GitHub:

   ```shell
   $ git add .
   $ git commit -m "feat(something): your detailed description of your changes"
   $ git push origin name-of-your-bugfix-or-feature
   ```

   Note: the commit message should follow [the conventional commits](https://www.conventionalcommits.org). We run [`commitlint` on CI](https://github.com/marketplace/actions/commit-linter) to validate it, and if you've installed pre-commit hooks at the previous step, the message will be checked at commit time.

8. Submit a pull request on GitHub.

## Obtain an API token

If you want to work on a feature that requires authentication, you'll need to obtain an API token to perform authenticated requests. You can do so using the [`deezer-oauth-cli`](https://pypi.org/project/deezer-oauth-cli/) package. It's a development dependency, so if you ran `uv sync`, you should already have it.

You'll need to have a dedicated app in the [Deezer developer portal](https://developers.deezer.com/myapps), create one with the following redirect URL after authentication: `http://localhost:8080/oauth/return`. Once created, grab the application ID and the secret key and call the CLI tool with them:

```shell
$ deezer-oauth APP_ID SECRET_KEY
```

Authorise the app in your browser. You should then should be redirected to a simple HTML page with your API token. The script also save the API token locally in the `.env` file. This is convenient to generate cassettes when writing new tests locally.

## Pull Request Guidelines

Feel free to open the pull request as soon as possible, but please be explicit if it's still a work in progress, we recommend draft pull requests. Please try to:

1. Include tests for feature or bug fixes.
2. Update the documentation if for any significant API changes.
3. Ensure tests are passing on continuous integration.

## Create a New Release

The deployment should be automated and can be triggered from the Semantic Release workflow in GitHub. The next version will be based on [the commit logs](https://python-semantic-release.readthedocs.io/en/latest/commit-log-parsing.html#commit-log-parsing). This is done by [python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/index.html) via a GitHub action.

[gh-issues]: https://github.com/browniebroke/deezer-python/issues
