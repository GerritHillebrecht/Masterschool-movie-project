def is_float(string: str) -> bool:
    """
    Validates that a string is convertable into a float-value.
    :param string: The potentially convertable string.
    """
    try:
        float(string)
    except ValueError:
        return False

    return True
