from django.conf.urls import url

from sms import views

urlpatterns = [
    url(r'^success/$', views.success, name='success'),
    url(r'^$', views.index, name='index'),
    url(r'^api/_send_log/$', views.send_log, name='send_log'),
    url(r'^api/_handle_twilio/$', views.handle_twilio, name='handle_twilio')
]