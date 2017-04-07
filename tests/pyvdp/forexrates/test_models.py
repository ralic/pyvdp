import unittest
from pyvdp.forexrates import ForeignExchangeRatesModel


class TestForeignExchangeRatesModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'destinationCurrencyCode': '123',
            'sourceCurrencyCode': '123',
            'sourceAmount': 100.00,
            'markUpRate': '0.07',
            'systemsTraceAuditNumber': 123456,
            'acquiringBin': 123,
            'acquirerCountryCode': 456,
            'cardAcceptor': object
        }

        model = ForeignExchangeRatesModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
