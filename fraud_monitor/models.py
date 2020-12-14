# Copyright 2020 Mikhail Dolbnin dolbnin.n@gmail.com

from django.db import models

class Transaction(models.Model):
    TransactionID = models.CharField(max_length = 25)
    TransactionAmt = models.FloatField()
    Card1 = models.FloatField()
    Card2 = models.FloatField()
    isFraud = models.BooleanField(default=False)
    Card6 = models.CharField(max_length = 10)

    def __str__(self):
        return self.TransactionID
