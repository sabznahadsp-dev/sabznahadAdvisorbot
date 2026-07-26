def is_valid_name(name: str):
    name = name.strip()

    if len(name) < 2:
        return False

    return True