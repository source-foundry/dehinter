# Changelog

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