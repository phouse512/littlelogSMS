from django.shortcuts import render
from django.http import HttpResponse

from sms.forms import SignupAliasForm
from sms.models import LittleLogHistory
from sms.models import LittleLogAlias

# Create your views here.


def index(request):

    #

    if request.method == 'GET':
        return HttpResponse("this is the screen you should see to register")

    form = SignupAliasForm(request.POST)

    if not form.is_valid():
        return HttpResponse("failure")

    if LittleLogAlias.objects.filter(alias=form.cleaned_data['alias']).exists():
        return HttpResponse("alias already exists, please choose another")

    new_alias = LittleLogAlias(
        alias=form.cleaned_data['alias'],
        email_secret=form.cleaned_data['email_secret'],
    ).save()
