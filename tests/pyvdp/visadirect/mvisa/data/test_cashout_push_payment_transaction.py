import unittest

from pyvdp.visadirect.mvisa.data import CashoutPushPaymentTransaction


class TestCashoutPushPaymentTransaction(unittest.TestCase):

    def test_hasSystemsTraceAuditNumber(self):
        cppt = CashoutPushPaymentTransaction(stan=123456)
        self.assertTrue(hasattr(cppt, 'systemsTraceAuditNumber'))

    def test_hasAmount(self):
        cppt = CashoutPushPaymentTransaction(stan=123456, amount=123.45)
        self.assertTrue(hasattr(cppt, 'amount'))

    def test_hasRecipientPrimaryAccountNumber(self):
        cppt = CashoutPushPaymentTransaction(stan=123456, recipient_pan='1234567812345678')
        self.assertTrue(hasattr(cppt, 'recipientPrimaryAccountNumber'))

    def test_hasTransactionCurrencyCode(self):
        cppt = CashoutPushPaymentTransaction(stan=123456, transaction_currency_code='USD')
        self.assertTrue(hasattr(cppt, 'transactionCurrencyCode'))

    def test_hasSenderName(self):
        cppt = CashoutPushPaymentTransaction(stan=123456, sender_name='John Doe')
        self.assertTrue(hasattr(cppt, 'senderName'))

    def test_hasSenderAccountNumber(self):
        cppt = CashoutPushPaymentTransaction(stan=123456, sender_account_number='1234567812345678')
        self.assertTrue(hasattr(cppt, 'senderAccountNumber'))

    def test_hasCardAcceptor(self):
        cppt = CashoutPushPaymentTransaction(stan=123456, card_acceptor=object)
        self.assertTrue(hasattr(cppt, 'cardAcceptor'))

    def test_hasAcquiringBin(self):
        cppt = CashoutPushPaymentTransaction(stan=123456)
        self.assertTrue(hasattr(cppt, 'acquiringBin'))

    def test_hasAcquirerCountryCode(self):
        cppt = CashoutPushPaymentTransaction(stan=123456)
        self.assertTrue(hasattr(cppt, 'acquirerCountryCode'))

    def test_hasBusinessApplicationId(self):
        cppt = CashoutPushPaymentTransaction(stan=123456)
        self.assertTrue(hasattr(cppt, 'businessApplicationId'))