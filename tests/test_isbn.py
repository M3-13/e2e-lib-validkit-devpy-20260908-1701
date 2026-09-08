import pytest

from validkit._isbn import is_valid_isbn13


def test_valid_isbn13_with_hyphens():
    assert is_valid_isbn13("978-3-16-148410-0") is True


def test_valid_isbn13_without_hyphens():
    assert is_valid_isbn13("9783161484100") is True


def test_valid_isbn13_another_example():
    assert is_valid_isbn13("9780306406157") is True


def test_changed_check_digit_is_invalid():
    assert is_valid_isbn13("978-3-16-148410-5") is False


def test_changed_non_check_digit_is_invalid():
    assert is_valid_isbn13("9793161484100") is False


def test_too_short_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("97831614841")


def test_too_long_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("97831614841000")


def test_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("")


def test_letters_raise_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("abc")


def test_mixed_invalid_characters_raise_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("97831614841XX")


def test_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_isbn13(42)


def test_none_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_isbn13(None)


def test_value_error_message_does_not_leak_input():
    with pytest.raises(ValueError) as exc_info:
        is_valid_isbn13("97831614841XX")
    assert "97831614841XX" not in str(exc_info.value)
    assert "text" in str(exc_info.value)


def test_type_error_message_does_not_leak_input():
    with pytest.raises(TypeError) as exc_info:
        is_valid_isbn13(42)
    assert "42" not in str(exc_info.value)
    assert "text" in str(exc_info.value)
