from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from core.domain.entities.base import BaseEntity


@dataclass
class Mark(BaseEntity):
    date: datetime
    chek: bool
    worker: Optional['Worker'] = None
    scriptAction: Optional['ScriptAction'] = None
    
from core.domain.entities.script import ScriptAction
from core.domain.entities.worker import Worker