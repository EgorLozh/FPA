from app.core.domain.events.base import BaseEvent
from app.core.domain.filters.report import ReportFilter


class CreateRequest(BaseEvent):
    video_url: str
    script_id: int
    worker_id: int


class GetReport(BaseEvent):
    report_filter: ReportFilter | None = None
