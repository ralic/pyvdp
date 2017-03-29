import unittest

from pyvdp.visadirect.mvisa import CashinPushPaymentTransaction, CashoutPushPaymentTransaction, \
    MerchantPushPaymentTransaction, PurchaseIdentifier


class TestCashinPushPaymentTransaction(unittest.TestCase):

    def test_attributes(self):

        params = {
            'stan': 123456,
            'recipient_pan': '1234567812345678',
            'amount': 123.45,
            'mcc': '1234',
            'acquiring_bin': 123456,
            'acquirer_country_code': 123,
            'card_acceptor': object,
            'transaction_currency_code': 'USD',
            'business_application_id': 'CI',
            'sender_reference': 'Agent 007',
            'sender_account_number': '09876543210987654321',
            'sender_name': 'Smith Agent'
        }

        data = CashinPushPaymentTransaction(**params)

        attrs = [
            'recipientPrimaryAccountNumber',
            'amount',
            'merchantCategoryCode',
            'acquiringBin',
            'acquirerCountryCode',
            'cardAcceptor',
            'transactionCurrencyCode',
            'businessApplicationId',
            'senderReference',
            'senderAccountNumber',
            'senderName'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestCashoutPushPaymentTransaction(unittest.TestCase):

    def test_attributes(self):

        params = {
            'stan': 123456,
            'recipient_pan': '1234567812345678',
            'amount': 123.45,
            'mcc': '1234',
            'acquiring_bin': 123456,
            'acquirer_country_code': 123,
            'card_acceptor': object,
            'transaction_currency_code': 'USD',
            'business_application_id': 'CI',
            'sender_reference': 'Agent 007',
            'sender_account_number': '09876543210987654321',
            'sender_name': 'Smith Agent'
        }

        data = CashoutPushPaymentTransaction(**params)

        attrs = [
            'recipientPrimaryAccountNumber',
            'amount',
            'merchantCategoryCode',
            'acquiringBin',
            'acquirerCountryCode',
            'cardAcceptor',
            'transactionCurrencyCode',
            'businessApplicationId',
            'senderReference',
            'senderAccountNumber',
            'senderName'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestMerchantPushPaymentTransaction(unittest.TestCase):

    def test_attributes(self):

        params = {
            'stan': 123456,
            'recipient_pan': '1234567812345678',
            'amount': 123.45,
            'mcc': '1234',
            'acquiring_bin': 123456,
            'acquirer_country_code': 123,
            'transaction_fee_amount': 12.34,
            'card_acceptor': object,
            'transaction_currency_code': 'USD',
            'purchase_id': object,
            'secondary_id': 'mypurchase',
            'business_application_id': 'MP',
            'sender_reference': 'Agent 007',
            'sender_account_number': '09876543210987654321',
            'sender_name': 'Smith Agent'
        }

        data = MerchantPushPaymentTransaction(**params)

        attrs = [
            'recipientPrimaryAccountNumber',
            'amount',
            'merchantCategoryCode',
            'acquiringBin',
            'acquirerCountryCode',
            'transactionFeeAmount',
            'cardAcceptor',
            'transactionCurrencyCode',
            'purchaseIdentifier',
            'secondaryId',
            'businessApplicationId',
            'senderReference',
            'senderAccountNumber',
            'senderName'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestPurchaseIdentifier(unittest.TestCase):

    def test_attributes(self):

        params = {
            'type': '0',
            'reference_number': 'ABC123'
        }

        data = PurchaseIdentifier(**params)

        attrs = [
            'type',
            'referenceNumber'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)