def mask_secret(text: str, keep: int = 4) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if not isinstance(keep, int):
        raise TypeError("keep must be an int")
    if keep < 0:
        raise ValueError("keep must be a non-negative integer")
    if keep == 0:
        return "*" * len(text)
    if len(text) <= keep:
        return "*" * len(text)
    return "*" * (len(text) - keep) + text[-keep:]
