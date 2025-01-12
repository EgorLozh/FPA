from ninja import Router, Query

from core.domain.filters.script import ScriptFilter
from core.domain.events.script import CreateScript, GetScripts
from core.logic.container import get_container
from core.logic.mediator import Mediator
from core.application.schemas.script import CreateScriptSchema, ResponseScriptSchema, ScriptActionSchema, ScriptFilterSchema


script_router = Router()


@script_router.post("/", response=ResponseScriptSchema)
def create_script(request, script_data: CreateScriptSchema):
    container = get_container()
    mediator: Mediator = container.resolve(Mediator)
    event = CreateScript(name=script_data.name, 
                         actions=[(script_action.text, script_action.weight) for script_action in script_data.actions])
    script, *_ = mediator.handle(event)
    response = ResponseScriptSchema(id=script.id, 
                                    name=script.name, 
                                    actions=[ScriptActionSchema(text=script_action.text, weight=script_action.weight) 
                                             for script_action in script.actions])
    return response


@script_router.get("/", response=list[ResponseScriptSchema])
def get_scripts(request, filter_data: Query[ScriptFilterSchema] = None):
    container = get_container()
    mediator: Mediator = container.resolve(Mediator)
    filter = ScriptFilter(id=filter_data.id, 
                          name=filter_data.name, 
                          text_piece=filter_data.text_piece)
    event = GetScripts(script_filter=filter)
    scripts, *_ = mediator.handle(event)
    response = [ResponseScriptSchema(id=script.id, 
                                     name=script.name,
                                     actions=[ScriptActionSchema(text=script_action.text, weight=script_action.weight) 
                                              for script_action in script.actions]) for script in scripts]
    return response