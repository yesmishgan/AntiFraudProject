from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from fraud_monitor.models import FraudMonitor


def index(request):
    #t = loader.get_template("template/fraud_monitor/index.html")
    return render(
        request,
        './fraud_monitor/index.html')
