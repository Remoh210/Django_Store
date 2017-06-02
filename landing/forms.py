from .models import *
from django.forms import ModelForm


class SubscriberForm(ModelForm):

    class Meta:
        model = Subscriber
        exclude = [""]



