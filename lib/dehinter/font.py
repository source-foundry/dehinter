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

import array
import os
from typing import Union

from fontTools import ttLib  # type: ignore

from dehinter.bitops import clear_bit_k, is_bit_k_set


# ========================================================
# Utilities
# ========================================================
def has_cvar_table(tt) -> bool:
    """Tests for the presence of a cvat table in a TrueType variable font."""
    return "cvar" in tt


def has_cvt_table(tt) -> bool:
    """Tests for the presence of a cvt table in a TrueType font."""
    return "cvt " in tt


def has_fpgm_table(tt) -> bool:
    """Tests for the presence of a fpgm table in a TrueType font."""
    return "fpgm" in tt


def has_gasp_table(tt) -> bool:
    """Tests for the presence of a gasp table in a TrueType font."""
    return "gasp" in tt


def has_hdmx_table(tt) -> bool:
    """Tests for the presence of a hdmx table in a TrueType font."""
    return "hdmx" in tt


def has_ltsh_table(tt) -> bool:
    """Tests for the presence of a LTSH table in a TrueType font."""
    return "LTSH" in tt


def has_prep_table(tt) -> bool:
    """Tests for the presence of a prep table in a TrueType font."""
    return "prep" in tt


def has_ttfa_table(tt) -> bool:
    """Tests for the presence of a TTFA table in a TrueType font."""
    return "TTFA" in tt


def has_vdmx_table(tt) -> bool:
    """Tests for the presence of a VDMX table in a TrueType font."""
    return "VDMX" in tt


def is_truetype_font(filepath: Union[bytes, str, "os.PathLike[str]"]) -> bool:
    """Tests that a font has the TrueType file signature of either:
    1) b'\x00\x01\x00\x00'
    2) b'\x74\x72\x75\x65' == 'true'"""
    with open(filepath, "rb") as f:
        file_signature: bytes = f.read(4)

        return file_signature in (b"\x00\x01\x00\x00", b"\x74\x72\x75\x65")


def is_variable_font(tt) -> bool:
    """Tests for the presence of a fvar table to confirm that a file is
    a variable font."""
    return "fvar" in tt


# ========================================================
# OpenType table removal
# ========================================================
def remove_cvar_table(tt) -> None:
    """Removes cvt table from a fontTools.ttLib.TTFont object"""
    try:
        del tt["cvar"]
    except KeyError:
        # do nothing if table is not present in the font
        pass


def remove_cvt_table(tt) -> None:
    """Removes cvt table from a fontTools.ttLib.TTFont object"""
    try:
        del tt["cvt "]
    except KeyError:
        # do nothing if table is not present in the font
        pass


def remove_fpgm_table(tt) -> None:
    """Removes fpgm table from a fontTools.ttLib.TTFont object"""
    try:
        del tt["fpgm"]
    except KeyError:
        # do nothing if table is not present in the font
        pass


def remove_hdmx_table(tt) -> None:
    """Removes hdmx table from a fontTools.ttLib.TTFont object"""
    try:
        del tt["hdmx"]
    except KeyError:
        # do nothing if table is not present in the font
        pass


def remove_ltsh_table(tt) -> None:
    """Removes LTSH table from a fontTools.ttLib.TTFont object."""
    try:
        del tt["LTSH"]
    except KeyError:
        # do nothing if table is not present in the font
        pass


def remove_prep_table(tt) -> None:
    """Removes prep table from a fontTools.ttLib.TTFont object"""
    try:
        del tt["prep"]
    except KeyError:
        # do nothing if table is not present in the font
        pass


def remove_ttfa_table(tt) -> None:
    """Removes TTFA table from a fontTools.ttLib.TTFont object"""
    try:
        del tt["TTFA"]
    except KeyError:
        # do nothing if table is not present in the font
        pass


def remove_vdmx_table(tt) -> None:
    """Removes TTFA table from a fontTools.ttLib.TTFont object"""
    try:
        del tt["VDMX"]
    except KeyError:
        # do nothing if table is not present in the font
        pass


# ========================================================
# glyf table instruction set bytecode removal
# ========================================================
def remove_glyf_instructions(tt) -> int:
    """Removes instruction set bytecode from glyph definitions in the glyf table."""
    glyph_number: int = 0
    for glyph in tt["glyf"].glyphs.values():
        glyph.expand(tt["glyf"])
        if hasattr(glyph, "program") and glyph.program.bytecode != array.array("B", []):
            if glyph.isComposite():
                del glyph.program
                glyph_number += 1
            else:
                glyph.program.bytecode = array.array("B", [])
                glyph_number += 1
    return glyph_number


# ========================================================
# gasp table edit
# ========================================================
def update_gasp_table(tt) -> bool:
    """Modifies the following gasp table fields:
    1) rangeMaxPPEM changed to 65535
    2) rangeGaspBehavior changed to 0x000a (symmetric grayscale, no gridfit)"""
    if "gasp" not in tt:
        tt["gasp"] = ttLib.newTable("gasp")
        tt["gasp"].gaspRange = {}
    if tt["gasp"].gaspRange != {65535: 0x000A}:
        tt["gasp"].gaspRange = {65535: 0x000A}
        return True
    else:
        return False


# =========================================
# maxp table edits
# =========================================
def update_maxp_table(tt) -> bool:
    """Update the maxp table with new values based on elimination of instruction sets."""
    changed: bool = False
    if tt["maxp"].maxZones != 0:
        tt["maxp"].maxZones = 0
        changed = True
    if tt["maxp"].maxTwilightPoints != 0:
        tt["maxp"].maxTwilightPoints = 0
        changed = True
    if tt["maxp"].maxStorage != 0:
        tt["maxp"].maxStorage = 0
        changed = True
    if tt["maxp"].maxFunctionDefs != 0:
        tt["maxp"].maxFunctionDefs = 0
        changed = True
    if tt["maxp"].maxStackElements != 0:
        tt["maxp"].maxStackElements = 0
        changed = True
    if tt["maxp"].maxSizeOfInstructions != 0:
        tt["maxp"].maxSizeOfInstructions = 0
        changed = True
    return changed


# =========================================
# head table edits
# =========================================
def update_head_table_flags(tt) -> bool:
    if is_bit_k_set(tt["head"].flags, 4):
        # confirm that there is no LTSH or hdmx table
        # bit 4 should be set if either of these tables are present in font
        if has_hdmx_table(tt) or has_ltsh_table(tt):
            return False
        else:
            new_flags = clear_bit_k(tt["head"].flags, 4)
            tt["head"].flags = new_flags
            return True
    else:
        return False
