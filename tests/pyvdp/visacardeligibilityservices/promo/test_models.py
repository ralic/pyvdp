import unittest
from pyvdp.visacardeligibilityservices.promo import RedeemModel


class TestRedeemModel(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'redeemRequest': object
        }

        model = RedeemModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestRedeemRequest(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'vendorUniqueId': str,
            'permanentAccountNumber': str,
            'requestTimeStamp': str,
            'correlationId': str
        }

        model = RedeemModel.RedeemRequest(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)

