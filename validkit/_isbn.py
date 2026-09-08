def is_valid_isbn13(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("text must be a str")

    digits = text.replace("-", "")

    if len(digits) != 13:
        raise ValueError("text must contain exactly 13 digits after removing hyphens")

    if not all(ch in "0123456789" for ch in digits):
        raise ValueError("text must contain only digits and hyphens")

    weighted_sum = 0
    for index, ch in enumerate(digits[:12]):
        weight = 1 if index % 2 == 0 else 3
        weighted_sum += int(ch) * weight

    check_digit = (10 - (weighted_sum % 10)) % 10
    return check_digit == int(digits[12])
