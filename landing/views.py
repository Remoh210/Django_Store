from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):
    name = "Remoh310"
    current_day = "05.01.2017"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():

        print(form.cleaned_data)
        new_form = form.save()
    return render(request, 'landing.html', locals())
