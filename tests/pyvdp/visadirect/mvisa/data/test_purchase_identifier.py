import unittest

from pyvdp.visadirect.mvisa.data import PurchaseIdentifier


class TestPurchaseIdentifier(unittest.TestCase):

    def test_hasType(self):
        pi = PurchaseIdentifier(type='test_type')
        self.assertTrue(hasattr(pi, 'type'))

    def test_hasReferenceNumber(self):
        pi = PurchaseIdentifier(reference_number='reference')
        self.assertTrue(hasattr(pi, 'referenceNumber'))
