<img src="https://github.com/source-foundry/dehinter/raw/img/img/dehinter_logo-crunch.png" width="300" />
<br/>

[![PyPI](https://img.shields.io/pypi/v/dehinter?color=blueviolet&label=PyPI&logo=python&logoColor=white)](https://pypi.org/project/dehinter/)
[![Build Status](https://travis-ci.org/source-foundry/dehinter.svg?branch=master)](https://travis-ci.org/source-foundry/dehinter)
[![Build status](https://ci.appveyor.com/api/projects/status/08uftyy98ni837ak?svg=true)](https://ci.appveyor.com/project/chrissimpkins/dehinter)
[![codecov](https://codecov.io/gh/source-foundry/dehinter/branch/master/graph/badge.svg)](https://codecov.io/gh/source-foundry/dehinter)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a2f54fac2c544f389e0066cfa159dfe8)](https://www.codacy.com/app/SourceFoundry/dehinter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=source-foundry/dehinter&amp;utm_campaign=Badge_Grade)

## About

`dehinter` is a Python command line application that removes TrueType instruction sets, global hinting tables, and other associated OpenType table data in font files.  The tool provides cross-platform support on macOS, Windows, and Linux systems with a Python v3.6+ interpreter.

## What it does

- Removes OpenType [glyf table](https://docs.microsoft.com/en-us/typography/opentype/spec/glyf) instruction set bytecode data
- Removes OpenType and other TTF hinting related tables
	- [cvt table](https://docs.microsoft.com/en-us/typography/opentype/spec/cvt)
	- [fpgm table](https://docs.microsoft.com/en-us/typography/opentype/spec/fpgm)
	- [hdmx table](https://docs.microsoft.com/en-us/typography/opentype/spec/hdmx)
	- [LTSH table](https://docs.microsoft.com/en-us/typography/opentype/spec/ltsh)
	- [prep table](https://docs.microsoft.com/en-us/typography/opentype/spec/prep)
	- [TTFA table](https://www.freetype.org/ttfautohint/doc/ttfautohint.html#add-ttfa-info-table) (not part of the OpenType specification)
	- [VDMX table](https://docs.microsoft.com/en-us/typography/opentype/spec/vdmx)
- Updates [gasp table](https://docs.microsoft.com/en-us/typography/opentype/spec/gasp) values
- Updates [maxp table](https://docs.microsoft.com/en-us/typography/opentype/spec/maxp) values
- Updates [head table](https://docs.microsoft.com/en-us/typography/opentype/spec/head) bit flags
- Displays file sizes of the hinted and dehinted versions of the fonts

Options allow you to maintain the original version of any of these tables.

## Installation

`dehinter` requires a Python 3.6+ interpreter.

Installation in a [Python3 virtual environment](https://docs.python.org/3/library/venv.html) is recommended as dependencies are pinned to versions that are confirmed to work with this project.

Use any of the following installation approaches:

### pip install from PyPI

```
$ pip3 install dehinter
```

### pip install from source

```
$ git clone https://github.com/source-foundry/dehinter.git
$ cd dehinter
$ pip3 install .
```

### Developer install from source

The following approach installs the project and associated optional developer dependencies so that source changes are available without the need for re-installation.

```
$ git clone https://github.com/source-foundry/dehinter.git
$ cd dehinter
$ pip3 install --ignore-installed -r requirements.txt -e ".[dev]"
```

## Usage

```
$ dehinter [OPTIONS] [HINTED FILE PATH]
```

By default, a new dehinted font build write occurs on the path `[ORIGINAL HINTED FONT NAME]-dehinted.ttf` in the `[HINTED FILE PATH]` directory.

Use `dehinter -h` to view available options.

## Issues

Please report issues on the [project issue tracker](https://github.com/source-foundry/dehinter/issues).

## Contributing

Contributions are warmly welcomed.  A development dependency environment can be installed in editable mode with the developer installation documentation above. 

Please use the standard Github pull request approach to propose source changes.

### Source file linting

Python source files are linted with `flake8`.  See the Makefile `test-lint` target for details.

### Source file static type checks

Static type checks are performed on Python source files with `pytype`.  See the Makefile `test-type-check` target for details.

### Testing

The project runs continuous integration testing on [Travis CI](https://travis-ci.org/source-foundry/dehinter) and [Appveyor CI](https://ci.appveyor.com/project/chrissimpkins/dehinter) with the `pytest` and `tox` testing toolchain.  Test modules are located in the `tests` directory of the repository.

Local testing by Python interpreter version can be performed with the following command executed from the root of the repository:

```
$ tox -e [PYTHON INTERPRETER VERSION]
```

Please see the `tox` documentation for additional details.

### Test coverage

Unit test coverage is executed with the `coverage` tool.  See the Makefile `test-coverage` target for details.

## Acknowledgments

`dehinter` is built with the fantastic [fontTools free software library](https://github.com/fonttools/fonttools) and is based on the dehinting approach used in the [`ttfautohint` free software project](https://www.freetype.org/ttfautohint/).

## License

   Copyright 2019 Source Foundry Authors and Contributors

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.