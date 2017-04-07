import unittest

from pyvdp.paai.fundstransferattinq.cardattributes import FundsTransferInquiryModel


class TestFundsTransferInquiryModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'systemsTraceAuditNumber': 123456,
            'primaryAccountNumber': '1234567812345678',
            'acquiringBin': 12345,
            'acquirerCountryCode': 123,
            'retrievalReferenceNumber': '123456123456'
        }

        model = FundsTransferInquiryModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
