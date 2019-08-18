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


# ========================================================
# Utilities
# ========================================================
def has_cvt_table(tt):
    """Tests for the presence of a cvt table in a TrueType font."""
    return "cvt " in tt


def has_fpgm_table(tt):
    """Tests for the presence of a fpgm table in a TrueType font."""
    return "fpgm" in tt


def has_prep_table(tt):
    """Tests for the presence of a prep table in a TrueType font."""
    return "prep" in tt


def is_truetype_font(filepath):
    """Tests that a font has the TrueType file signature of either:
         1) b'\x00\x01\x00\x00'
         2) b'\x74\x72\x75\x65' == 'true'"""
    with open(filepath, 'rb') as f:
        file_signature = f.read(4)

        return file_signature in (b'\x00\x01\x00\x00', b'\x74\x72\x75\x65')


# ========================================================
# OpenType table removal
# ========================================================
def remove_cvt(tt):
    """Removes cvt table from a fontTools.ttLib.TTFont object"""
    try:
        del tt["cvt "]
    except KeyError:
        # return unmodified font if table is not present in the font
        pass


def remove_fpgm(tt):
    """Removes fpgm table from a fontTools.ttLib.TTFont object"""
    try:
        del tt["fpgm"]
    except KeyError:
        # return unmodified font if table is not present in the font
        pass


def remove_prep(tt):
    """Removes prep table from a fontTools.ttLib.TTFont object"""
    try:
        del tt["prep"]
    except KeyError:
        # return unmodified font if table is not present in the font
        pass


# ========================================================
# glyf table instruction set bytecode removal
# ========================================================
def remove_glyf_instructions(tt):
    glyph_number = 0
    for glyph in tt['glyf'].glyphs.values():
        glyph.expand(tt['glyf'])
        if hasattr(glyph, "program"):
            glyph.program.bytecode = array.array("B", [])
            glyph_number += 1
    return glyph_number
