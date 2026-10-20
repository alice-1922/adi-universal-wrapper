from urllib.parse import urlsplit

def is_safe_next(value: str) -> bool:
    parsed = urlsplit(value)
    return value.startswith("/")
