from dataclasses import dataclass
from datetime import datetime

from core.domain.entities.base import BaseEntity


@dataclass
class Mark(BaseEntity):
    date: datetime
    chek: bool
    worker: 'Worker' | None = None
    scriptAction: 'ScriptAction' | None = None
    
from core.domain.entities.script import ScriptAction
from core.domain.entities.worker import Worker