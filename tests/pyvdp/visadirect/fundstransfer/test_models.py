import unittest

from pyvdp.visadirect.fundstransfer import PullFundsTransaction, MultiPullFundsTransaction
from pyvdp.visadirect.fundstransfer import PushFundsTransaction, MultiPushFundsTransaction
from pyvdp.visadirect.fundstransfer import ReverseFundsTransaction, MultiReverseFundsTransaction


class TestPullFundsTransaction(unittest.TestCase):

    def test_attributes(self):

        params = {
            'stan': 123456,
            'acquiring_bin': 123456,
            'acquirer_country_code': 123,
            'amount': 123.45,
            'sender_pan': '1234123412341234',
            'sender_expiration': '2020-02',
            'sender_currency_code': 'USD',
            'business_application_id': 'AA',
            'card_acceptor': object,
            'surcharge': 0.45,
            'mcc': 1234,
            'cavv': '123456789123456789',
            'cvv2': '123',
            'foreign_exchange_fee_transaction': 0.45,
            'msd': object,
            'pos': object,
            'posc': object,
            'pin_data': object,
            'fee_program_indicator': 'abc',
            'merchant_pseudo_aba_number': '123456789',
            'sharing_group_code': 'abc',
            'mvv': object
        }

        data = PullFundsTransaction(**params)

        attrs = [
            'systemsTraceAuditNumber',
            'acquiringBin',
            'acquirerCountryCode',
            'amount',
            'senderPrimaryAccountNumber',
            'senderCardExpiryDate',
            'senderCurrencyCode',
            'cardAcceptor',
            'businessApplicationId',
            'merchantCategoryCode',
            'surcharge',
            'cavv',
            'cardCvv2Value',
            'foreignExchangeFeeTransaction',
            'magneticStripeData',
            'pointOfServiceData',
            'pointOfServiceCapability',
            'pinData',
            'feeProgramIndicator',
            'merchantPseudoAbaNumber',
            'sharingGroupCode',
            'merchantVerificationValue'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestMultiPullFundsTransaction(unittest.TestCase):

    def test_attributes(self):
        params = {
            'acquiring_bin': 123456789,
            'acquirer_country_code': 853,
            'business_application_id': 'AA',
            'request': [object, object]
        }

        data = MultiPullFundsTransaction(**params)

        attrs = [
            'acquiringBin',
            'acquirerCountryCode',
            'businessApplicationId',
            'request'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestPushFundsTransaction(unittest.TestCase):

    def test_attributes(self):

        params = {
            'stan': 123456,
            'acquiring_bin': 123456,
            'acquirer_country_code': 123,
            'transaction_currency_code': 'USD',
            'recipient_pan': '1234567812345678',
            'amount': 123.45,
            'business_application_id': 'AA',
            'card_acceptor': object,
            'sender_address': 'Elm Street 18',
            'sender_name': 'Doe Jane',
            'sender_reference': 'ABCDEFGH12345678',
            'sender_account_number': '12345678901234567890',
            'sender_country_code': 'USA',
            'sender_city': 'San Francisco',
            'sender_state_code': 'CA',
            'recipient_name': 'Doe John',
            'mcc': 123,
            'transaction_identifier': 123456789012345,
            'source_of_funds_code': 'ABC',
            'recipient_expiration': '2020-12',
            'account_type': '00',
            'fee_program_indicator': 'wtf',
            'sender_dob': '1981-02-04',
            'pos': object,
            'surcharge': 0.45,
            'merchant_pseudo_aba_number': 123456789,
            'sharing_group_code': '1234567812345678',
            'mvv': object
        }

        data = PushFundsTransaction(**params)

        attrs = [
            'systemsTraceAuditNumber',
            'acquiringBin',
            'acquirerCountryCode',
            'transactionCurrencyCode',
            'recipientPrimaryAccountNumber',
            'amount',
            'businessApplicationId',
            'cardAcceptor',
            'senderReference',
            'senderAccountNumber',
            'senderAddress',
            'senderCountryCode',
            'senderName',
            'senderCity',
            'senderStateCode',
            'recipientName',
            'merchantCategoryCode',
            'transactionIdentifier',
            'sourceOfFundsCode',
            'recipientCardExpiryDate',
            'accountType',
            'feeProgramIndicator',
            'senderDateOfBirth',
            'pointOfServiceData',
            'surcharge',
            'merchantPseudoAbaNumber',
            'sharingGroupCode',
            'merchantVerificationValue'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestMultiPushFundsTransaction(unittest.TestCase):

    def test_attributes(self):
        params = {
            'acquiring_bin': 123456789,
            'acquirer_country_code': 853,
            'business_application_id': 'AA',
            'request': [object, object]
        }

        data = MultiPushFundsTransaction(**params)

        attrs = [
            'acquiringBin',
            'acquirerCountryCode',
            'businessApplicationId',
            'request'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestReverseFundsTransaction(unittest.TestCase):

    def test_attributes(self):

        params = {
            'stan': 123456,
            'transaction_identifier': 123456,
            'acquiring_bin': 123456,
            'acquirer_country_code': 123,
            'sender_pan': '1234567812345678',
            'sender_expiration': '2020-12',
            'sender_currency_code': 'USD',
            'amount': 123.45,
            'surcharge': 0.45,
            'foreign_exchange_fee_transaction': 0.45,
            'ode': object,
            'card_acceptor': object,
            'pos': object,
            'posc': object,
            'fee_program_indicator': 'wtf',
            'merchant_pseudo_aba_number': '123',
            'sharing_group_code': 'abc',
            'network_id': 12,
            'mvv': object
        }

        data = ReverseFundsTransaction(**params)

        attrs = [
            'systemsTraceAuditNumber',
            'transactionIdentifier',
            'acquiringBin',
            'acquirerCountryCode',
            'senderPrimaryAccountNumber',
            'senderCardExpiryDate',
            'senderCurrencyCode',
            'amount',
            'surcharge',
            'foreignExchangeFeeTransaction',
            'originalDataElements',
            'cardAcceptor',
            'pointOfServiceData',
            'pointOfServiceCapability',
            'feeProgramIndicator',
            'merchantPseudoAbaNumber',
            'networkId',
            'sharingGroupCode',
            'merchantVerificationValue'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestMultiReverseFundsTransaction(unittest.TestCase):

    def test_attributes(self):
        params = {
            'acquiring_bin': 123456789,
            'acquirer_country_code': 853,
            'request': [object, object]
        }

        data = MultiReverseFundsTransaction(**params)

        attrs = [
            'acquiringBin',
            'acquirerCountryCode',
            'request'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)
