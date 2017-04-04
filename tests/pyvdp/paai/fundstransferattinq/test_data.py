import unittest

from pyvdp.paai.fundstransferattinq.cardattributes import FundsTransferInquiryData


class TestFundsTransferInquiryData(unittest.TestCase):

    def test_attributes(self):

        params = {
            'stan': 123456,
            'pan': '1234567812345678',
            'acquiring_bin': 12345,
            'acquirer_country_code': 123,
        }

        data = FundsTransferInquiryData(**params)

        attrs = [
            'primaryAccountNumber',
            'acquiringBin',
            'acquirerCountryCode'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)
