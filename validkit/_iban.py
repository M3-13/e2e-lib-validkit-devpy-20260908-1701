import re

_IBAN_RE = re.compile(r"^[A-Z]{2}[0-9]+$")

_MIN_LENGTH = 15
_MAX_LENGTH = 34


def is_valid_iban(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("text must be of type str")

    compact = text.replace(" ", "")
    upper = compact.upper()

    if not _IBAN_RE.fullmatch(upper):
        raise ValueError("text must match IBAN format (two letters followed by digits)")
    if not _MIN_LENGTH <= len(compact) <= _MAX_LENGTH:
        raise ValueError("text must be between 15 and 34 characters long")

    rearranged = upper[4:] + upper[:4]
    digits = "".join(str(int(ch, 36)) for ch in rearranged)
    return int(digits) % 97 == 1
