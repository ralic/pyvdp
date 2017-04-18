import unittest

from pyvdp.pav import CardValidationModel


class TestCardValidationModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'systemsTraceAuditNumber': 123456,
            'primaryAccountNumber': '1234567812345678',
            'cardExpiryDate': '2018-02',
            'addressVerificationResults': object,
            'cardCvv2Value': '123',
            'acquiringBin': 123456,
            'acquirerCountryCode': 123,
            'cardAcceptor': object
        }

        model = CardValidationModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestAddressVerificationResults(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'street': 'Elm street',
            'postalCode': '123456'
        }

        model = CardValidationModel.AddressVerificationResults(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
