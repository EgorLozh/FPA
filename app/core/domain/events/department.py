from dataclasses import dataclass
from core.domain.filters.department import DepartmentFilter
from core.domain.events.base import BaseEvent


@dataclass
class CreateDepartmentEvent(BaseEvent):
    name: str
    description: str | None


@dataclass
class GetDepartmentsEvent(BaseEvent):
    department_filter: DepartmentFilter | None = None