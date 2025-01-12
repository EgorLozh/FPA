from ninja import Router

from core.application.schemas.department import CreateDepartment, ResponseDepartment, WorkerInDepartment
from core.domain.events.department import CreateDepartmentEvent
from core.logic.container import get_container
from core.logic.mediator import Mediator

department_router = Router()

@department_router.post("/", response=ResponseDepartment)
def create_department(request, department_data: CreateDepartment):
    container = get_container()
    mediator: Mediator = container.resolve(Mediator)
    event = CreateDepartmentEvent(name=department_data.name, description=department_data.description)
    department, *_ = mediator.handle(event)
    response = ResponseDepartment(id=department.id, 
                                  name=department.name, 
                                  description=department.description, 
                                  workers=[WorkerInDepartment(id=worker.id, name=worker.name) for worker in department.workers])
    return response