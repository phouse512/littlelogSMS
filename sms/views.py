from django.shortcuts import redirect
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
        form = SignupAliasForm()
        return render(request, "index.html", {'form': form})

    form = SignupAliasForm(request.POST)

    if not form.is_valid():
        return render(request, "index.html", {'form': form})

    if LittleLogAlias.objects.filter(alias=form.cleaned_data['alias']).exists():
        return HttpResponse("alias already exists, please choose another")


    new_alias = LittleLogAlias(alias=form.cleaned_data['alias'], email_secret=form.cleaned_data['email_secret'])
    new_alias.save()

    print new_alias

    return redirect("success/", alias=new_alias.alias)
    # except Exception:
    #     return HttpResponse("could not create account")


def success(request, alias=None):
    return render(request, "success.html", {'alias': alias})



#
# def handleTwilio(request):
#     resp = Response()
#     resp.redirect("create path to ")
#
# def updateLog(request):
#
#     body