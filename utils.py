"""Shared utilities."""
from datetime import datetime, timezone


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def safe_int(v, default=0):
    try:
        return int(v)
    except (TypeError, ValueError):
        return default
