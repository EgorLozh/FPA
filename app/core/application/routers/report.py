from ninja import Router

from core.domain.events.report import GetReport
from core.domain.filters.report import ReportFilter
from core.logic.container import get_container
from core.logic.mediator import Mediator
from core.application.schemas.report import ReportFilterSchema, ResponseReportSchema, MarkSchema


report_router = Router()

@report_router.get('/report', response=ResponseReportSchema)
def get_report(request, filter_data: ReportFilterSchema = None):
    container = get_container()
    mediator: Mediator = container.resolve(Mediator)
    filter = ReportFilter(request_id=filter_data.request_id)
    event = GetReport(report_filter=filter)
    report, *_ = mediator.handle(event)
    response = ResponseReportSchema(id=report.id, 
                                    marks=[MarkSchema(script_action_id=mark.script_action.id, 
                                                      weight=mark.script_action.weight, 
                                                      chek=mark.chek) for mark in report.marks])
    return response