from ninja import Schema


class CreateRequestSchema(Schema):
    worker_id: int
    script_id: int
    video_url: str

class ScriptActionSchema(Schema):
    id: int
    weight: float
    text: str

class ResponseRequestSchema(Schema):
    id: int
    actions: list[ScriptActionSchema]
    worker_id: int
    script_id: int
    video_url: str
