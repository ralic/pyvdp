import unittest

from pyvdp.visadirect.mvisa.data import CashinPushPaymentTransaction


class TestCashinPushPaymentTransaction(unittest.TestCase):

    def test_hasSystemsTraceAuditNumber(self):
        cppt = CashinPushPaymentTransaction(stan=123456)
        self.assertTrue(hasattr(cppt, 'systemsTraceAuditNumber'))

    def test_hasAmount(self):
        cppt = CashinPushPaymentTransaction(stan=123456, amount=123.45)
        self.assertTrue(hasattr(cppt, 'amount'))

    def test_hasRecipientPrimaryAccountNumber(self):
        cppt = CashinPushPaymentTransaction(stan=123456, recipient_pan='1234567812345678')
        self.assertTrue(hasattr(cppt, 'recipientPrimaryAccountNumber'))

    def test_hasTransactionCurrencyCode(self):
        cppt = CashinPushPaymentTransaction(stan=123456, transaction_currency_code='USD')
        self.assertTrue(hasattr(cppt, 'transactionCurrencyCode'))

    def test_hasSenderName(self):
        cppt = CashinPushPaymentTransaction(stan=123456, sender_name='John Doe')
        self.assertTrue(hasattr(cppt, 'senderName'))

    def test_hasSenderAccountNumber(self):
        cppt = CashinPushPaymentTransaction(stan=123456, sender_account_number='12345667812345678')
        self.assertTrue(hasattr(cppt, 'senderAccountNumber'))

    def test_hasCardAcceptor(self):
        cppt = CashinPushPaymentTransaction(stan=123456, card_acceptor=object)
        self.assertTrue(hasattr(cppt, 'cardAcceptor'))
