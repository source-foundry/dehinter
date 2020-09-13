import os

from dehinter.paths import filepath_exists, get_default_out_path

import pytest


def test_filepath_exists_good_filepath():
    good_path = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    assert filepath_exists(good_path) is True


def test_filepath_exists_bad_filepath():
    bad_path = "bogus_file.txt"
    assert filepath_exists(bad_path) is False


def test_get_default_filepath_without_dir():
    path = "Roboto-Regular.ttf"
    default_path = get_default_out_path(path)
    assert default_path == "Roboto-Regular-dehinted.ttf"


def test_get_default_filepath_with_dir():
    path = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    default_path = get_default_out_path(path)
    assert default_path == os.path.join(
        "tests", "test_files", "fonts", "Roboto-Regular-dehinted.ttf"
    )
