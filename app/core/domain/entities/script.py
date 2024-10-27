from dataclasses import dataclass

from core.domain.entities.base import BaseEntity


@dataclass
class Script(BaseEntity):
    name: str
    actions: list['ScriptAction'] | None = None


@dataclass
class ScriptAction(BaseEntity):
    text: str
    weight: float
    script: 'Script' | None = None
