from ninja import Router

from core.logic.container import get_container
from  core.logic.mediator import Mediator
from core.domain.events.report import CreateRequest
from core.application.schemas.request import CreateRequestSchema, ResponseRequestSchema


request_router = Router()

@request_router.post('/', response=ResponseRequestSchema)
def create_request(request, request_data: CreateRequestSchema):
    container = get_container()
    mediator: Mediator = container.resolve(Mediator)
    event = CreateRequest(
        video_url=request_data.video_url,
        script_id=request_data.script_id,
        worker_id=request_data.worker_id
    )
    request, *_ = mediator.handle(event)
    response = ResponseRequestSchema(
        id=request.id,
        video_url=request.video_url,
        script_id=request.script.id,
        worker_id=request.worker.id
    )
    return response
