from punq import Container

from functools import lru_cache


@lru_cache
def get_container() -> Container:
    return init_container()


def init_container() -> Container:
    container = Container()

    return container
