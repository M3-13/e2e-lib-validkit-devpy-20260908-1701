import pytest

from validkit import is_valid_iban


def test_valid_iban_with_spaces():
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True


def test_valid_iban_without_spaces():
    assert is_valid_iban("DE89370400440532013000") is True


def test_valid_iban_lowercase_country_code():
    assert is_valid_iban("de89 3704 0044 0532 0130 00") is True


def test_manipulated_iban_returns_false():
    assert is_valid_iban("DE89 3704 0044 0532 0130 01") is False


def test_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_iban(42)  # type: ignore[arg-type]


def test_none_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_iban(None)  # type: ignore[arg-type]


def test_invalid_format_starts_with_digits():
    with pytest.raises(ValueError):
        is_valid_iban("12DE 8937 0400 4405 3201 3000")


def test_invalid_format_letter_in_number_part():
    with pytest.raises(ValueError):
        is_valid_iban("DE89 3704 0044 0532 0130 0X")


def test_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_iban("")


def test_too_short_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_iban("DE123456789012")


def test_too_long_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_iban("DE" + "1" * 33)


def test_error_messages_do_not_contain_input_value():
    with pytest.raises(TypeError) as type_info:
        is_valid_iban(42)  # type: ignore[arg-type]
    assert "42" not in str(type_info.value)

    with pytest.raises(ValueError) as value_info:
        is_valid_iban("12DE 8937 0400 4405 3201 3000")
    assert "12DE" not in str(value_info.value)
