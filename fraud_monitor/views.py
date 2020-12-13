import json
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from .models import Transaction


def index(request):
    print(request.body)
    last_transaction = Transaction.objects.all()[::-1]
    print(last_transaction)
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
