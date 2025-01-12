from abc import ABC
from dataclasses import dataclass, field


@dataclass
class BaseEntity(ABC):
    id: int | None = field(kw_only=True)
