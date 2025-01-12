from core.domain.entities.base import BaseEntity


class Request(BaseEntity):
    video: 'Video'
    script: 'Script'
    worker: 'Worker'

from core.domain.entities.video import Video
from core.domain.entities.worker import Worker
from core.domain.entities.script import Script