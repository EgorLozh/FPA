from ninja import Router, Query

from core.domain.filters.worker import WorkerFilter
from core.domain.entities.worker import Worker
from core.domain.events.worker import CreateWorkerEvent, GetWorkersEvent, GetWorkerStatisticsEvent
from core.logic.container import get_container
from core.logic.mediator import Mediator
from core.application.schemas.worker import (CreateWorker, 
    ResponseWorker, WorkerFilterSchema, WorkerGetStatisticsSchema, DateSchema, ScriptSchema, ScriptActionSchema)

worker_router = Router()


@worker_router.post("/", response=ResponseWorker)
def create_worker(request, worker_data: CreateWorker):
    container = get_container()
    mediator: Mediator = container.resolve(Mediator)
    event = CreateWorkerEvent(
        name=worker_data.name, 
        department_id=worker_data.departement_id
    )
    worker, *_ = mediator.handle(event)
    response = ResponseWorker(id=worker.id, 
                              name=worker.name, 
                              departement_id=worker.department.id if worker.department is not None else None)
    return response


@worker_router.get("/", response=list[ResponseWorker])
def get_workers(request, filter_data: Query[WorkerFilterSchema] = None):
    container = get_container()
    mediator: Mediator = container.resolve(Mediator)
    filter = WorkerFilter(id=filter_data.id, 
                                               worker_name=filter_data.worker_name, 
                                               department_id=filter_data.department_id)
    event = GetWorkersEvent(worker_filter=filter)
    workers, *_ = mediator.handle(event)
    response = [ResponseWorker(id=worker.id, 
                               name=worker.name, 
                               departement_id=worker.department.id if worker.department is not None else None) 
                               for worker in workers]
    return response

@worker_router.get("{worker_id}/statistics", response=WorkerGetStatisticsSchema)
def get_workers_statistics(request, worker_id: int):
    container = get_container()
    mediator: Mediator = container.resolve(Mediator)
    event = GetWorkerStatisticsEvent(worker_id=worker_id)
    #TODO serialize returned value
    dict_value, *_ = mediator.handle(event)
    
    return WorkerGetStatisticsSchema.model_validate(dict_value)