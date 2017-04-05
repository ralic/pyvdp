import unittest

from pyvdp.pav import PaymentAccountValidation


class TestPavData(unittest.TestCase):

    def test_attributes(self):

        params = {
            'stan': 123456,
            'pan': '1234567812345678',
            'card_expiry_date': '2018-02',
            'avr': object,
            'cvv2': '123',
            'acquiring_bin': 123456,
            'acquirer_country_code': 123,
            'card_acceptor': object
        }

        data = PaymentAccountValidation(**params)

        attrs = [
            'systemsTraceAuditNumber',
            'primaryAccountNumber',
            'cardExpiryDate',
            'addressVerificationResults',
            'cardCvv2Value',
            'acquiringBin',
            'acquirerCountryCode',
            'cardAcceptor'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestAddressVerificationResults(unittest.TestCase):

    def test_attributes(self):

        params = {
            'street': 'Elm street',
            'postal_code': '123456'
        }

        data = PaymentAccountValidation.AddressVerificationResults(**params)

        attrs = [
            'street',
            'postalCode'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)