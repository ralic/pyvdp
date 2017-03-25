import unittest

from pyvdp.visadirect.data import OriginalDataElements


class TestOriginalDataElements(unittest.TestCase):

    def test_hasSystemsTraceAuditNumber(self):
        ode = OriginalDataElements(stan=123456)
        self.assertTrue(hasattr(ode, 'systemsTraceAuditNumber'))

    def test_hasApprovalCode(self):
        ode = OriginalDataElements(approval_code=123456)
        self.assertTrue(hasattr(ode, 'approvalCode'))

    def test_hasTransmissionDateTime(self):
        ode = OriginalDataElements(transmission_datetime='02-12-24')
        self.assertTrue(hasattr(ode, 'transmissionDateTime'))


