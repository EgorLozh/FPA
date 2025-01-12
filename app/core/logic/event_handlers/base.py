from abc import ABC, abstractmethod
from dataclasses import dataclass

from core.domain.events.base import BaseEvent


@dataclass
class BaseEventHandler(ABC):
    @abstractmethod
    def __call__(self, event: BaseEvent):
        ...
