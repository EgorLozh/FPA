from django.db import models

from core.infra.models.script import ScriptAction
from core.infra.models.worker import Worker
from core.infra.models.report import Report
from core.domain.entities.mark import Mark as MarkEntity

class Mark(models.Model):
    date = models.DateTimeField()
    chek = models.BooleanField()
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True)
    script_action = models.ForeignKey(ScriptAction, on_delete=models.SET_NULL, null=True, blank=True)
    report = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True, blank=True, related_name='marks')
    
    def to_entity(self):
        Worker = self.worker.to_entity() if self.worker is not None else None
        ScriptAction = self.script_action.to_entity() if self.script_action is not None else None
        return MarkEntity(id=self.pk, date=self.date, chek=self.chek, worker=Worker, script_action=ScriptAction)