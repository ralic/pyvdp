import unittest

from pyvdp.paai.fundstransferattinq.cardattributes.data import FundsTransferInquiryData


class TestFundsTransferInquiryData(unittest.TestCase):

    def setUp(self):
        self.ftid = FundsTransferInquiryData(pan='12345678',
                                             stan=123456,
                                             rrn='123456123456',
                                             acquiring_bin=12345678,
                                             acquirer_country_code=123)

    def test_hasATTR_MAPPINGS(self):
        self.assertTrue(hasattr(self.ftid, 'ATTR_MAPPINGS'), 'missing ATTR_MAPPINGS')

    def test_hasPrimaryAccountNumber(self):
        self.assertTrue(hasattr(self.ftid, 'primaryAccountNumber'), 'missing pan')

    def test_hasSystemsTraceAuditNumber(self):
        self.assertTrue(hasattr(self.ftid, 'systemsTraceAuditNumber'), 'missing stan')

    def test_hasRetrievalReferenceNumber(self):
        self.assertTrue(hasattr(self.ftid, 'retrievalReferenceNumber'), 'missing rrn')

    def test_hasAcquiringBin(self):
        self.assertTrue(hasattr(self.ftid, 'acquiringBin'), 'missing acquiring_bin')

    def test_hasAcquirerCountryCode(self):
        self.assertTrue(hasattr(self.ftid, 'acquirerCountryCode'), 'missing acquirer_country_code')
