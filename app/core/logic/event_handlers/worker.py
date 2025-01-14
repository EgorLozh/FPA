from django.db.models import Prefetch, Q
from core.infra.models.mark import Mark
from core.logic.event_handlers.base import BaseEventHandler
from core.domain.entities.worker import Worker
from core.infra.models.worker import Worker as WorkerModel
from core.infra.models.department import Department as DepartmentModel
from core.domain.events.worker import CreateWorkerEvent, GetWorkersEvent, GetWorkerStatisticsEvent


class CreateWorkerEventHandler(BaseEventHandler):
    def __call__(self, event: CreateWorkerEvent):
        department = DepartmentModel.objects.get(id=event.department_id) if event.department_id is not None else None
        worker_model = WorkerModel(name=event.name, department=department)
        worker_model.save()

        return worker_model.to_entity()
    

class GetWorkersEventHandler(BaseEventHandler):
    def __call__(self, event: GetWorkersEvent):
        q = Q()
        if event.worker_filter is not None:
            if event.worker_filter.id is not None:
                q = q & Q(id=event.worker_filter.id)
            if event.worker_filter.department_id is not None:
                q = q & Q(department__id=event.worker_filter.department_id)
            if event.worker_filter.worker_name is not None:
                q = q & Q(name__contains=event.worker_filter.worker_name)
        workers = WorkerModel.objects.filter(q)
        return [worker.to_entity() for worker in workers]
    

class GetWorkerStatisticsEventHandler(BaseEventHandler):
    def __call__(self, event: GetWorkerStatisticsEvent):
        worker_id = event.worker_id
        worker = WorkerModel.objects.prefetch_related(
            Prefetch('mark_set', queryset=Mark.objects.select_related('script_action', 'script_action__script'))
        ).get(id=worker_id)

        result = {
            "worker_id": worker.id,
            "dates": []
        }

        for mark in worker.mark_set.all():

            scripts = []
            script_actions = mark.script_action

            actions = [{
                "id": script_action.id,
                "weight": script_action.weight,
                "text": script_action.text,
            } for script_action in script_actions]

            scripts.append({
                "script_id": script_actions.script.id,
                "actions": actions,
            })

            result['dates'].append({
                "date": mark.date,
                "scripts": scripts
            })

        return result
        