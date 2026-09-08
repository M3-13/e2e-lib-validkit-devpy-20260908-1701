import pytest

from validkit._slug import slugify


def test_slugify_with_accents_and_special_chars():
    assert slugify("Héllo Wörld!  Test -- x") == "hello-world-test-x"


def test_slugify_already_slugged_text_is_unchanged():
    assert slugify("hello-world-test-x") == "hello-world-test-x"


def test_slugify_lowercases_uppercase_input():
    assert slugify("Hello WORLD") == "hello-world"


def test_slugify_collapses_multiple_hyphens():
    assert slugify("a---b   c") == "a-b-c"


def test_slugify_strips_leading_and_trailing_hyphens():
    assert slugify("- hello -") == "hello"


def test_slugify_keeps_digits():
    assert slugify("Order 42 shipped") == "order-42-shipped"


def test_slugify_handles_umlauts():
    assert slugify("Ünïcodé Tëst") == "unicode-test"


def test_slugify_only_special_characters_returns_empty_string():
    assert slugify("!@#$%^&*()") == ""


def test_slugify_empty_string_returns_empty_string():
    assert slugify("") == ""


def test_slugify_non_string_raises_type_error():
    with pytest.raises(TypeError):
        slugify(42)


def test_slugify_none_raises_type_error():
    with pytest.raises(TypeError):
        slugify(None)


def test_slugify_type_error_message_names_param_and_type_not_value():
    with pytest.raises(TypeError) as exc_info:
        slugify(42)
    message = str(exc_info.value)
    assert "text" in message
    assert "str" in message
    assert "42" not in message
