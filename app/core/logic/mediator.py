from dataclasses import dataclass, field
from typing import Generator
from core.domain.events.base import BaseEvent
from core.logic.event_handlers.base import BaseEventHandler


@dataclass
class Mediator:
    event_handlers: dict[type[BaseEvent], list[BaseEventHandler]] = field(default_factory=dict)

    def register(self, event_type: type[BaseEvent], handler: BaseEventHandler) -> None:
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)

    def handle(self, event: BaseEvent) -> Generator:
        if type(event) not in self.event_handlers:
            raise ValueError(f'No handlers registered for event type {type(event)}')
        for handler in self.event_handlers[type(event)]:
            yield handler(event)
