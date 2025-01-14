from punq import Container, Scope

from functools import lru_cache

from core.logic.mediator import Mediator

from core.domain.events.department import CreateDepartmentEvent
from core.domain.events.worker import CreateWorkerEvent, GetWorkersEvent, GetWorkerStatisticsEvent
from core.domain.events.report import GetReportEvent, CreateRequestEvent
from core.domain.events.script import CreateScript, GetScripts

from core.logic.event_handlers.department import CreateDepartmentEventHandler
from core.logic.event_handlers.worker import CreateWorkerEventHandler, GetWorkersEventHandler, GetWorkerStatisticsEventHandler
from core.logic.event_handlers.report import GetReportEventHandler, CreateRequestEventHandler
from core.logic.event_handlers.script import CreateScriptEventHandler, GetScriptsEventHandler


@lru_cache
def get_container() -> Container:
    return init_container()

def init_container() -> Container:
    container = Container()
    
    init_mediator(container)
    
    return container

def init_mediator(container: Container) -> None:
    container.register(Mediator, scope=Scope.singleton)

    mediator: Mediator = container.resolve(Mediator)
    mediator.register(CreateDepartmentEvent, CreateDepartmentEventHandler())
    mediator.register(CreateWorkerEvent, CreateWorkerEventHandler())
    mediator.register(GetWorkersEvent, GetWorkersEventHandler())
    mediator.register(GetWorkerStatisticsEvent, GetWorkerStatisticsEventHandler())
    mediator.register(GetReportEvent, GetReportEventHandler())
    mediator.register(CreateRequestEvent, CreateRequestEventHandler())
    mediator.register(CreateScript, CreateScriptEventHandler())
    mediator.register(GetScripts, GetScriptsEventHandler())

