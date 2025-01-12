from dataclasses import dataclass
from typing import Optional

from core.domain.entities.base import BaseEntity


@dataclass
class Worker(BaseEntity):
    name: str
    department: Optional['Department'] = None

from core.domain.entities.department import Department