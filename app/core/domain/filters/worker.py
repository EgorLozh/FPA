from dataclasses import dataclass
from core.domain.filters.base import BaseFilter


@dataclass
class WorkerFilter(BaseFilter):
    worker_name: str | None = None
    department_id: int | None = None
