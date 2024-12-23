from django.db import models

from core.infra.models.script import ScriptAction
from core.infra.models.worker import Worker


class Mark(models.Model):
    date = models.DateTimeField()
    chek = models.BooleanField()
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True)
    script_action = models.ForeignKey(ScriptAction, on_delete=models.SET_NULL, null=True, blank=True)
    