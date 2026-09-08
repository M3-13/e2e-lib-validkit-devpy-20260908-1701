_COUNTRY_CALLING_CODES = {
    "AT": "43",
    "BE": "32",
    "CH": "41",
    "DE": "49",
    "DK": "45",
    "ES": "34",
    "FI": "358",
    "FR": "33",
    "GB": "44",
    "IT": "39",
    "NL": "31",
    "NO": "47",
    "PL": "48",
    "PT": "351",
    "SE": "46",
    "US": "1",
}


def normalize_phone(text: str, country_code: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if not isinstance(country_code, str):
        raise TypeError("country_code must be a str")

    calling_code = _COUNTRY_CALLING_CODES.get(country_code.upper())
    if calling_code is None:
        raise ValueError("country_code must be a valid ISO 3166-1 alpha-2 code")

    cleaned = text.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if cleaned.startswith("+"):
        cleaned = cleaned[1:]
    if not cleaned or not cleaned.isdigit():
        raise ValueError(
            "text must be a phone number of digits with optional spaces, hyphens and parentheses"
        )

    national = cleaned.lstrip("0")
    if national.startswith(calling_code):
        national = national[len(calling_code) :].lstrip("0")

    if not national:
        raise ValueError(
            "text must be a phone number of digits with optional spaces, hyphens and parentheses"
        )

    return "+" + calling_code + national
