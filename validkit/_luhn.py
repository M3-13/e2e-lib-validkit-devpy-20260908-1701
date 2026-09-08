def luhn_check(digits: str | int) -> bool:
    if isinstance(digits, bool) or not isinstance(digits, (str, int)):
        raise TypeError("digits must be of type str or int")

    cleaned = str(digits).replace(" ", "").replace("-", "")

    if not cleaned:
        raise ValueError("digits must contain at least one digit")
    if not cleaned.isdigit():
        raise ValueError(
            "digits must contain only digits, optionally separated by spaces or hyphens"
        )

    total = 0
    for index, char in enumerate(reversed(cleaned)):
        value = int(char)
        if index % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value

    return total % 10 == 0
