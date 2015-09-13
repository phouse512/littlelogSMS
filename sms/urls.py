from django.conf.urls import url

from sms import views

urlpatterns = [
    url(r'^success/(?P<alias>[-A-Za-z0-9_]+)$', views.success, name='success'),
    url(r'^$', views.index, name='index'),
    url(r'^api/_handle_twilio/$', views.handle_twilio, name='handle_twilio'),
    url(r'^test_processor/$', views.test_processor, name='test_processor')
]