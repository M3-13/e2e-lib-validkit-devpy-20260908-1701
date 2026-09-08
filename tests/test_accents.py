import pytest

from validkit._accents import strip_accents


def test_strips_accents_from_diacritic_text():
    assert strip_accents("café au lait — déjà") == "cafe au lait — deja"


def test_already_accent_free_string_is_unchanged():
    assert strip_accents("cafe au lait — deja") == "cafe au lait — deja"


def test_empty_string_returns_empty_string():
    assert strip_accents("") == ""


def test_german_umlauts_are_stripped():
    assert strip_accents("übermäßig schön") == "ubermaßig schon"


def test_combining_marks_only_are_removed():
    assert strip_accents("e\u0301") == "e"


def test_non_latin_accented_characters_are_handled():
    assert strip_accents("Ångström") == "Angstrom"


def test_wrong_type_raises_type_error():
    with pytest.raises(TypeError) as exc_info:
        strip_accents(42)
    message = str(exc_info.value)
    assert "text" in message
    assert "42" not in message


def test_none_raises_type_error():
    with pytest.raises(TypeError):
        strip_accents(None)
