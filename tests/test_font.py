import os

from dehinter.font import is_truetype_font

import pytest


def test_is_truetype_font_for_ttf():
    path = os.path.join("tests", "test_files", "fonts", "Hack-Regular.ttf")
    assert is_truetype_font(path) is True


def test_is_truetype_font_for_not_ttf():
    path = os.path.join("tests", "test_files", "text", "test.txt")
    assert is_truetype_font(path) is False