def clamp(value: float, low: float, high: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("value must be an int or float")
    if isinstance(low, bool) or not isinstance(low, (int, float)):
        raise TypeError("low must be an int or float")
    if isinstance(high, bool) or not isinstance(high, (int, float)):
        raise TypeError("high must be an int or float")
    if low > high:
        raise ValueError("low must be less than or equal to high")
    return max(low, min(value, high))
