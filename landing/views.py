from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
import time
from .forms import SabscribersForm


def landing(request):
    name = "CoderMax"
    #current_day = "22.02.2020"
    #current_day = datetime.datetime.today()
    #print(current_day.strftime("%m/%d/%Y"))
    form = SabscribersForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        new_form = form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'landing/landing.html', locals())


def home(request):
    return render(request, 'landing/home.html', locals())
