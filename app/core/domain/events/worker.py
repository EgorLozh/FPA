from core.domain.events.base import BaseEvent
from core.domain.filters.worker import WorkerFilter


class CreateWorkerEvent(BaseEvent):
    name: str
    department_id: int


class GetWorkersEvent(BaseEvent):
    worker_filter: WorkerFilter | None = None


class GetWorkerStatisticsEvent(BaseEvent):
    worker_filter: WorkerFilter
