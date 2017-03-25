import unittest

from pyvdp.visadirect.fundstransfer.data import ReverseFundsTransaction


class TestReverseTransaction(unittest.TestCase):

    def test_hasSystemsTraceAuditNumber(self):
        t = ReverseFundsTransaction(stan=123456, ode=object)
        self.assertTrue(hasattr(t, 'systemsTraceAuditNumber'))

    def test_hasOriginalDataElements(self):
        t = ReverseFundsTransaction(stan=123456, ode=object)
        self.assertTrue(hasattr(t, 'originalDataElements'))

    def test_hasSenderPrimaryAccountNumber(self):
        t = ReverseFundsTransaction(stan=123456, ode=object, sender_pan='1234567812345678')
        self.assertTrue(hasattr(t, 'senderPrimaryAccountNumber'))

    def test_hasSenderCardExpiryDate(self):
        t = ReverseFundsTransaction(stan=123456, ode=object, sender_card_expiry_date='12/12')
        self.assertTrue(hasattr(t, 'senderCardExpiryDate'))

    def test_hasSenderCurrencyCode(self):
        t = ReverseFundsTransaction(stan=123456, ode=object, sender_currency_code='USD')
        self.assertTrue(hasattr(t, 'senderCurrencyCode'))

    def test_hasAmount(self):
        t = ReverseFundsTransaction(stan=123456, ode=object, amount=123.45)
        self.assertTrue(hasattr(t, 'amount'))

    def test_hasTransactionIdentifier(self):
        t = ReverseFundsTransaction(stan=123456, ode=object, transaction_identifier='12345')
        self.assertTrue(hasattr(t, 'transactionIdentifier'))

    def test_hasCardAcceptor(self):
        t = ReverseFundsTransaction(stan=123456, ode=object, card_acceptor=object)
        self.assertTrue(hasattr(t, 'cardAcceptor'))
