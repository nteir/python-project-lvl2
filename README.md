Generate diff
-------------

### Hexlet tests and linter status:
[![Actions Status](https://github.com/nteir/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/nteir/python-project-lvl2/actions)
[![Python package](https://github.com/nteir/python-project-lvl2/actions/workflows/python-package.yml/badge.svg)](https://github.com/nteir/python-project-lvl2/actions/workflows/python-package.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/7b83d284d0163bae3f52/maintainability)](https://codeclimate.com/github/nteir/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/7b83d284d0163bae3f52/test_coverage)](https://codeclimate.com/github/nteir/python-project-lvl2/test_coverage)

Generates difference between 2 JSON or YAML files. Represents the diff in 3 possible formats: stylish, plain, or JSON.

### Installation
Requires Python 3.8 or higher.
Installation via [Poetry](https://python-poetry.org/):
* clone the repository
* change directory to python-project-lvl2
* run the following commands in shell:
```
make install
make build
make package-install
```
Usage: gendiff [-h] [-f FORMAT] first_file second_file

Flat JSON:
[![asciicast](https://asciinema.org/a/WF7NosMdqc3zf3rHebEDy0cBu.svg)](https://asciinema.org/a/WF7NosMdqc3zf3rHebEDy0cBu)

Flat YAML:
[![asciicast](https://asciinema.org/a/Jd74CUaDryvTL3MOrckEkuIzk.svg)](https://asciinema.org/a/Jd74CUaDryvTL3MOrckEkuIzk)

Nested trees:
[![asciicast](https://asciinema.org/a/fDlGcgRnfHSavWIZPBFhogF9T.svg)](https://asciinema.org/a/fDlGcgRnfHSavWIZPBFhogF9T)

Plain format on nested trees:
[![asciicast](https://asciinema.org/a/2L8Kx4gUGfq6mYvLXmkUA9xZH.svg)](https://asciinema.org/a/2L8Kx4gUGfq6mYvLXmkUA9xZH)

JSON dump of nested trees diff:
[![asciicast](https://asciinema.org/a/xQkbEMNZQ52Y4TZmkpvvrgC6V.svg)](https://asciinema.org/a/xQkbEMNZQ52Y4TZmkpvvrgC6V)