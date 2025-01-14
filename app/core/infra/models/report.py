from django.db import models

from core.infra.models.request import Request

from core.domain.entities.report import Report as ReportEntity


class Report(models.Model):
    request = models.ForeignKey(Request, on_delete=models.SET_NULL, null=True, blank=True)

    def to_entity(self):
        request = self.request.to_entity()
        marks = [mark.to_entity() for mark in self.marks.all()]
        return ReportEntity(request=self.request.to_entity(), marks=marks)