from django.conf.urls import url

from . import views

app_name = 'fraud_monitor'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]