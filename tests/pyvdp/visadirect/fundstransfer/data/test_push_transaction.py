import unittest

from pyvdp.visadirect.fundstransfer.data import PushFundsTransaction


class TestPushTransaction(unittest.TestCase):

    def test_hasSystemsTraceAuditNumber(self):
        t = PushFundsTransaction(stan=123456)
        self.assertTrue(hasattr(t, 'systemsTraceAuditNumber'))

    def test_hasAmount(self):
        t = PushFundsTransaction(stan=123456, amount=123.45)
        self.assertTrue(hasattr(t, 'amount'))

    def test_hasTransactionCurrencyCode(self):
        t = PushFundsTransaction(stan=123456, transaction_currency_code='USD')
        self.assertTrue(hasattr(t, 'transactionCurrencyCode'))

    def test_hasSenderAccountNumber(self):
        t = PushFundsTransaction(stan=123456, sender_pan='12345678123456789')
        self.assertTrue(hasattr(t, 'senderAccountNumber'))

    def test_hasSenderName(self):
        t = PushFundsTransaction(stan=123456, sender_name='John Doe')
        self.assertTrue(hasattr(t, 'senderName'))

    def test_hasSenderAddress(self):
        t = PushFundsTransaction(stan=123456, sender_address='Elm Street')
        self.assertTrue(hasattr(t, 'senderAddress'))

    def test_hasSenderCountryCode(self):
        t = PushFundsTransaction(stan=123456, sender_country_code='USA')
        self.assertTrue(hasattr(t, 'senderCountryCode'))

    def test_hasSenderCity(self):
        t = PushFundsTransaction(stan=123456, sender_city='SFO')
        self.assertTrue(hasattr(t, 'senderCity'))

    def test_hasSenderStateCode(self):
        t = PushFundsTransaction(stan=123456, sender_state_code='CA')
        self.assertTrue(hasattr(t, 'senderStateCode'))

    def test_hasRecipientPrimaryAccountNumber(self):
        t = PushFundsTransaction(stan=123456, recipient_pan='1234567812345678')
        self.assertTrue(hasattr(t, 'recipientPrimaryAccountNumber'))

    def test_hasRecipientName(self):
        t = PushFundsTransaction(stan=123456, recipient_name='John Doe')
        self.assertTrue(hasattr(t, 'recipientName'))

    def test_hasCardAcceptor(self):
        t = PushFundsTransaction(stan=123456, card_acceptor=object)
        self.assertTrue(hasattr(t, 'cardAcceptor'))
