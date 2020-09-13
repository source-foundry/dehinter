import os

from dehinter.font import (
    is_truetype_font,
    has_cvt_table,
    has_fpgm_table,
    has_gasp_table,
    has_hdmx_table,
    has_ltsh_table,
    has_prep_table,
    has_ttfa_table,
    has_vdmx_table,
)
from dehinter.font import (
    remove_cvt_table,
    remove_fpgm_table,
    remove_hdmx_table,
    remove_ltsh_table,
    remove_prep_table,
    remove_ttfa_table,
    remove_vdmx_table,
    remove_glyf_instructions,
)
from dehinter.font import update_gasp_table, update_head_table_flags, update_maxp_table

import pytest
from fontTools.ttLib import TTFont

FILEPATH_TEST_TEXT = os.path.join("tests", "test_files", "text", "test.txt")
FILEPATH_HINTED_TTF = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
FILEPATH_DEHINTED_TTF = os.path.join(
    "tests", "test_files", "fonts", "Roboto-Regular-dehinted.ttf"
)
FILEPATH_HINTED_TTF_2 = os.path.join(
    "tests", "test_files", "fonts", "NotoSans-Regular.ttf"
)
FILEPATH_DEHINTED_TTF_2 = os.path.join(
    "tests", "test_files", "fonts", "NotoSans-Regular-dehinted.ttf"
)

FILEPATH_HINTED_TTF_3 = os.path.join(
    "tests", "test_files", "fonts", "Ubuntu-Regular.ttf"
)


# ========================================================
# Utilities
# ========================================================


def test_has_cvt_table_true():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert has_cvt_table(tt) is True


def test_has_cvt_table_false():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert has_cvt_table(tt) is False


def test_has_fpgm_table_true():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert has_fpgm_table(tt) is True


def test_has_fpgm_table_false():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert has_fpgm_table(tt) is False


def test_has_gasp_table_true():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert has_gasp_table(tt) is True


def test_has_hdmx_table_true():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert has_hdmx_table(tt) is True


def test_has_hdmx_table_false():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert has_hdmx_table(tt) is False


def test_has_ltsh_table_true():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert has_ltsh_table(tt) is True


def test_has_ltsh_table_false():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert has_ltsh_table(tt) is False


def test_has_prep_table_true():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert has_prep_table(tt) is True


def test_has_prep_table_false():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert has_prep_table(tt) is False


def test_has_ttfa_table_true():
    tt = TTFont(FILEPATH_HINTED_TTF_2)  # tested in Noto Sans font
    assert has_ttfa_table(tt) is True


def test_has_ttfa_table_false():
    tt = TTFont(FILEPATH_DEHINTED_TTF_2)  # tested in Noto Sans font
    assert has_ttfa_table(tt) is False


def test_has_vdmx_table_true():
    tt = TTFont(FILEPATH_HINTED_TTF_3)
    assert has_vdmx_table(tt) is True


def test_has_vdmx_table_false():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert has_vdmx_table(tt) is False


def test_is_truetype_font_for_ttf():
    assert is_truetype_font(FILEPATH_HINTED_TTF) is True


def test_is_truetype_font_for_not_ttf():
    assert is_truetype_font(FILEPATH_TEST_TEXT) is False


# ========================================================
# OpenType table removal
# ========================================================
def test_delete_cvt_table():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert ("cvt " in tt) is True
    remove_cvt_table(tt)
    assert ("cvt " in tt) is False


def test_delete_cvt_table_missing_table():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert ("cvt " in tt) is False
    remove_cvt_table(tt)
    assert ("cvt " in tt) is False


def test_delete_fpgm_table():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert ("fpgm" in tt) is True
    remove_fpgm_table(tt)
    assert ("fpgm" in tt) is False


def test_delete_fpgm_table_missing_table():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert ("fpgm" in tt) is False
    remove_fpgm_table(tt)
    assert ("fpgm" in tt) is False


def test_delete_hdmx_table():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert ("hdmx" in tt) is True
    remove_hdmx_table(tt)
    assert ("hdmx" in tt) is False


def test_delete_hdmtx_table_missing_table():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert ("hdmx" in tt) is False
    remove_hdmx_table(tt)
    assert ("hdmx" in tt) is False


def test_delete_ltsh_table():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert ("LTSH" in tt) is True
    remove_ltsh_table(tt)
    assert ("LTSH" in tt) is False


def test_delete_ltsh_table_missing_table():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert ("LTSH" in tt) is False
    remove_ltsh_table(tt)
    assert ("LTSH" in tt) is False


def test_delete_prep_table():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert ("prep" in tt) is True
    remove_prep_table(tt)
    assert ("prep" in tt) is False


def test_delete_prep_table_missing_table():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert ("prep" in tt) is False
    remove_prep_table(tt)
    assert ("prep" in tt) is False


def test_delete_ttfa_table():
    tt = TTFont(FILEPATH_HINTED_TTF_2)  # tested in Noto Sans
    assert ("TTFA" in tt) is True
    remove_ttfa_table(tt)
    assert ("TTFA" in tt) is False


def test_delete_ttfa_table_missing_table():
    tt = TTFont(FILEPATH_DEHINTED_TTF_2)  # tested in Noto Sans
    assert ("TTFA" in tt) is False
    remove_ttfa_table(tt)
    assert ("TTFA" in tt) is False


def test_delete_vdmx_table():
    tt = TTFont(FILEPATH_HINTED_TTF_3)  # tested in Ubuntu
    assert ("VDMX" in tt) is True
    remove_vdmx_table(tt)
    assert ("VDMX" in tt) is False


def test_delete_vdmx_table_missing_table():
    tt = TTFont(FILEPATH_DEHINTED_TTF)  # tested in Roboto
    assert ("VDMX" in tt) is False
    remove_vdmx_table(tt)
    assert ("VDMX" in tt) is False


# ========================================================
# glyf table instruction set bytecode removal
# ========================================================
def test_remove_glyf_instructions_hinted_font():
    tt = TTFont(FILEPATH_HINTED_TTF)
    number_removed = remove_glyf_instructions(tt)
    assert number_removed == 2717


def test_remove_glyf_instructions_dehinted_font():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    number_removed = remove_glyf_instructions(tt)
    assert number_removed == 0


# ========================================================
# gasp table edits
# ========================================================
def test_update_gasp_table():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert update_gasp_table(tt) is True
    assert tt["gasp"].gaspRange == {65535: 0x000A}


def test_update_gasp_table_previous_correct_definition():
    tt = TTFont(FILEPATH_DEHINTED_TTF_2)
    assert update_gasp_table(tt) is False
    assert tt["gasp"].gaspRange == {65535: 0x000A}


# =========================================
# maxp table edits
# =========================================
def test_update_maxp_table():
    tt = TTFont(
        FILEPATH_HINTED_TTF_2
    )  # test in Noto Sans as all values are modified there
    assert update_maxp_table(tt) is True
    assert tt["maxp"].maxZones == 0
    assert tt["maxp"].maxTwilightPoints == 0
    assert tt["maxp"].maxStorage == 0
    assert tt["maxp"].maxFunctionDefs == 0
    assert tt["maxp"].maxStackElements == 0
    assert tt["maxp"].maxSizeOfInstructions == 0


# =========================================
# head table edits
# =========================================
def test_update_head_table_flags_without_ltsh_hdmx():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert (tt["head"].flags & (1 << 4)) != 0
    remove_hdmx_table(tt)
    remove_ltsh_table(tt)
    response = update_head_table_flags(tt)
    assert response is True
    assert (tt["head"].flags & (1 << 4)) == 0


def test_update_head_table_flags_with_ltsh_hdmx():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert (tt["head"].flags & (1 << 4)) != 0
    response = update_head_table_flags(tt)
    assert response is False
    assert (tt["head"].flags & (1 << 4)) != 0


def test_update_head_table_flags_with_ltsh():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert (tt["head"].flags & (1 << 4)) != 0
    remove_hdmx_table(tt)
    response = update_head_table_flags(tt)
    assert response is False
    assert (tt["head"].flags & (1 << 4)) != 0


def test_update_head_table_flags_with_hdmx():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert (tt["head"].flags & (1 << 4)) != 0
    remove_ltsh_table(tt)
    response = update_head_table_flags(tt)
    assert response is False
    assert (tt["head"].flags & (1 << 4)) != 0


def test_update_head_table_flags_previously_cleared():
    tt = TTFont(FILEPATH_HINTED_TTF_2)
    assert (tt["head"].flags & (1 << 4)) == 0
    response = update_head_table_flags(tt)
    assert response is False
    assert (tt["head"].flags & (1 << 4)) == 0
