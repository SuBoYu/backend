from django.db import models


# Create your models here.
class Experience:
    id: int
    name: str
    location: str
    details: list
    duration: str
