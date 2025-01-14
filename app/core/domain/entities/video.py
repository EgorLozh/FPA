from dataclasses import dataclass

from core.domain.entities.base import BaseEntity


@dataclass
class Video(BaseEntity):
    url: str
