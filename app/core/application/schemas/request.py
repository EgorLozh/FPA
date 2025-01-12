from ninja import Schema


class CreateRequestSchema(Schema):
    worker_id: int
    script_id: int
    video_url: str

class ResponseRequestSchema(Schema):
    id: int
    worker_id: int
    script_id: int
    video_url: str