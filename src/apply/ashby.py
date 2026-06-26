"""Ashby applicator: the application form lives at <jobUrl>/application."""

from __future__ import annotations

from ..models import Job
from .base import Applicator
from .url_safety import is_https_host


_ASHBY_HOSTS = {"jobs.ashbyhq.com"}


class AshbyApplicator(Applicator):
    ats = "ashby"

    def can_handle(self, job: Job) -> bool:
        return is_https_host(job.url, _ASHBY_HOSTS)

    def application_url(self, job: Job) -> str:
        base = (job.url or "").rstrip("/")
        return base if base.endswith("/application") else f"{base}/application"
