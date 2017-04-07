import unittest
from datetime import datetime

from pyvdp.visadirect.models import CardAcceptorModel
from pyvdp.visadirect.models import MerchantVerificationValueModel
from pyvdp.visadirect.models import VisaDirectTransactionModel
from pyvdp.visadirect.models import OriginalDataElementsModel
from pyvdp.visadirect.models import PointOfServiceCapabilityModel
from pyvdp.visadirect.models import PointOfServiceDataModel


class TestVisaDirectTransactionModel(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'systemsTraceAuditNumber': 123456,
            'retrievalReferenceNumber': '123456123456'
        }

        model = VisaDirectTransactionModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)

class TestCardAcceptorModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'name': 'Card Acceptor',
            'terminalId': 'ABC123',
            'idCode': '321CBA',
            'address': object
        }

        model = CardAcceptorModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestCardAcceptorAddress(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'country': 'US',
            'zipCode': 'ABC123',
            'state': 'CA',
            'county': 'ML',
            'city': 'SFO'
        }

        model = CardAcceptorModel.CardAcceptorAddress(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestMerchantVerificationValueModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'mvvAcquirerAssigned': 'ABC123',
            'mvvVisaAssigned': 'DE45',
        }

        model = MerchantVerificationValueModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestOriginalDataElementsModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'systemsTraceAuditNumber': 123456,
            'approvalCode': 'abc123',
            'transmissionDateTime': '2017-28-03T16:17:18',
            'acquiringBin': 12345678
        }

        model = OriginalDataElementsModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestPointOfServiceCapabilityModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'posTerminalType': 1,
            'posTerminalEntryCapability': 2,
        }

        model = PointOfServiceCapabilityModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestPointOfServiceDataModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'panEntryMode': 1,
            'posConditionCode': 12,
            'motoECIIndicator': '0'
        }

        model = PointOfServiceDataModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
