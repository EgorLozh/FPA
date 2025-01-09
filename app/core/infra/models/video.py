from django.db import models


class Video(models.Model):
    url = models.URLField()
    file_name = models.CharField(max_length=255, null=True, blank=True)
