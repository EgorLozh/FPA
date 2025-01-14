from dataclasses import dataclass
from core.domain.filters.base import BaseFilter


@dataclass
class ReportFilter(BaseFilter):
    request_id: int | None = None
