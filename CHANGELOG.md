# Changelog

## v3.0.0

- add support for cvar table removal in variable fonts (backward incompatible change)
- add new `--keep-cvar` option to toggle cvar table removal off
- modify default gasp approach to add a gasp table when it is not available in a font (backward incompatible change)
- add new source formatting Makefile targets
- add isort package to setup.py extras_requires dev dependencies
- source import statement formatting
- update fonttools dependency to v4.22.0
- update GitHub Actions workflows to use cPython 3.9 (from cPython 3.8)

## v2.0.4

- dependency update patch
- update fonttools dependency to v4.17.1

## v2.0.3

- add cPython 3.9 interpreter testing
- add CodeQL static source testing
- update fonttools dependency to v4.16.1

## v2.0.2

- refactor string formatting to f-strings
- added GitHub Action CI workflows
- removed Travis CI testing
- removed Appveyor CI testing

## v2.0.1

- update setup.py classifiers to properly define this project as status 5: Production / Stable
- update README.md with transition to `mypy` as our static type check tool

## v2.0.0

Backwards incompatible gasp table change introduced in this release

- modified dehinted gasp table definition to grayscale, symmetric smoothing behavior (bit flag 0x000A).  The previous default was bit flag 0x000f which defines gridfit, grayscale, symmetric gridfit, symmetric smoothing.  Our previous default is the *default* behavior in `ttfautohint -d` to our knowledge.  This change is a departure from the `ttfautohint -d` default behavior. (pull request #39, thanks Aaron!)
- added type hints and mypy static type checking
- updated fontTools dependency to v4.14.0
- black source formatting applied to Python sources

## v1.0.0

- updated fontTools and associated dependencies to v4.6.0 release
- this update adds Unicode 13 support
- add Python3.8 CI testing support

## v0.4.3

- escalated fontTools dependency version to v4.2.4

## v0.4.2

- fix Travis CI testing error on macOS platform with move to `pip3` from `pip`
- update fontTools dependency to v4.0.1

## v0.4.1

- fix Makefile uninstall target error
- PEP8 source formatting edits

## v0.4.0

- changed min Python version to Python 3.6+ interpreters
- added support for default VDMX table removal
- added `--keep-vdmx` option to keep original VDMX table
- updated fontTools dependency to v4.0.0
- changed configuration to build wheels for Py3 only
- setup.py file updated with new classifiers
- added new Ubuntu-Regular.ttf testing file with the UFL license
- added the Roboto testing file license

## v0.3.0

- modified `glyf` table instruction set bytecode removal approach for composite glyphs
- fixed: `head` table flags bit 4 is now cleared only when `hdmx` and `LTSH` tables are removed (or were not present and bit is set in the font)

## v0.2.0

- add `--keep-cvt` option to keep original cvt table
- add `--keep-fpgm` option to keep original fpgm table
- add `--keep-gasp` option to keep original gasp table
- add `--keep-glyf` option to keep original glyf table
- add `--keep-hdmx` option to keep original hdmx table
- add `--keep-head` option to keep original head table
- add `--keep-ltsh` option to keep original LTSH table
- add `--keep-maxp` option to keep original maxp table
- add `--keep-prep` option to keep original prep table
- add `--keep-ttfa` option to keep original TTFA table

## v0.1.0

- initial beta release

## v0.0.1

- pre-release for PyPI naming
