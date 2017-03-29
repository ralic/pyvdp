import unittest
from datetime import datetime

from pyvdp.visadirect.data import CardAcceptor
from pyvdp.visadirect.data import MerchantVerificationValue
from pyvdp.visadirect.data import VisaDirectTransaction
from pyvdp.visadirect.data import OriginalDataElements
from pyvdp.visadirect.data import PointOfServiceCapability
from pyvdp.visadirect.data import PointOfServiceData

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


class TestCardAcceptor(unittest.TestCase):

    def test_attributes(self):

        params = {
            'name': 'Card Acceptor',
            'terminal_id': 'ABC123',
            'id_code': '321CBA',
            'address': {}
        }

        ca = CardAcceptor(**params)

        attrs = [
            'name',
            'terminalId',
            'idCode',
            'address'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(ca, attr), 'missing %s attribute' % attr)


class TestCardAcceptorAddress(unittest.TestCase):

    def test_attributes(self):

        params = {
            'country': 'US',
            'zip_code': 'ABC123',
            'state': 'CA',
            'county': 'ML'
        }

        caa = CardAcceptor.CardAcceptorAddress(**params)

        attrs = [
            'country',
            'zipCode',
            'state',
            'county'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(caa, attr), 'missing %s attribute' % attr)


class TestMerchantVerificationValue(unittest.TestCase):

    def test_attributes(self):

        params = {
            'acquirer_assigned': 'ABC123',
            'visa_assigned': 'DE45',
        }

        data = MerchantVerificationValue(**params)

        attrs = [
            'mvvAcquirerAssigned',
            'mvvVisaAssigned',
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestOriginalDataElements(unittest.TestCase):

    def test_attributes(self):

        params = {
            'stan': 123456,
            'approval_code': 'abc123',
            'transmission_datetime': '2017-28-03T16:17:18',
            'acquiring_bin': 12345678
        }

        data = OriginalDataElements(**params)

        attrs = [
            'systemsTraceAuditNumber',
            'approvalCode',
            'transmissionDateTime',
            'acquiringBin'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestPointOfServiceCapability(unittest.TestCase):

    def test_attributes(self):

        params = {
            'type': 1,
            'entry_capability': 2,
        }

        data = PointOfServiceCapability(**params)

        attrs = [
            'posTerminalType',
            'posTerminalEntryCapability',
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestPointOfServiceData(unittest.TestCase):

    def test_attributes(self):

        params = {
            'pan_entry_mode': 1,
            'condition_code': 12,
            'moto_eci_indicator': '0'
        }

        data = PointOfServiceData(**params)

        attrs = [
            'panEntryMode',
            'posConditionCode',
            'motoECIIndicator'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


