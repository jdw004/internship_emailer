"""Source parser safety checks."""

from src.sources.github_lists import _map_listing


def test_github_list_rejects_non_http_urls():
    raw = {
        "company_name": "Acme",
        "title": "Software Engineer Intern",
        "url": "javascript:alert(1)",
        "locations": ["New York, NY"],
    }

    assert _map_listing(raw, "test") is None
