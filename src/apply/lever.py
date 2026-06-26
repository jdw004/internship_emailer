"""Lever applicator: the application form lives at <jobUrl>/apply."""

from __future__ import annotations

from ..models import Job
from .base import Applicator
from .url_safety import is_https_host


_LEVER_HOSTS = {"jobs.lever.co"}


class LeverApplicator(Applicator):
    ats = "lever"

    def can_handle(self, job: Job) -> bool:
        return is_https_host(job.url, _LEVER_HOSTS)

    def application_url(self, job: Job) -> str:
        base = (job.url or "").rstrip("/")
        return base if base.endswith("/apply") else f"{base}/apply"
