from django.db.models import Q
from core.infra.models.script import Script, ScriptAction
from core.domain.entities.script import Script as ScriptEntity
from core.domain.events.script import CreateScript, GetScripts
from core.logic.event_handlers.base import BaseEventHandler


class CreateScriptEventHandler(BaseEventHandler):
    def __call__(self, event: CreateScript) -> ScriptEntity:
        model = Script(name=event.name)
        model.save()
        for text, weight in event.actions:
            ScriptAction(text=text, weight=weight, script=model).save()
        return model.to_entity()
    

class GetScriptsEventHandler(BaseEventHandler):
    def __call__(self, event: GetScripts) -> list[ScriptEntity]:
        q = Q()
        if event.script_filter.id is not None:
            q = q & Q(id=event.script_filter.id)
        if event.script_filter.name is not None:
            q = q & Q(name=event.script_filter.name)
        if event.script_filter.text_piece is not None:
            q = q & Q(actions__text__contains=event.script_filter.text_piece)
        scripts = Script.objects.all()
        return [script.to_entity() for script in scripts]