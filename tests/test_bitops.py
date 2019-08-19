import pytest

from dehinter.bitops import is_bit_k_set, clear_bit_k, set_bit_k


def test_is_bit_k_set_true():
    assert is_bit_k_set(15, 1) is True


def test_is_bit_k_set_false():
    assert is_bit_k_set(13, 1) is False


def test_clear_bit_k():
    # clearing bit 1 on 0b1111 is 0b1101 = 13
    assert clear_bit_k(15, 1) == 13


def test_set_bit_k():
    # setting bit 1 on 0b1101 is 0b1111 = 15
    assert set_bit_k(13, 1) == 15
