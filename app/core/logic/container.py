from punq import Container, Scope

from functools import lru_cache

from core.logic.mediator import Mediator


@lru_cache
def get_container() -> Container:
    return init_container()

def init_container() -> Container:
    container = Container()
    
    init_mediator(container)
    
    return container

def init_mediator(container: Container) -> None:
    container.register(Mediator, scope=Scope.singleton)
