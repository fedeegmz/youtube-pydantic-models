from enum import Enum


DEFAULT_LIMIT_PER_DAY = 10000


class Quotas(Enum):
    SEARCH = 100
    LIST_CHANNEL = 1
    LIST_PLAYLIST = 1
    LIST_VIDEO = 1
