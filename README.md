# Flake8 SARIF formatting plugin

> ℹ️ This is an _unofficial_ tool created by Field Security Services, and is not officially supported by GitHub.

This is a plugin for [Flake8](https://flake8.pycqa.org/en/latest/) (a Python linter) that formats the output as [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html).

## Installation

### From PyPi

Install it with pip [from PyPi](https://pypi.org/project/flake8-sarif-formatter/):

```bash
python3 -mpip install flake8-sarif-formatter
```

### From the GitHub repository

Clone the [GitHub repository](https://github.com/advanced-security/flake8-sarif-formatter) and install it with pip:

```bash
python3 -mpip . install
```

OR

Install straight from the GitHub repository:

```bash
python3 -mpip install pip --upgrade # make sure pip is sufficiently up-to-date for the #egg= fragment
python3 -mpip install git+https://github.com/advanced-security/flake8-sarif-formatter.git#egg=flake8-sarif-formatter
```

## Usage

Use it in Flake8 by referencing the plugin name `sarif` in your Flake8 configuration file on a single line, as:

```ini
format=sarif
```

or at the CLI with:

```bash
flake8 --format=sarif
```

## License

This project is licensed under the terms of the MIT open source license. Please refer to the [LICENSE](LICENSE) for the full terms.

## Maintainers

See [CODEOWNERS](CODEOWNERS) for the list of maintainers.

## Support

> ℹ️ This is an _unofficial_ tool created by Field Security Services, and is not officially supported by GitHub.

See the [SUPPORT](SUPPORT.md) file.

## Background

See the [CHANGELOG](CHANGELOG.md), [CONTRIBUTING](CONTRIBUTING.md), [SECURITY](SECURITY.md), [SUPPORT](SUPPORT.md), [CODE OF CONDUCT](CODE_OF_CONDUCT.md) and [PRIVACY](PRIVACY.md) files for more information.
