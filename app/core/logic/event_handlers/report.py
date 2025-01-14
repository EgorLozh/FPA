from core.logic.event_handlers.base import BaseEventHandler
from core.domain.events.report import CreateRequestEvent, GetReportEvent
from core.domain.entities.report import Report
from core.domain.filters.report import ReportFilter
from core.domain.entities.request import Request
from core.infra.models.request import (Request as RequestModel, 
    Video as VideoModel, Script as ScriptModel, Worker as WorkerModel)
from core.infra.models.report import Report as ReportModel


class CreateRequestEventHandler(BaseEventHandler):
    def __call__(self, event: CreateRequestEvent)-> Request:
        video_model = VideoModel(url=event.video_url)
        video_model.save()

        script_model = ScriptModel.objects.get(id=event.script_id)

        worker_model = WorkerModel.objects.get(id=event.worker_id)

        request_model = RequestModel(video=video_model, script=script_model, worker=worker_model)
        request_model.save()

        return request_model.to_entity()


class GetReportEventHandler(BaseEventHandler):
    def __call__(self, event: GetReportEvent)-> Report:
        if event.report_filter is not None:
            if event.report_filter.request_id is not None:
                report_model = ReportModel.objects.get(id=event.report_filter.request_id)
                return report_model.to_entity()
            
        return None
