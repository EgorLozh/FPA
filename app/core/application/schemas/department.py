from ninja import Schema


class CreateDepartment(Schema):
    name: str
    description: str | None = None


class WorkerInDepartment(Schema):
    id: int
    name: str

class ResponseDepartment(Schema):
    id: int
    name: str
    description: str | None = None
    workers: list[WorkerInDepartment] = []

class QueryDepartment(Schema):
    id: int | None = None
    name: str | None = None

