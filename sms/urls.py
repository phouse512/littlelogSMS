from django.conf.urls import url

from sms import views

urlpatterns = [
    url(r'^success/$', views.success, name='success'),
    url(r'^$', views.index, name='index')
]