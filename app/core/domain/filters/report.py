from core.domain.filters.base import BaseFilter


class ReportFilter(BaseFilter):
    request_id: int | None = None
