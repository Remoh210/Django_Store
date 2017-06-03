from django.shortcuts import render
from .forms import SubscriberForm
from .models import *


def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        new_form = form.save()
        form = SubscriberForm()
    return render(request, 'landing.html', locals())
