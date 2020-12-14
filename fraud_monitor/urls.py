# Copyright 2020 Mikhail Dolbnin dolbnin.n@gmail.com

from django.conf.urls import url
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

app_name = 'fraud_monitor'

urlpatterns = [
    url('upload/', views.upload, name='upload'),
    url(r'^$', views.index, name='index'),
]
