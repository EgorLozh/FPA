from core.domain.filters.base import BaseFilter


class ScriptFilter(BaseFilter):
    name: str | None = None
    text_piece: str | None = None
