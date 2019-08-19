import os

from dehinter.paths import filepath_exists

import pytest


def test_filepath_exists_good_filepath():
    good_path = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    assert filepath_exists(good_path) is True


def test_filepath_exists_bad_filepath():
    bad_path = "bogus_file.txt"
    assert filepath_exists(bad_path) is False
