from django.db import models

from core.domain.entities.department import Department as DepartmentEntity


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def to_entity(self) -> DepartmentEntity:
        from core.infra.models.worker import Worker
        from core.domain.entities.worker import Worker as WorkerEntity
        worker_models = Worker.objects.filter(department=self)
        departament = DepartmentEntity(id=self.pk, name=self.name, description=self.description)
        workers = [WorkerEntity(id=worker.pk, name=worker.name, department=departament) for worker in worker_models]
        departament.workers = workers
        return departament