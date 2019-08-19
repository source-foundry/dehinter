import os

from dehinter.font import is_truetype_font, has_cvt_table, has_fpgm_table, has_prep_table
from dehinter.font import remove_cvt, remove_fpgm, remove_prep, remove_glyf_instructions
from dehinter.font import update_gasp_table

import pytest
from fontTools.ttLib import TTFont

FILEPATH_TEST_TEXT = os.path.join("tests", "test_files", "text", "test.txt")
FILEPATH_HINTED_TTF = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
FILEPATH_DEHINTED_TTF = os.path.join("tests", "test_files", "fonts", "Roboto-Regular-dehinted.ttf")


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


def test_has_prep_table_true():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert has_prep_table(tt) is True


def test_has_prep_table_false():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert has_prep_table(tt) is False


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
    remove_cvt(tt)
    assert ("cvt " in tt) is False


def test_delete_cvt_table_missing_table():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert ("cvt " in tt) is False
    remove_cvt(tt)
    assert ("cvt " in tt) is False


def test_delete_fpgm_table():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert ("fpgm" in tt) is True
    remove_fpgm(tt)
    assert ("fpgm" in tt) is False


def test_delete_fpgm_table_missing_table():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert ("fpgm" in tt) is False
    remove_fpgm(tt)
    assert ("fpgm" in tt) is False


def test_delete_prep_table():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert ("prep" in tt) is True
    remove_prep(tt)
    assert ("prep" in tt) is False


def test_delete_prep_table_missing_table():
    tt = TTFont(FILEPATH_DEHINTED_TTF)
    assert ("prep" in tt) is False
    remove_prep(tt)
    assert ("prep" in tt) is False


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
# gasp table edit
# ========================================================
def test_update_gasp_table():
    tt = TTFont(FILEPATH_HINTED_TTF)
    assert update_gasp_table(tt) is True
    assert tt["gasp"].gaspRange == {65535: 15}
