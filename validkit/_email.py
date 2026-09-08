def is_valid_email(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if any(ch.isspace() for ch in text):
        return False

    if text.count("@") != 1:
        return False

    local, domain = text.split("@")
    if not local:
        return False

    if "." not in domain:
        return False

    tld = domain.rsplit(".", 1)[-1]
    return len(tld) >= 2 and tld.isalnum()
