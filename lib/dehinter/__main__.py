# Copyright 2019 Source Foundry Authors and Contributors

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import os
import sys

from dehinter import __version__
from dehinter.font import is_truetype_font
from dehinter.paths import filepath_exists

import fontTools


def main():
    argv = sys.argv

    # ===========================================================
    # argparse command line argument definitions
    # ===========================================================
    # TODO: add support for options to keep cvt, prep, and fpgm tables
    parser = argparse.ArgumentParser(description="A tool for the removal of TrueType instruction sets (hints) in fonts")
    parser.add_argument("--version", action="version",
                        version="dehinter v{}".format(__version__))
    parser.add_argument("-o", "--out", help="out file path (dehinted font)")
    parser.add_argument("INFILE", help="in file path (hinted font)")

    args = parser.parse_args()

    # ===========================================================
    # Command line logic
    # ===========================================================
    #
    # Validations
    # -----------
    #  (1) file path request is a file
    if not filepath_exists(args.INFILE):
        sys.stderr.write("[!] Error: '{}' is not a valid file path.{}".format(args.INFILE, os.linesep))
        sys.stderr.write("[!] Request canceled.{}".format(os.linesep))
        sys.exit(1)
    #  (2) the file is a ttf font file (based on the 4 byte file signature
    if not is_truetype_font(args.INFILE):
        sys.stderr.write("[!] Error: '{}' does not appear to be a TrueType font file.{}".format(args.INFILE, os.linesep))
        sys.stderr.write("[!] Request canceled.{}".format(os.linesep))
        sys.exit(1)




if __name__ == "__main__":
    sys.exit(main())
