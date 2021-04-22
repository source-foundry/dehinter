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
import pprint
import sys
from typing import List

from fontTools.ttLib import TTFont  # type: ignore

from dehinter import __version__
from dehinter.font import (
    has_cvar_table,
    has_cvt_table,
    has_fpgm_table,
    has_hdmx_table,
    has_ltsh_table,
    has_prep_table,
    has_ttfa_table,
    has_vdmx_table,
    is_truetype_font,
    is_variable_font,
    remove_cvar_table,
    remove_cvt_table,
    remove_fpgm_table,
    remove_glyf_instructions,
    remove_hdmx_table,
    remove_ltsh_table,
    remove_prep_table,
    remove_ttfa_table,
    remove_vdmx_table,
    update_gasp_table,
    update_head_table_flags,
    update_maxp_table,
)
from dehinter.paths import filepath_exists, get_default_out_path
from dehinter.system import get_filesize


def main() -> None:  # pragma: no cover
    run(sys.argv[1:])


def run(argv: List[str]) -> None:
    # instantiate pretty printer
    pp = pprint.PrettyPrinter(indent=4)

    # ===========================================================
    # argparse command line argument definitions
    # ===========================================================
    parser = argparse.ArgumentParser(
        description="A tool for the removal of TrueType instruction sets (hints) in fonts"
    )
    parser.add_argument(
        "--version", action="version", version="dehinter v{}".format(__version__)
    )
    parser.add_argument("-o", "--out", help="out file path (dehinted font)")
    parser.add_argument("--keep-cvar", help="keep cvar table", action="store_true")
    parser.add_argument("--keep-cvt", help="keep cvt table", action="store_true")
    parser.add_argument("--keep-fpgm", help="keep fpgm table", action="store_true")
    parser.add_argument("--keep-hdmx", help="keep hdmx table", action="store_true")
    parser.add_argument("--keep-ltsh", help="keep LTSH table", action="store_true")
    parser.add_argument("--keep-prep", help="keep prep table", action="store_true")
    parser.add_argument("--keep-ttfa", help="keep TTFA table", action="store_true")
    parser.add_argument("--keep-vdmx", help="keep VDMX table", action="store_true")
    parser.add_argument(
        "--keep-glyf", help="do not modify glyf table", action="store_true"
    )
    parser.add_argument(
        "--keep-gasp", help="do not modify gasp table", action="store_true"
    )
    parser.add_argument(
        "--keep-maxp", help="do not modify maxp table", action="store_true"
    )
    parser.add_argument(
        "--keep-head", help="do not modify head table", action="store_true"
    )
    parser.add_argument("INFILE", help="in file path (hinted font)")

    args = parser.parse_args(argv)

    # ===========================================================
    # Command line logic
    # ===========================================================
    #
    # Validations
    # -----------
    #  (1) file path request is a file
    if not filepath_exists(args.INFILE):
        sys.stderr.write(
            f"[!] Error: '{args.INFILE}' is not a valid file path.{os.linesep}"
        )
        sys.stderr.write(f"[!] Request canceled.{os.linesep}")
        sys.exit(1)
    #  (2) the file is a ttf font file (based on the 4 byte file signature
    if not is_truetype_font(args.INFILE):
        sys.stderr.write(
            f"[!] Error: '{args.INFILE}' does not appear to be a TrueType font "
            f"file.{os.linesep}"
        )
        sys.stderr.write(f"[!] Request canceled.{os.linesep}")
        sys.exit(1)
    #   (3) confirm that out path is not the same as in path
    #    This tool does not support writing dehinted files in place over hinted version
    if args.INFILE == args.out:
        sys.stderr.write(
            f"[!] Error: You are attempting to overwrite the hinted file with the "
            f"dehinted file.  This is not supported. Please choose a different file "
            f"path for the dehinted file.{os.linesep}"
        )
        sys.exit(1)
    # Execution
    # ---------
    #  (1) OpenType table removal
    try:
        tt = TTFont(args.INFILE)
    except Exception as e:
        sys.stderr.write(
            f"[!] Error: Unable to create font object with '{args.INFILE}' -> {str(e)}"
        )
        sys.exit(1)

    if is_variable_font(tt) and not args.keep_cvar:
        if has_cvar_table(tt):
            remove_cvar_table(tt)
            if not has_cvar_table(tt):
                print("[-] Removed cvar table")
            else:  # pragma: no cover
                sys.stderr.write(
                    f"[!] Error: failed to remove cvar table from font{os.linesep}"
                )

    if not args.keep_cvt:
        if has_cvt_table(tt):
            remove_cvt_table(tt)
            if not has_cvt_table(tt):
                print("[-] Removed cvt table")
            else:  # pragma: no cover
                sys.stderr.write(
                    f"[!] Error: failed to remove cvt table from font{os.linesep}"
                )

    if not args.keep_fpgm:
        if has_fpgm_table(tt):
            remove_fpgm_table(tt)
            if not has_fpgm_table(tt):
                print("[-] Removed fpgm table")
            else:  # pragma: no cover
                sys.stderr.write(
                    f"[!] Error: failed to remove fpgm table from font{os.linesep}"
                )

    if not args.keep_hdmx:
        if has_hdmx_table(tt):
            remove_hdmx_table(tt)
            if not has_hdmx_table(tt):
                print("[-] Removed hdmx table")
            else:  # pragma: no cover
                sys.stderr.write(
                    f"[!] Error: failed to remove hdmx table from font{os.linesep}"
                )

    if not args.keep_ltsh:
        if has_ltsh_table(tt):
            remove_ltsh_table(tt)
            if not has_ltsh_table(tt):
                print("[-] Removed LTSH table")
            else:  # pragma: no cover
                sys.stderr.write(
                    f"[!] Error: failed to remove LTSH table from font{os.linesep}"
                )

    if not args.keep_prep:
        if has_prep_table(tt):
            remove_prep_table(tt)
            if not has_prep_table(tt):
                print("[-] Removed prep table")
            else:  # pragma: no cover
                sys.stderr.write(
                    f"[!] Error: failed to remove prep table from font{os.linesep}"
                )

    if not args.keep_ttfa:
        if has_ttfa_table(tt):
            remove_ttfa_table(tt)
            if not has_ttfa_table(tt):
                print("[-] Removed TTFA table")
            else:  # pragma: no cover
                sys.stderr.write(
                    f"[!] Error: failed to remove TTFA table from font{os.linesep}"
                )

    if not args.keep_vdmx:
        if has_vdmx_table(tt):
            remove_vdmx_table(tt)
            if not has_vdmx_table(tt):
                print("[-] Removed VDMX table")
            else:  # pragma: no cover
                sys.stderr.write(
                    f"[!] Error: failed to remove VDMX table from font{os.linesep}"
                )

    #  (2) Remove glyf table instruction set bytecode
    if not args.keep_glyf:
        number_glyfs_edited = remove_glyf_instructions(tt)
        if number_glyfs_edited > 0:
            print(
                f"[-] Removed glyf table instruction bytecode from "
                f"{number_glyfs_edited} glyphs"
            )

    #  (3) Edit gasp table
    if not args.keep_gasp:
        if update_gasp_table(tt):
            gasp_string = pp.pformat(tt["gasp"].__dict__)
            print(f"[Δ] New gasp table values:{os.linesep}    {gasp_string}")

    #  (4) Edit maxp table
    if not args.keep_maxp:
        if update_maxp_table(tt):
            maxp_string = pp.pformat(tt["maxp"].__dict__)
            print(f"[Δ] New maxp table values:{os.linesep}    {maxp_string}")

    #  (5) Edit head table flags to clear bit 4
    if not args.keep_head:
        if update_head_table_flags(tt):
            print("[Δ] Cleared bit 4 in head table flags")

    # File write
    # ----------
    if args.out:
        # validation performed above to prevent this file path definition from
        # being the same as the in file path.  Write in place over a hinted
        # file is not supported
        outpath = args.out
    else:
        outpath = get_default_out_path(args.INFILE)

    try:
        tt.save(outpath)
        print(f"{os.linesep}[+] Saved dehinted font as '{outpath}'")
    except Exception as e:  # pragma: no cover
        sys.stderr.write(
            f"[!] Error: Unable to save dehinted font file: {str(e)}{os.linesep}"
        )

    # File size comparison
    # --------------------
    infile_size_tuple = get_filesize(args.INFILE)
    outfile_size_tuple = get_filesize(
        outpath
    )  # depends on outpath definition defined during file write
    print(f"{os.linesep}[*] File sizes:")
    print(f"    {infile_size_tuple[0]}{infile_size_tuple[1]} (hinted)")
    print(f"    {outfile_size_tuple[0]}{outfile_size_tuple[1]} (dehinted)")
