import unittest

from pyvdp.mlc.enrollment import EnrollmentsModel


class TestEnrollmentsModel(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'enrollmentMessageType': str,
            'enrollmentRequest': object
        }

        model = EnrollmentsModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestEnrollmentRequest(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'clientMessageID': str,
            'primaryAccountNumber': str,
            'deviceId': str,
            'issuerId': str
        }

        model = EnrollmentsModel.EnrollmentRequest(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
