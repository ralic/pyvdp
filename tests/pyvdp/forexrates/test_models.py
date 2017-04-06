import unittest
from pyvdp.forexrates import ForeignExchangeRatesModel


class TestForeignExchangeRatesModel(unittest.TestCase):

    def test_attributes(self):
        params = {
            'destination_cur_code': '123',
            'source_cur_code': '123',
            'source_amount': 100.00,
            'markup_rate': '0.07',
            'stan': 123456,
            'acquiring_bin': 123,
            'acquirer_country_code': 456,
            'card_acceptor': object
        }

        data = ForeignExchangeRatesModel(**params)

        attrs = [
            'destinationCurrencyCode',
            'sourceCurrencyCode',
            'sourceAmount',
            'markUpRate',
            'systemsTraceAuditNumber',
            'acquiringBin',
            'acquirerCountryCode',
            'cardAcceptor'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)

