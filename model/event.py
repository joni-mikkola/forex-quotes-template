from enum import Enum
import string


class EventType(Enum):
    LOGIN = 0,
    QUOTE = 1


class Event:
    def __init__(self, type: EventType, value: string = ""):
        self.type = type
        self.value = value
