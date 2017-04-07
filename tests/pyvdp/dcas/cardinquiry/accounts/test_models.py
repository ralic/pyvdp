import unittest

from pyvdp.dcas.cardinquiry.accounts import CardInquiryModel


class TestCardInquiryModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'directDebitAccountNumber': '0987654321',
            'routingNumber': '0987654321',
            'cardholderName': object,
        }

        model = CardInquiryModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestCardholderName(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'firstName': 'John',
            'lastName': 'Doe',
        }

        model = CardInquiryModel.CardholderName(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
