import pytest

from validkit import normalize_phone


@pytest.mark.parametrize(
    ("text", "country_code", "expected"),
    [
        ("030 1234567", "DE", "+49301234567"),
        ("+49 30 1234567", "DE", "+49301234567"),
        ("0301234567", "DE", "+49301234567"),
        ("030-1234567", "DE", "+49301234567"),
        ("(030) 1234567", "DE", "+49301234567"),
        ("030 1234567", "de", "+49301234567"),
        ("0049 30 1234567", "DE", "+49301234567"),
        ("+43 1 234567", "AT", "+431234567"),
        ("+41 44 234 56 78", "CH", "+41442345678"),
        ("+33 1 42 68 53 00", "FR", "+33142685300"),
        ("+44 20 7946 0958", "GB", "+442079460958"),
        ("+1 202 555 0143", "US", "+12025550143"),
        ("+39 06 698 12345", "IT", "+39669812345"),
        ("+34 91 234 56 78", "ES", "+34912345678"),
        ("+31 20 123 4567", "NL", "+31201234567"),
        ("+32 2 123 45 67", "BE", "+3221234567"),
        ("+48 22 123 45 67", "PL", "+48221234567"),
        ("+351 21 234 5678", "PT", "+351212345678"),
        ("+46 8 123 456 78", "SE", "+46812345678"),
        ("+47 22 12 34 56", "NO", "+4722123456"),
        ("+45 12 34 56 78", "DK", "+4512345678"),
        ("+358 9 123 4567", "FI", "+35891234567"),
    ],
)
def test_normalize_phone_normal(text, country_code, expected):
    assert normalize_phone(text, country_code) == expected


@pytest.mark.parametrize("text", ["", "   ", "()--", "+", "abc", "030 abc 1234", "000"])
def test_normalize_phone_non_normalizable(text):
    with pytest.raises(ValueError):
        normalize_phone(text, "DE")


def test_normalize_phone_unknown_country_code():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "XX")


def test_normalize_phone_three_letter_code_rejected():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "DEU")


@pytest.mark.parametrize("text", [42, None, 3.14, ["030"]])
def test_normalize_phone_wrong_text_type(text):
    with pytest.raises(TypeError):
        normalize_phone(text, "DE")


@pytest.mark.parametrize("country_code", [49, None, ["DE"]])
def test_normalize_phone_wrong_country_code_type(country_code):
    with pytest.raises(TypeError):
        normalize_phone("030 1234567", country_code)


def test_normalize_phone_type_error_message_hides_value():
    with pytest.raises(TypeError) as exc_info:
        normalize_phone(42, "DE")
    assert "42" not in str(exc_info.value)
    assert "text" in str(exc_info.value)


def test_normalize_phone_value_error_message_hides_input():
    with pytest.raises(ValueError) as exc_info:
        normalize_phone("030 1234567", "XX")
    assert "XX" not in str(exc_info.value)
    assert "030" not in str(exc_info.value)
    assert "country_code" in str(exc_info.value)
