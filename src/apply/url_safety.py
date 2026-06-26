"""URL safety checks for the local apply tool."""

from __future__ import annotations

from urllib.parse import urlparse


def is_https_host(url: str, allowed_hosts: set[str]) -> bool:
    """Return True only for HTTPS URLs on an exact allowed host."""
    try:
        parsed = urlparse(url or "")
    except ValueError:
        return False
    return parsed.scheme == "https" and (parsed.hostname or "").lower() in allowed_hosts
