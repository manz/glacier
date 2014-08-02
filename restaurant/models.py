from django.db import models
from django.db.models.fields import DateField, TextField


class Event(models.Model):
    posted = DateField()
    title = TextField()
    content = TextField()