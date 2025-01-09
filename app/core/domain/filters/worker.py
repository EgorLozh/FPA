from core.domain.filters import BaseFilter


class WorkerFilter(BaseFilter):
    worker_name: str | None = None
    department_id: int | None = None
