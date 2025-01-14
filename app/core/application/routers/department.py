from ninja import Query, Router

from core.domain.filters.department import DepartmentFilter
from core.application.schemas.department import CreateDepartment, ResponseDepartment, WorkerInDepartment, QueryDepartment
from core.domain.events.department import CreateDepartmentEvent, GetDepartmentsEvent
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

@department_router.get("/", response=list[ResponseDepartment])
def get_departments(request, filter_data: Query[QueryDepartment] = None):
    container = get_container()
    mediator: Mediator = container.resolve(Mediator)
    filter: DepartmentFilter = DepartmentFilter(name=filter_data.name, id=filter_data.id)
    event = GetDepartmentsEvent(department_filter=filter)
    departments, *_ = mediator.handle(event)
    response = [ResponseDepartment(id=department.id, 
                                   name=department.name, 
                                   description=department.description, 
                                   workers=[WorkerInDepartment(id=worker.id, name=worker.name) for worker in department.workers]) for department in departments]
    return response