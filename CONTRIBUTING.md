# Contributing

## Security

For security issues, see [SECURITY](SECURITY.md).

## Bugs and issues

Please raise non-security bugs and suggestions in the Issues on the GitHub-hosted repository.

## Developing

Please test your changes before submitting a PR.

Run existing tests with:

```bash
pipenv run python3 -munittest discover -s tests -p 'test*.py'
```

Use `pipenv` to maintain dependencies.

Upload new versions to PyPi using the `./release.sh` wrapper script.

This requires you to have a suitable PyPi API token with publish access to `flake8-sarif-formatter` stored in your system keychain.

## Submitting changes

Please fork the repository, and raise a Pull Request (PR) for review.

Remember to update the [README](README.md) and [CHANGELOG](CHANGELOG.md).

Your changes must be acceptable under the [LICENSE](LICENSE.md) of the project.

## Code of conduct

Follow the [Code of Conduct](CODE_OF_CONDUCT.md).
