from dataclasses import dataclass
from core.domain.filters.base import BaseFilter


@dataclass
class ScriptFilter(BaseFilter):
    name: str | None = None
    text_piece: str | None = None
