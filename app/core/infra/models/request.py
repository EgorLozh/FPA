from django.db import models

from core.infra.models.video import Video
from core.infra.models.script import Script
from core.infra.models.worker import Worker

from core.domain.entities.request import Request as RequestEntity


class Request(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def to_entity(self):
        return RequestEntity(id=self.pk, 
                             video=self.video.to_entity(), 
                             script=self.script.to_entity(), 
                             worker=self.worker.to_entity())
