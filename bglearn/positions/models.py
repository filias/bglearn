import uuid
from enum import StrEnum

from django.db import models


class Category(StrEnum):
    CUBE = "cube"
    OPENING = "opening"
    MIDDLEGAME = "middlegame"
    ENDGAME = "endgame"


class Position(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=32)
    position = models.ImageField(upload_to="positions/")
    solution = models.ImageField(upload_to="positions/")
    analysis = models.ImageField(upload_to="positions/")
