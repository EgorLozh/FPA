from dataclasses import dataclass
from core.domain.events.base import BaseEvent


@dataclass
class CreateDepartmentEvent(BaseEvent):
    name: str
    description: str | None
