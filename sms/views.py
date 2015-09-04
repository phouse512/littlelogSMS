from django.shortcuts import render
from django.http import HttpResponse

from sms.forms import SignupAliasForm
from sms.models import LittleLogHistory
from sms.models import LittleLogAlias

from twilio.rest import TwilioRestClient
from twilio.twiml import Response

# Create your views here.


def index(request):

    if request.method == 'GET':
        return render(request, "index.html")

    form = SignupAliasForm(request.POST)

    if not form.is_valid():
        return HttpResponse("failure")

    if LittleLogAlias.objects.filter(alias=form.cleaned_data['alias']).exists():
        return HttpResponse("alias already exists, please choose another")

    try:
        new_alias = LittleLogAlias(
            alias=form.cleaned_data['alias'],
            email_secret=form.cleaned_data['email_secret'],
        ).save()
    except Exception:
        return HttpResponse("could not create account")


#
# def handleTwilio(request):
#     resp = Response()
#     resp.redirect("create path to ")
#
# def updateLog(request):
#
#     body