import unittest
from datetime import datetime

from pyvdp.visadirect.data import VisaDirectTransaction

STAN = '123456'


class TestVisaDirectTransaction(unittest.TestCase):
    def setUp(self):
        self.t = VisaDirectTransaction(stan=STAN)

    def test_systemsTraceAuditNumber(self):
        self.assertTrue(STAN, self.t.systemsTraceAuditNumber)

    def test_localTransactionDateTime(self):
        tdt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        self.assertTrue(tdt, self.t.localTransactionDateTime)

    def test_retrievalReferenceNUmber(self):
        now = datetime.now()
        yld = now.strftime('%Y')[3]
        doty = now.strftime('%j')
        ch = now.strftime('%H')
        rrn = yld + doty + ch + STAN

        self.assertTrue(rrn, self.t.retrievalReferenceNumber)
