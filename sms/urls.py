from django.conf.urls import url

from sms import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]