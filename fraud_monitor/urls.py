from django.conf.urls import url
from django.urls import path, include
from django.views.generic import RedirectView

from . import views

app_name = 'fraud_monitor'

urlpatterns = [
    url('', views.index, name='index'),
]