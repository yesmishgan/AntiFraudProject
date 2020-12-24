from django.test import TestCase
from .models import *

class TransactionTestCase(TestCase):

    def setUp(self) -> None:
        self.tran = Transaction.objects.create(
        TransactionID='1',
        TransactionAmt=1,
        Card1=1,
        Card2=2,
        isFraud=True,
        Card6='debit'
        )

    def test_check(self):
        print()
        print("TESTS CORRECT")
        self.assertEqual(1, 1)
        print("OK")

    def test_add_transaction(self):
        print()
        print("TESTS ADDING TRANSACTION")
        self.assertIn(self.tran, Transaction.objects.all())
        print("OK")

    def test_get_func(self):
        print()
        print("TESTS FUNC STATUS")
        self.assertEqual(self.tran.getStatus(), True)
        print("OK")
