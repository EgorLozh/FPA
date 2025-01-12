from core.domain.entities.base import BaseEntity


class Report(BaseEntity):
    request: 'Request'
    marks: list['Mark']

from core.domain.entities.request import Request
from core.domain.entities.mark import Mark
