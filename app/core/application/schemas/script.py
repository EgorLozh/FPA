from ninja import Schema


class ScriptActionSchema(Schema):
    text: str
    weight: float


class CreateScriptSchema(Schema):
    name: str
    actions: list[ScriptActionSchema]


class ResponseScriptSchema(Schema):
    id: int
    name: str
    actions: list[ScriptActionSchema]

class ScriptFilterSchema(Schema):
    id: int | None = None
    name: str | None = None
    text_piece: str | None = None

