from dataclasses import dataclass
from core.domain.events.base import BaseEvent
from core.domain.filters.report import ReportFilter


@dataclass
class CreateRequestEvent(BaseEvent):
    video_url: str
    script_id: int
    worker_id: int


@dataclass
class GetReportEvent(BaseEvent):
    report_filter: ReportFilter | None = None
