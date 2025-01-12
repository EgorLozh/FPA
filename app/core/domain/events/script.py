from dataclasses import dataclass
from typing import List, Tuple

from core.domain.filters.script import ScriptFilter
from core.domain.events.base import BaseEvent


@dataclass
class CreateScript(BaseEvent):
    name: str
    actions: List[Tuple[str, float]]


@dataclass
class GetScripts(BaseEvent):
    script_filter: ScriptFilter
