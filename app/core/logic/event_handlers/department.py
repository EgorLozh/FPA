from django.db.models import Q

from core.domain.entities.department import Department
from core.infra.models.department import Department as DepartmentModel
from core.domain.events.department import CreateDepartmentEvent, GetDepartmentsEvent
from core.logic.event_handlers.base import BaseEventHandler


class CreateDepartmentEventHandler(BaseEventHandler):
    def __call__(self, event: CreateDepartmentEvent) -> Department:
        model = DepartmentModel(
            name=event.name,
            description=event.description
        )
        model.save()
        return model.to_entity()
    


class GetDepartmentsEventHandler(BaseEventHandler):
    def __call__(self, event: GetDepartmentsEvent) -> list[Department]:
        q = Q()
        if event.department_filter is not None:
            if event.department_filter.id is not None:
                q = q & Q(id=event.department_filter.id)
            if event.department_filter.name is not None:
                q = q & Q(name=event.department_filter.name)
        departments = DepartmentModel.objects.filter(q)
        return [department.to_entity() for department in departments]
