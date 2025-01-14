from core.domain.entities.department import Department
from core.infra.models.department import Department as DepartmentModel
from core.domain.events.department import CreateDepartmentEvent
from core.logic.event_handlers.base import BaseEventHandler


class CreateDepartmentEventHandler(BaseEventHandler):
    def __call__(self, event: CreateDepartmentEvent) -> Department:
        model = DepartmentModel(
            name=event.name,
            description=event.description
        )
        model.save()
        return model.to_entity()
