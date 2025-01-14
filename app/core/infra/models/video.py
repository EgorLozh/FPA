from django.db import models
from core.domain.entities.video import Video as VideoEntity


class Video(models.Model):
    url = models.URLField()

    def to_entity(self):
        return VideoEntity(id=self.pk, url=self.url)
