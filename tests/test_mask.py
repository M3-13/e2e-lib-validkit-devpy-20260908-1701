import pytest

from validkit import mask_secret


def test_masks_all_but_last_keep_chars():
    assert mask_secret("geheim123456789", keep=4) == "*" * 11 + "6789"


def test_text_shorter_than_keep_is_fully_masked():
    assert mask_secret("kurz", keep=4) == "****"


def test_text_equal_to_keep_is_fully_masked():
    assert mask_secret("abcd", keep=4) == "****"


def test_single_char_with_keep_one_is_fully_masked():
    assert mask_secret("x", keep=1) == "*"


def test_keep_zero_masks_everything():
    assert mask_secret("abc", keep=0) == "***"


def test_default_keep_is_four():
    assert mask_secret("geheim123456789") == "*" * 11 + "6789"


def test_empty_text():
    assert mask_secret("", keep=4) == ""


def test_empty_text_with_keep_zero():
    assert mask_secret("", keep=0) == ""


def test_negative_keep_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("x", keep=-1)


def test_negative_keep_message_does_not_leak_value():
    with pytest.raises(ValueError) as excinfo:
        mask_secret("x", keep=-1)
    assert "-1" not in str(excinfo.value)
    assert "keep" in str(excinfo.value)


def test_non_string_text_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret(42, keep=4)


def test_non_string_text_message_does_not_leak_value():
    with pytest.raises(TypeError) as excinfo:
        mask_secret(42, keep=4)
    assert "42" not in str(excinfo.value)
    assert "text" in str(excinfo.value)


def test_non_int_keep_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret("geheim", keep="4")


def test_non_int_keep_message_does_not_leak_value():
    with pytest.raises(TypeError) as excinfo:
        mask_secret("geheim", keep=2.5)
    assert "2.5" not in str(excinfo.value)
    assert "keep" in str(excinfo.value)
