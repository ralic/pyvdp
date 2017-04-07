import unittest

from pyvdp.visadirect.mvisa import (CashinPushPaymentTransactionModel,
                                    CashoutPushPaymentTransactionModel,
                                    MerchantPushPaymentTransactionModel,
                                    PurchaseIdentifierModel)


class TestCashinPushPaymentTransactionModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'systemsTraceAuditNumber': 123456,
            'recipientPrimaryAccountNumber': '1234567812345678',
            'amount': 123.45,
            'merchantCategoryCode': '1234',
            'acquiringBin': 123456,
            'acquirerCountryCode': 123,
            'cardAcceptor': object,
            'transactionCurrencyCode': 'USD',
            'businessApplicationId': 'CI',
            'senderReference': 'Agent 007',
            'senderAccountNumber': '09876543210987654321',
            'senderName': 'Smith Agent'
        }

        model = CashinPushPaymentTransactionModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestCashoutPushPaymentTransactionModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'systemsTraceAuditNumber': 123456,
            'recipientPrimaryAccountNumber': '1234567812345678',
            'amount': 123.45,
            'merchantCategoryCode': '1234',
            'acquiringBin': 123456,
            'acquirerCountryCode': 123,
            'cardAcceptor': object,
            'transactionCurrencyCode': 'USD',
            'businessApplicationId': 'CI',
            'senderReference': 'Agent 007',
            'senderAccountNumber': '09876543210987654321',
            'senderName': 'Smith Agent'
        }

        model = CashoutPushPaymentTransactionModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestMerchantPushPaymentTransactionModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'systemsTraceAuditNumber': 123456,
            'recipientPrimaryAccountNumber': '1234567812345678',
            'amount': 123.45,
            'merchantCategoryCode': '1234',
            'acquiringBin': 123456,
            'acquirerCountryCode': 123,
            'transactionFeeAmount': 12.34,
            'cardAcceptor': object,
            'transactionCurrencyCode': 'USD',
            'purchaseIdentifier': object,
            'secondaryId': 'mypurchase',
            'businessApplicationId': 'MP',
            'senderReference': 'Agent 007',
            'senderAccountNumber': '09876543210987654321',
            'senderName': 'Smith Agent'
        }

        model = MerchantPushPaymentTransactionModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestPurchaseIdentifierModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'type': '0',
            'referenceNumber': 'ABC123'
        }

        model = PurchaseIdentifierModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
