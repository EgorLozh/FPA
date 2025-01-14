from datetime import datetime
from ninja import Schema


class CreateWorker(Schema):
    name: str
    departement_id: int | None = None

class ResponseWorker(Schema):
    id: int
    name: str
    departement_id: int | None = None

class WorkerFilterSchema(Schema):
    id: int | None = None
    worker_name: str | None = None
    department_id: int | None = None


class ScriptActionSchema(Schema):
    script_action_id: int
    weight: float

class ScriptSchema(Schema):
    script_id: int
    actions: list[ScriptActionSchema]

class DateSchema(Schema):
    date: datetime
    scripts: list[ScriptSchema]

class WorkerGetStatisticsSchema(Schema):
    worker_id : int
    dates: list[DateSchema]