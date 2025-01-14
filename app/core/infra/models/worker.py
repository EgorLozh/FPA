from django.db import models

from core.infra.models.department import Department
from core.domain.entities.worker import Worker as WorkerEntity


class Worker(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def to_entity(self):
        department = self.department.to_entity() if self.department is not None else None
        return WorkerEntity(id=self.pk, name=self.name, department=department)    
