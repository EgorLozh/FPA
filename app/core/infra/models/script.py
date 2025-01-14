from django.db import models

from core.domain.entities.script import ScriptAction as ScriptActionEntity, Script as ScriptEntity


class Script(models.Model):
    name = models.CharField(max_length=255)

    def to_entity(self):
        script = ScriptEntity(id=self.pk, name=self.name)
        actions = ScriptAction.objects.filter(script=self)
        script.actions = [ScriptActionEntity(id=action.pk,
                                             text=action.text,
                                             weight=action.weight,
                                             script=script) for action in actions]
        return script

class ScriptAction(models.Model):
    text = models.CharField(max_length=255)
    weight = models.FloatField()
    script = models.ForeignKey(Script, on_delete=models.SET_NULL, null=True, blank=True)

    def to_entity(self):
        script = self.script.to_entity() if self.script is not None else None
        return ScriptActionEntity(text=self.text, weight=self.weight, script=script)
