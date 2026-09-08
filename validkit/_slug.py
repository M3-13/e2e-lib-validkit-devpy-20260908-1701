import re
import unicodedata


def slugify(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text muss ein str sein")

    normalized = unicodedata.normalize("NFD", text)
    without_accents = "".join(c for c in normalized if not unicodedata.combining(c))
    lower = without_accents.lower()
    hyphenated = re.sub(r"[^a-z0-9]+", "-", lower)
    return hyphenated.strip("-")
