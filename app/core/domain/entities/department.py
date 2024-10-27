from dataclasses import dataclass

from core.domain.entities.base import BaseEntity


@dataclass
class Department(BaseEntity):
    name: str
    description: str | None = None
    workers: list['Worker'] | None = None

from core.domain.entities.worker import Worker