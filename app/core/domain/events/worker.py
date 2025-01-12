from dataclasses import dataclass
from core.domain.events.base import BaseEvent
from core.domain.filters.worker import WorkerFilter


@dataclass
class CreateWorkerEvent(BaseEvent):
    name: str
    department_id: int


@dataclass
class GetWorkersEvent(BaseEvent):
    worker_filter: WorkerFilter | None = None


@dataclass
class GetWorkerStatisticsEvent(BaseEvent):
    worker_filter: WorkerFilter
