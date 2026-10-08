def is_safe_input(value: str) -> bool:
    if value is None:
        return False
    cleaned = value.strip()
    return bool(cleaned) and len(cleaned) <= 5000
