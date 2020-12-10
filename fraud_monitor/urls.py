from django.conf.urls import url

from . import views

app_name = 'fraud_monitor'

urlpatterns = [
    url('', views.index, name='index'),
]
