def is_valid_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_valid_amount(value):
    try:
        float(value)
        return float(value) > 0
    except ValueError:
        return False


def is_valid_string(value):
    return isinstance(value, str) and len(value.strip()) > 0