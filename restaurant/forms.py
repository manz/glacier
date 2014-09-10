from django.forms.fields import CharField, DateField
from django.forms.forms import Form


class EventForm(Form):
    title = CharField()
    content = CharField()
    posted = DateField()