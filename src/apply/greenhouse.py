"""Greenhouse applicator: the job URL is the application form page."""

from __future__ import annotations

from ..models import Job
from .base import Applicator
from .url_safety import is_https_host


_GREENHOUSE_HOSTS = {"boards.greenhouse.io", "job-boards.greenhouse.io"}


class GreenhouseApplicator(Applicator):
    ats = "greenhouse"

    def can_handle(self, job: Job) -> bool:
        return is_https_host(job.url, _GREENHOUSE_HOSTS)

    def application_url(self, job: Job) -> str:
        # Greenhouse renders the application form inline on the job page.
        return job.url
