from abc import ABC
from dataclasses import dataclass


@dataclass
class BaseEntity(ABC):
    id: int | None = None
