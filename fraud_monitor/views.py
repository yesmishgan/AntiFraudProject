# Copyright 2020 Mikhail Dolbnin dolbnin.n@gmail.com

import json
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from .models import Transaction


def index(request):
    last_transaction = Transaction.objects.all()[::-1]
    return render(
        request,
        './fraud_monitor/index.html',
        {'last_transaction' : last_transaction}
        )


def upload(request):
    if request.method == "POST":
        data = request.body.decode('utf8')
        data = json.loads(data)
        element = Transaction(TransactionID = data['id'],
                            TransactionAmt = data['amt'],
                            Card1 = data['card1'],
                            Card2 = data['card2'],
                            isFraud = data['fraud'],
                            Card6 = data['card6']
        )
        element.save()
        print(element, " is saved")
        return HttpResponse(str(element) +" is saved")
    else:
        return HttpResponse("no")


def stats(request):
    last_transaction = Transaction.objects.all()
    legal = len(last_transaction.filter(isFraud = False))
    fraud = len(last_transaction.filter(isFraud = True))
    return render(
    request,
    './fraud_monitor/stats.html',
    {'legal' : legal, 'fraud' : fraud}
    )
