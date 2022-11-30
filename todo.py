from datetime import date
from enum import Enum
from uuid import uuid4

class Status(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2

class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Item():
    creation_date = date.today()
    title = "empty"
    status = Status.NOT_STARTED
    priority = Priority.LOW
    flag = False
    url = ""
    due_date = date
    state = False
    notes = ""
    icon = ""

    def init(self, title:str=None):
        if title is not None:
            self.title = title
            self.id = str(uuid4())

    @property
    def title(self) ->str:
        """Returns the Title of the object"""
        return self.title

    @title.setter
    def title(self, value):
        self.title = value

    @property
    def priority(self):
        return self.priority.name

    @priority.setter
    def priority(self, value: Priority):
        self.priority = value

    @property
    def creation_date(self):
        return self.creation_date

    @creation_date.setter
    def creation_date(self, value):
        self.creation_date = value

    @property
    def age(self):
        return self.creation_date - date.today()

    @property
    def status(self):
        return self.status.name

    @status.setter
    def status(self, value: Status):
        self.status = value

    @property
    def id(self):
        return self.id

    @property
    def flag(self):
        return self.flag

    @flag.setter
    def flag(self, value: bool):
        self.flag = value

    @property
    def url(self):
        return self.url

    @url.setter
    def url(self, value: str):
        self.url = value

    @property
    def due_date(self):
        return self.due_date

    @due_date.setter
    def due_date(self, value: date):
        self.due_date = value

    @property
    def icon(self):
        return self.icon

    @icon.setter
    def icon(self, value: str):
        self.icon = value

    @property
    def state(self):
        return self.state

    @state.setter
    def state(self, value: bool):
        self.state = value

    @property
    def notes(self):
        return self.notes

    @notes.setter
    def notes(self, value: str):
        self.value = value

class ToDo():
    todo = []







