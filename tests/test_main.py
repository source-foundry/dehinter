import array
import os
import shutil

from fontTools.ttLib import TTFont

from dehinter.__main__ import run


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

