"""Data schemas for fetcher.

Dribia 2021/04/21, Oleguer Sagarra <ula@dribia.com>  # original author
"""

import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Sequence

from driganttic.schemas.base import Base


class ErrorMessage(str, Enum):
    """Error message options."""

    API_ERROR: str = "API_ERROR"


# Enums


class ServiceEnum(str, Enum):
    """Service Enum."""

    projecte = "Projecte"
    manteniment = "Manteniment"
    intern = "Intern"
    discovery = "Discovery"
    peed = "PEED"


class RoleEnum(str, Enum):
    """Role Enum."""

    soci = "Soci"
    bd = "BD"
    lds = "LDS"
    ds = "DS"


class ScenarioEnum(str, Enum):
    """Scenario Enum."""

    esperat = "Esperat"
    optimista = "Optimista"
    congelat = "Congelat"
    confirmat = "Confirmat"


class FetcherDetails(Base):
    """Fetcher Details schema.

    Warning: Timestamps are time aware!
    """

    id: Optional[str]
    fetched_timestamp: datetime.datetime = datetime.datetime.now()
    status: str
    name: Optional[str]
    created: Optional[datetime.datetime]


class FetcherList(Base):
    """Fetcher List schema."""

    fetched_timestamp: datetime.datetime = datetime.datetime.now()
    fetched_items: Sequence[FetcherDetails]
    pages: int
    page: int


class ResourceDetails(FetcherDetails):
    """Resource List schema."""

    capacity: float
    role: RoleEnum


class TaskDetails(FetcherDetails):
    """Task List schema."""

    # could be holidays
    projectId: Optional[str]
    resources: List[str]
    start: datetime.datetime
    end: datetime.datetime
    utilizationPercent: Optional[float]
    isBillable: Optional[bool]


class ProjectDetails(FetcherDetails):
    """Project List schema."""

    dateAproxStart: Optional[datetime.datetime]
    team: Optional[float]
    discount: Optional[float]
    probability: Optional[float]
    service: ServiceEnum
    scenario: ScenarioEnum
    sprints: Optional[float]


class DataFieldsEnum(str, Enum):
    """Standard enum."""

    listValues = "listValues"
    numbers = "numbers"


class DataFields(Base):
    """Data fields model for API."""

    dates: Dict = {}
    numbers: Dict = {}
    listValues: Any = {}
    texts: Dict = {}
    users: Dict = {}


class ResourceList(FetcherList):
    """Resource List schema."""

    fetched_items: Sequence[ResourceDetails]


class TaskList(FetcherList):
    """Task List schema."""

    fetched_items: Sequence[TaskDetails]


class ProjectList(FetcherList):
    """Project List schema."""

    fetched_items: Sequence[ProjectDetails]
