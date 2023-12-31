#!/usr/bin/python3
"shebang"

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    "class base"

    def __init__(self, *args, **kwargs):
        "instantation"
        if not kwargs or len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if "id" not in kwargs.keys():
                    self.id == str(uuid4())
                if "created_at" not in kwargs.keys():
                    self.created_at = datetime.now()
                if "updated_at" not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, k, v)

    def __str__(self):
        "string replication"
        return (
            f"[BaseModel] ({self.id}) ({self.created_at}) {self.__dict__}"
        )

    def save(self):
        "save function"
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        "return dict"
        dict = self.__dict__
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
