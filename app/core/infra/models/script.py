from django.db import models


class Script(models.Model):
    name = models.CharField(max_length=255)


class ScriptAction(models.Model):
    text = models.CharField(max_length=255)
    weight = models.FloatField()
    script = models.ForeignKey(Script, on_delete=models.SET_NULL, null=True, blank=True)
