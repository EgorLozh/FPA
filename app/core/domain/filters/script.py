from core.domain.filters.base import BaseFilter


class ScriptFilter(BaseFilter):
    text_pieces: str | None = None
