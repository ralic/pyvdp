import unittest

from pyvdp.visadirect.fundstransfer import PullFundsTransactionsModel, MultiPullFundsTransactionsModel
from pyvdp.visadirect.fundstransfer import PushFundsTransactionsModel, MultiPushFundsTransactionsModel
from pyvdp.visadirect.fundstransfer import ReverseFundsTransactionsModel, MultiReverseFundsTransactionsModel


class TestPullFundsTransactionModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'systemsTraceAuditNumber': 123456,
            'acquiringBin': 123456,
            'acquirerCountryCode': 123,
            'amount': 123.45,
            'senderPrimaryAccountNumber': '1234123412341234',
            'senderCardExpiryDate': '2020-02',
            'senderCurrencyCode': 'USD',
            'businessApplicationId': 'AA',
            'cardAcceptor': object,
            'surcharge': 0.45,
            'merchantCategoryCode': 1234,
            'cavv': '123456789123456789',
            'cardCvv2Value': '123',
            'foreignExchangeFeeTransaction': 0.45,
            'magneticStripeData': object,
            'pointOfServiceData': object,
            'pointOfServiceCapability': object,
            'pinData': object,
            'feeProgramIndicator': 'abc',
            'merchantPseudoAbaNumber': '123456789',
            'sharingGroupCode': 'abc',
            'merchantVerificationValue': object
        }

        model = PullFundsTransactionsModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestMultiPullFundsTransactionModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'acquiringBin': 123456789,
            'acquirerCountryCode': 853,
            'businessApplicationId': 'AA',
            'request': [object, object]
        }

        model = MultiPullFundsTransactionsModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestPushFundsTransactionModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'systemsTraceAuditNumber': 123456,
            'acquiringBin': 123456,
            'acquirerCountryCode': 123,
            'transactionCurrencyCode': 'USD',
            'recipientPrimaryAccountNumber': '1234567812345678',
            'amount': 123.45,
            'businessApplicationId': 'AA',
            'cardAcceptor': object,
            'senderAddress': 'Elm Street 18',
            'senderName': 'Doe Jane',
            'senderReference': 'ABCDEFGH12345678',
            'senderAccountNumber': '12345678901234567890',
            'senderCountryCode': 'USA',
            'senderCity': 'San Francisco',
            'senderStateCode': 'CA',
            'recipientName': 'Doe John',
            'merchantCategoryCode': 123,
            'transactionIdentifier': 123456789012345,
            'sourceOfFundsCode': 'ABC',
            'recipientCardExpiryDate': '2020-12',
            'accountType': '00',
            'feeProgramIndicator': 'wtf',
            'senderDateOfBirth': '1981-02-04',
            'pointOfServiceData': object,
            'surcharge': 0.45,
            'merchantPseudoAbaNumber': 123456789,
            'sharingGroupCode': '1234567812345678',
            'merchantVerificationValue': object
        }

        model = PushFundsTransactionsModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestMultiPushFundsTransactionModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'acquiringBin': 123456789,
            'acquirerCountryCode': 853,
            'businessApplicationId': 'AA',
            'request': [object, object]
        }

        model = MultiPushFundsTransactionsModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestReverseFundsTransactionModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'systemsTraceAuditNumber': 123456,
            'transactionIdentifier': 123456,
            'acquiringBin': 123456,
            'acquirerCountryCode': 123,
            'senderPrimaryAccountNumber': '1234567812345678',
            'senderCardExpiryDate': '2020-12',
            'senderCurrencyCode': 'USD',
            'amount': 123.45,
            'surcharge': 0.45,
            'foreignExchangeFeeTransaction': 0.45,
            'originalDataElements': object,
            'cardAcceptor': object,
            'pointOfServiceData': object,
            'pointOfServiceCapability': object,
            'feeProgramIndicator': 'wtf',
            'merchantPseudoAbaNumber': '123',
            'sharingGroupCode': 'abc',
            'networkId': 12,
            'merchantVerificationValue': object
        }

        model = ReverseFundsTransactionsModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestMultiReverseFundsTransactionModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'acquiringBin': 123456789,
            'acquirerCountryCode': 853,
            'request': [object, object]
        }

        model = MultiReverseFundsTransactionsModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
