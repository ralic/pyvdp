import unittest

from pyvdp.pav.data import PavTransaction


class TestPavTransaction(unittest.TestCase):

    def test_hasSystemsTraceAuditNumber(self):
        t = PavTransaction(stan=123456)
        self.assertTrue(hasattr(t, 'systemsTraceAuditNumber'))

    def test_hasPrimaryAccountNumber(self):
        t = PavTransaction(pan=1234567812345678)
        self.assertTrue(hasattr(t, 'primaryAccountNumber'))

    def test_hasCardExpiryDate(self):
        t = PavTransaction(expiry_date='12/18')
        self.assertTrue(hasattr(t, 'cardExpiryDate'))

    def test_hasCardCvv2Value(self):
        t = PavTransaction(cvv2='123')
        self.assertTrue(hasattr(t, 'cardCvv2Value'))
