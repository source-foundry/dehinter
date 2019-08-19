import os

from dehinter.system import get_filesize


def test_get_filesize_bytes():
    byte_file = os.path.join("tests", "test_files", "text", "byte.txt")
    assert get_filesize(byte_file) == ("1.00", "B")


def test_get_filesize_kilobytes():
    kilobyte_file = os.path.join("tests", "test_files", "text", "kb.txt")
    assert get_filesize(kilobyte_file) == ("1.00", "KB")


def test_get_filesize_megabytes():
    megabyte_file = os.path.join("tests", "test_files", "text", "mb.txt")
    assert get_filesize(megabyte_file) == ("1.00", "MB")
