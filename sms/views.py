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
from sms.response import TextResponse



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

    return redirect("success/", alias=new_alias.alias)


def success(request, alias=None):
    return render(request, "success.html", {'alias': alias})



#
@csrf_exempt
@require_POST
def handle_twilio(request):

    recipient_list = ["bob.49195@mailbot.littlelogs.co"]
    from_email = "LittleLog SMS"
    subject = "test"
    message = request.POST['Body']

    response_handler = TextResponse(request.POST['From'])
    try:
        send_mail(subject, message, from_email, recipient_list)
        return response_handler.handle_success()
    except SMTPException as exception:
        return response_handler.handle_error()


#
# def updateLog(request):
#
#     body


# def send_log(request):
#
#     recipient_list = ["bob.49195@mailbot.littlelogs.co"]
#     from_email = "LittleLog SMS"
#     subject = "test"
#     message = request.POST['Body']
#
#     response_handler = TextResponse(request.POST['FROM'])
#     try:
#         send_mail(subject, message, from_email, recipient_list)
#         response_handler.handle_success()
#     except SMTPException as exception:
#         response_handler.handle_error()
#
#     return HttpResponse("sent successfully!", status=200)
