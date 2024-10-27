from dataclasses import dataclass

from core.domain.entities.base import BaseEntity


@dataclass
class Worker(BaseEntity):
    name: str
    department: 'Department' | None = None

from core.domain.entities.department import Department