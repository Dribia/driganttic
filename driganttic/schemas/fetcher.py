"""Data schemas for fetcher.

Dribia 2021/04/21, Oleguer Sagarra <ula@dribia.com>  # original author
"""

import datetime
from enum import Enum

from driganttic.schemas.base import Base


class ErrorMessage(str, Enum):
    """Error message options."""

    API_ERROR: str = "API_ERROR"


class FetcherDetails(Base):
    """Fetcher Details schema.

    Warning: Timestamps are time aware!
    """

    id: str
    fetched_timestamp: datetime.time = datetime.time()


class FetcherList(Base):
    """Fetcher List schema."""

    fetched_timestamp: datetime.time = datetime.time()
    # original_query: str


class ResourceList(FetcherList):
    """Resource List schema."""


class TaskList(FetcherList):
    """Task List schema."""


class ProjectList(FetcherList):
    """Project List schema."""


class ResourceDetails(FetcherDetails):
    """Resource List schema."""


class TaskDetails(FetcherDetails):
    """Task List schema."""


class ProjectDetails(FetcherDetails):
    """Project List schema."""