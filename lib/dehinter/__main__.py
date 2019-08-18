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

from fontTools.ttLib import TTFont

from dehinter import __version__
from dehinter.font import is_truetype_font
from dehinter.font import has_cvt_table, has_fpgm_table, has_prep_table
from dehinter.font import remove_cvt, remove_fpgm, remove_prep, remove_glyf_instructions
from dehinter.paths import filepath_exists


def main():

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

    # Execution
    # ---------
    #  (1) Unnecessary OpenType table removal
    try:
        tt = TTFont(args.INFILE)
    except Exception as e:
        sys.stderr.write("[!] Error: Unable to create font object with '{}' -> {}".format(args.INFILE, str(e)))
        sys.exit(1)

    if has_cvt_table(tt):
        remove_cvt(tt)
        if not has_cvt_table(tt):
            print("[-] Removed cvt table")
        else:
            sys.stderr.write("[!] Error: failed to remove cvt table from font")

    if has_fpgm_table(tt):
        remove_fpgm(tt)
        if not has_fpgm_table(tt):
            print("[-] Removed fpgm table")
        else:
            sys.stderr.write("[!] Error: failed to remove fpgm table from font")

    if has_prep_table(tt):
        remove_prep(tt)
        if not has_prep_table(tt):
            print("[-] Removed prep table")
        else:
            sys.stderr.write("[!] Error: failed to remove prep table from font")

    #  (2) Remove glyf table instruction set bytecode
    number_glyfs_edited = remove_glyf_instructions(tt)
    if number_glyfs_edited > 0:
        print("[-] Removed glyf table instruction bytecode from {} glyphs".format(number_glyfs_edited))


if __name__ == "__main__":
    sys.exit(main())
