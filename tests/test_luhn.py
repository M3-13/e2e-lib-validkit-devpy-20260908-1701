import pytest

from validkit import luhn_check


@pytest.mark.parametrize(
    "digits",
    [
        "79927398713",
        "4111 1111 1111 1111",
        "4111-1111-1111-1111",
        "4000 0566 5566 5556",
        "4532014816553929",
        42,
        79927398713,
    ],
)
def test_luhn_check_accepts_valid_digit_sequences(digits):
    assert luhn_check(digits) is True


@pytest.mark.parametrize(
    "digits",
    [
        "79927398714",
        "4532014816553922",
        "4111 1111 1111 1112",
        "7",
        "1",
    ],
)
def test_luhn_check_rejects_invalid_digit_sequences(digits):
    assert luhn_check(digits) is False


def test_luhn_check_accepts_all_zeroes():
    assert luhn_check("0000") is True


def test_luhn_check_single_zero():
    assert luhn_check("0") is True


def test_luhn_check_ticket_example_is_not_luhn_valid():
    # '4532 0148 1655 3921' is cited in the ticket as valid, but it is NOT
    # Luhn-valid: the weighted sum is 72 (72 % 10 == 2). The correct check
    # digit for the prefix 453201481655392 is 9, so the valid number is
    # '4532 0148 1655 3929' and both cited strings fail the mod-10 check.
    assert luhn_check("4532 0148 1655 3921") is False
    assert luhn_check("4532 0148 1655 3922") is False
    assert luhn_check("4532 0148 1655 3929") is True


@pytest.mark.parametrize(
    "digits",
    [
        "12a4",
        "",
        "   ",
        "--",
        "123#456",
        "12.34",
        "abc",
    ],
)
def test_luhn_check_raises_value_error_for_invalid_content(digits):
    with pytest.raises(ValueError):
        luhn_check(digits)


@pytest.mark.parametrize("digits", [None, 3.14, [], {}, True])
def test_luhn_check_raises_type_error_for_wrong_types(digits):
    with pytest.raises(TypeError):
        luhn_check(digits)


def test_luhn_check_value_error_message_does_not_leak_input():
    with pytest.raises(ValueError) as exc_info:
        luhn_check("12a4")
    assert "12a4" not in str(exc_info.value)
    assert "digits" in str(exc_info.value)


def test_luhn_check_type_error_message_does_not_leak_input():
    with pytest.raises(TypeError) as exc_info:
        luhn_check(3.14)
    assert "3.14" not in str(exc_info.value)
    assert "digits" in str(exc_info.value)
