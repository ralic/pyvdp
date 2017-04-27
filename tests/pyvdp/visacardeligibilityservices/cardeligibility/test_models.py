import unittest
from pyvdp.visacardeligibilityservices.cardeligibility import PrepayModel, ValidateModel


class TestValidateModel(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'validateRequest': object
        }

        model = ValidateModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestValidateRequest(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'vendorUniqueId': str,
            'extendedData': str,
            'permanentAccountNumber': str,
            'requestTimeStamp': str,
            'correlationId': str
        }

        model = ValidateModel.ValidateRequest(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestPrepayModel(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'prepayRequest': object
        }

        model = PrepayModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestPrepayRequest(unittest.TestCase):
    def test_attributes(self):
        attrs = {
            'vendorUniqueId': str,
            'permanentAccountNumber': str,
            'requestTimeStamp': str,
            'correlationId': str
        }

        model = PrepayModel.PrepayRequest(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)