import unittest

from pyvdp.dcas.cardinquiry.accounts import CardInquiryModel


class TestCardInquiryModel(unittest.TestCase):

    def test_attributes(self):

        params = {
            'direct_dan': '0987654321',
            'routing_number': '0987654321',
            'cardholder_name': object,
        }

        data = CardInquiryModel(**params)

        attrs = [
            'directDebitAccountNumber',
            'routingNumber',
            'cardholderName',
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestCardholderName(unittest.TestCase):

    def test_attributes(self):

        params = {
            'first_name': 'John',
            'last_name': 'Doe',
        }

        data = CardInquiryModel.CardholderName(**params)

        attrs = [
            'firstName',
            'lastName',
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)