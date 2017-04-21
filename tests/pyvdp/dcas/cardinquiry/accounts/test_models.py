import unittest

from pyvdp.dcas.cardinquiry.accounts import DebitCardInquiryModel


class TestCardInquiryModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'directDebitAccountNumber': '0987654321',
            'routingNumber': '0987654321',
            'cardholderName': object,
        }

        model = DebitCardInquiryModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestCardholderName(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'firstName': 'John',
            'lastName': 'Doe',
        }

        model = DebitCardInquiryModel.CardholderName(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
