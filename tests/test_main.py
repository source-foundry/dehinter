import array
import os
import shutil

from fontTools.ttLib import TTFont

from dehinter.__main__ import run

import pytest


#
#  Integration tests
#

def font_validator(filepath):
    assert os.path.exists(filepath)
    tt = TTFont(filepath)
    assert "cvt " not in tt
    assert "fpgm" not in tt
    assert "hdmx" not in tt
    assert "LTSH" not in tt
    assert "prep" not in tt
    assert "TTFA" not in tt
    for glyph in tt["glyf"].glyphs.values():
        glyph.expand(tt["glyf"])
        if glyph.isComposite():
            assert not hasattr(glyph, "program")
        if hasattr(glyph, "program"):
            assert glyph.program.bytecode == array.array("B", [])
    assert tt["gasp"].gaspRange == {65535: 15}
    assert tt["maxp"].maxZones == 0
    assert tt["maxp"].maxTwilightPoints == 0
    assert tt["maxp"].maxStorage == 0
    assert tt["maxp"].maxStackElements == 0
    assert tt["maxp"].maxSizeOfInstructions == 0
    assert (tt["head"].flags & 1 << 4) == 0


def test_default_run_roboto():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular-dehinted.ttf")
    test_args = [test_inpath]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    font_validator(test_outpath)

    # tear down
    shutil.rmtree(test_dir)


def test_default_run_noto():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "NotoSans-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "NotoSans-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "NotoSans-Regular-dehinted.ttf")
    test_args = [test_inpath]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    font_validator(test_outpath)

    # tear down
    shutil.rmtree(test_dir)


def test_run_roboto_keep_cvt():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular-dehinted.ttf")
    test_args = [test_inpath, "--keep-cvt"]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    tt = TTFont(test_outpath)
    assert "cvt " in tt

    # tear down
    shutil.rmtree(test_dir)


def test_run_roboto_keep_fpgm():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular-dehinted.ttf")
    test_args = [test_inpath, "--keep-fpgm"]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    tt = TTFont(test_outpath)
    assert "fpgm" in tt

    # tear down
    shutil.rmtree(test_dir)


def test_run_roboto_keep_hdmx():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular-dehinted.ttf")
    test_args = [test_inpath, "--keep-hdmx"]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    tt = TTFont(test_outpath)
    assert "hdmx" in tt

    # tear down
    shutil.rmtree(test_dir)


def test_run_roboto_keep_ltsh():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular-dehinted.ttf")
    test_args = [test_inpath, "--keep-ltsh"]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    tt = TTFont(test_outpath)
    assert "LTSH" in tt

    # tear down
    shutil.rmtree(test_dir)


def test_run_roboto_keep_prep():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular-dehinted.ttf")
    test_args = [test_inpath, "--keep-prep"]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    tt = TTFont(test_outpath)
    assert "prep" in tt

    # tear down
    shutil.rmtree(test_dir)


def test_run_noto_keep_ttfa():  # this has to be tested in Noto as it contains a TTFA table
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "NotoSans-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "NotoSans-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "NotoSans-Regular-dehinted.ttf")
    test_args = [test_inpath, "--keep-ttfa"]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    tt = TTFont(test_outpath)
    assert "TTFA" in tt

    # tear down
    shutil.rmtree(test_dir)


def test_run_roboto_keep_glyf():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular-dehinted.ttf")
    test_args = [test_inpath, "--keep-glyf"]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    tt_pre = TTFont(test_inpath)
    tt_post = TTFont(test_outpath)
    assert tt_pre["glyf"] == tt_post["glyf"]

    # tear down
    shutil.rmtree(test_dir)


def test_run_roboto_keep_gasp():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular-dehinted.ttf")
    test_args = [test_inpath, "--keep-gasp"]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    tt = TTFont(test_outpath)
    assert tt["gasp"].gaspRange == {8: 2, 65535: 15}  # unmodified value in Roboto

    # tear down
    shutil.rmtree(test_dir)


def test_run_noto_keep_maxp():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "NotoSans-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "NotoSans-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "NotoSans-Regular-dehinted.ttf")
    test_args = [test_inpath, "--keep-maxp"]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    tt = TTFont(test_outpath)
    assert tt["maxp"].maxZones != 0
    assert tt["maxp"].maxTwilightPoints != 0
    assert tt["maxp"].maxStorage != 0
    assert tt["maxp"].maxFunctionDefs != 0
    assert tt["maxp"].maxStackElements != 0
    assert tt["maxp"].maxSizeOfInstructions != 0

    # tear down
    shutil.rmtree(test_dir)


def test_run_roboto_keep_head():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular-dehinted.ttf")
    test_args = [test_inpath, "--keep-head"]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    tt = TTFont(test_outpath)
    assert (tt["head"].flags & 1 << 4) != 0

    # tear down
    shutil.rmtree(test_dir)


def test_run_with_outfile_path_roboto():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "Roboto-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "Roboto-Regular-dehintilio.ttf")
    test_args = [test_inpath, "--out", test_outpath]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    font_validator(test_outpath)

    # tear down
    shutil.rmtree(test_dir)


def test_run_with_outfile_path_noto():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "NotoSans-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "NotoSans-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "NotoSans-Regular-dehintilio.ttf")
    test_args = [test_inpath, "-o", test_outpath]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    run(test_args)

    # test
    font_validator(test_outpath)

    # tear down
    shutil.rmtree(test_dir)


#
# Validation error testing
#

def test_run_with_invalid_filepath():
    with pytest.raises(SystemExit):
        run(["bogusfile.txt"])


def test_run_with_non_font_file():
    with pytest.raises(SystemExit):
        run([os.path.join("tests", "test_files", "text", "test.txt")])


def test_run_dehinted_file_write_inplace():
    test_dir = os.path.join("tests", "test_files", "fonts", "temp")
    notouch_inpath = os.path.join("tests", "test_files", "fonts", "NotoSans-Regular.ttf")
    test_inpath = os.path.join("tests", "test_files", "fonts", "temp", "NotoSans-Regular.ttf")
    test_outpath = os.path.join("tests", "test_files", "fonts", "temp", "NotoSans-Regular.ttf")
    test_args = [test_inpath, "-o", test_outpath]

    # setup
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    shutil.copyfile(notouch_inpath, test_inpath)

    # execute
    with pytest.raises(SystemExit):
        run(test_args)

    # tear down
    shutil.rmtree(test_dir)
