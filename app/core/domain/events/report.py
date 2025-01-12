from dataclasses import dataclass
from core.domain.events.base import BaseEvent
from core.domain.filters.report import ReportFilter


@dataclass
class CreateRequest(BaseEvent):
    video_url: str
    script_id: int
    worker_id: int


@dataclass
class GetReport(BaseEvent):
    report_filter: ReportFilter | None = None
