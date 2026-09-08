import pytest

from validkit import clamp


def test_value_inside_interval_unchanged():
    assert clamp(5, 0, 10) == 5


def test_value_below_low_is_clamped_up():
    assert clamp(-5, 0, 10) == 0


def test_value_above_high_is_clamped_down():
    assert clamp(15, 0, 10) == 10


def test_float_value_is_clamped():
    assert clamp(2.5, 0, 10) == 2.5
    assert clamp(-1.5, 0, 10) == 0
    assert clamp(12.5, 0, 10) == 10


def test_value_equal_to_boundaries():
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10


def test_low_greater_than_high_raises_value_error():
    with pytest.raises(ValueError):
        clamp(5, 10, 0)


def test_non_numeric_value_raises_type_error():
    with pytest.raises(TypeError):
        clamp("abc", 0, 10)


def test_non_numeric_low_raises_type_error():
    with pytest.raises(TypeError):
        clamp(5, "0", 10)


def test_non_numeric_high_raises_type_error():
    with pytest.raises(TypeError):
        clamp(5, 0, "10")


def test_bool_input_raises_type_error():
    with pytest.raises(TypeError):
        clamp(True, 0, 10)


def test_error_messages_do_not_contain_input_values():
    with pytest.raises(TypeError) as exc_info:
        clamp("secret-value", 0, 10)
    assert "secret-value" not in str(exc_info.value)

    with pytest.raises(ValueError) as exc_info:
        clamp(5, 10, 0)
    assert "5" not in str(exc_info.value)
