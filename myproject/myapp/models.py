from django.db import models


# Create your models here.
class Experience:
    id: int
    name: str
    location: str
    details: list
    duration: str


class Education:
    id: int
    school: str
    degree: str
    details: list
    duration: str


class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)