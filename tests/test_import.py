import inspect

import validkit

EXPECTED_NAMES = {
    "is_valid_email",
    "luhn_check",
    "is_valid_iban",
    "is_valid_isbn13",
    "normalize_phone",
    "strip_accents",
    "mask_secret",
    "slugify",
    "clamp",
}

EXPECTED_PARAMS = {
    "is_valid_email": ["text"],
    "luhn_check": ["digits"],
    "is_valid_iban": ["text"],
    "is_valid_isbn13": ["text"],
    "normalize_phone": ["text", "country_code"],
    "strip_accents": ["text"],
    "mask_secret": ["text", "keep"],
    "slugify": ["text"],
    "clamp": ["value", "low", "high"],
}

EXPECTED_DEFAULTS = {
    "mask_secret": {"keep": 4},
}

EXPECTED_RETURNS = {
    "is_valid_email": bool,
    "luhn_check": bool,
    "is_valid_iban": bool,
    "is_valid_isbn13": bool,
    "normalize_phone": str,
    "strip_accents": str,
    "mask_secret": str,
    "slugify": str,
    "clamp": float,
}


def test_all_has_exactly_nine_names():
    assert len(validkit.__all__) == 9
    assert set(validkit.__all__) == EXPECTED_NAMES


def test_every_name_is_importable():
    for name in EXPECTED_NAMES:
        assert hasattr(validkit, name), f"{name!r} is not reachable via validkit"
        assert callable(getattr(validkit, name)), f"{name!r} is not callable"


def test_signatures_match_contract():
    for name in EXPECTED_NAMES:
        func = getattr(validkit, name)
        sig = inspect.signature(func)

        assert list(sig.parameters) == EXPECTED_PARAMS[name], f"{name!r} parameters differ"
        for param_name, default in EXPECTED_DEFAULTS.get(name, {}).items():
            assert sig.parameters[param_name].default == default, (
                f"{name!r} default for {param_name!r} differs"
            )
        assert sig.return_annotation == EXPECTED_RETURNS[name], (
            f"{name!r} return annotation differs"
        )
