from django.core.mail import send_mail
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from smtplib import SMTPException

from sms.forms import SignupAliasForm
from sms.models import LittleLogHistory
from sms.models import LittleLogAlias
from sms.processor import MessageProcessor
from sms.response import TextResponse

import logging
logger = logging.getLogger(__name__)

# Create your views here.

SAFE_ALIASES = ["feedback", "help"]

def index(request):

    if request.method == 'GET':
        form = SignupAliasForm()
        return render(request, "index.html", {'form': form})

    form = SignupAliasForm(request.POST)

    if not form.is_valid():
        return render(request, "index.html", {'form': form})

    alias_text = form.cleaned_data['alias'].lower()

    ### catch safewords
    if alias_text in SAFE_ALIASES:
        logger.info("Reserved alias attempted signup")
        return HttpResponse("that alias is reserved for special commands")

    if LittleLogAlias.objects.filter(alias=alias_text).exists():
        return HttpResponse("alias already exists, please choose another")

    new_alias = LittleLogAlias(alias=alias_text, email_secret=form.cleaned_data['email_secret'])
    new_alias.save()

    return redirect("success/%s" % new_alias.alias)


def success(request, alias):
    return render(request, "success.html", {'alias': alias})


@csrf_exempt
@require_POST
def handle_twilio(request):

    message = request.POST['Body']
    response = MessageProcessor(message).handle()
    return HttpResponse(response, content_type="text/xml")


@csrf_exempt
@require_POST
def test_processor(request):

    message = request.POST['Body']
    response = MessageProcessor(message).handle()
    return HttpResponse(response, content_type="text/xml")