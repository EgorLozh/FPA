from dataclasses import dataclass, field


@dataclass
class BaseFilter:
    id: int | None = field(kw_only=True)
