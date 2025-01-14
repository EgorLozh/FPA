from core.domain.filters.base import BaseFilter

from dataclasses import dataclass

@dataclass
class DepartmentFilter(BaseFilter):
    name: str | None = None