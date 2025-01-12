from ninja import Schema


class ReportFilterSchema(Schema):
    request_id: int


class MarkSchema(Schema):
    script_action_id: int
    weight: float
    chek: bool


class ResponseReportSchema(Schema):
    id: int
    marks: list[MarkSchema]