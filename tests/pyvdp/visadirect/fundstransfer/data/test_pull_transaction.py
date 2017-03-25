import unittest

from pyvdp.visadirect.fundstransfer.data import PullFundsTransaction


class TestPullTransaction(unittest.TestCase):

    def test_hasSystemsTraceAuditNumber(self):
        t = PullFundsTransaction(stan=123456)
        self.assertTrue(hasattr(t, 'systemsTraceAuditNumber'))

    def test_hasAmount(self):
        t = PullFundsTransaction(stan=123456, amount=123.45)
        self.assertTrue(hasattr(t, 'amount'))

    def test_hasSenderPrimaryAccountNumber(self):
        t = PullFundsTransaction(stan=123456, sender_pan='1234567812345678')
        self.assertTrue(hasattr(t, 'senderPrimaryAccountNumber'))

    def test_hasSenderCardExpiryDate(self):
        t = PullFundsTransaction(stan=123456, sender_card_expiry_date='12/18')
        self.assertTrue(hasattr(t, 'senderCardExpiryDate'))

    def test_hasSenderCurrencyCode(self):
        t = PullFundsTransaction(stan=123456, sender_currency_code='USD')
        self.assertTrue(hasattr(t, 'senderCurrencyCode'))

    def test_hasCardAcceptor(self):
        t = PullFundsTransaction(stan=123456, card_acceptor=object)
        self.assertTrue(hasattr(t, 'cardAcceptor'))
