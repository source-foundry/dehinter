import os

from dehinter.font import is_truetype_font, has_cvt_table, has_fpgm_table, has_prep_table

import pytest
from fontTools.ttLib import TTFont

FILEPATH_TEST_TEXT = os.path.join("tests", "test_files", "text", "test.txt")
FILEPATH_HINTED_TTF = os.path.join("tests", "test_files", "fonts", "Hack-Regular.ttf")
FILEPATH_DEHINTED_TTF = os.path.join("tests", "test_files", "fonts", "Hack-Regular-dehinted.ttf")


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
