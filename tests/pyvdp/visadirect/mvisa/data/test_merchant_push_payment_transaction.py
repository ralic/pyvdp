import unittest

from pyvdp.visadirect.mvisa.data import MerchantPushPaymentTransaction


class TestMerchantPushPaymentTransaction(unittest.TestCase):

    def test_hasSystemsTraceAuditNumber(self):
        mppt = MerchantPushPaymentTransaction(stan=123456)
        self.assertTrue(hasattr(mppt, 'systemsTraceAuditNumber'))

    def test_hasAmount(self):
        mppt = MerchantPushPaymentTransaction(stan=123456, amount=123.45)
        self.assertTrue(hasattr(mppt, 'amount'))

    def test_hasRecipientPrimaryAccountNumber(self):
        mppt = MerchantPushPaymentTransaction(stan=123456, recipient_pan='1234567812345678')
        self.assertTrue(hasattr(mppt, 'recipientPrimaryAccountNumber'))

    def test_hasTransactionCurrencyCode(self):
        mppt = MerchantPushPaymentTransaction(stan=123456, transaction_currency_code='USD')
        self.assertTrue(hasattr(mppt, 'transactionCurrencyCode'))

    def test_hasSenderName(self):
        mppt = MerchantPushPaymentTransaction(stan=123456, sender_name='John Doe')
        self.assertTrue(hasattr(mppt, 'senderName'))

    def test_hasSenderAccountNumber(self):
        mppt = MerchantPushPaymentTransaction(stan=123456, sender_account_number='12345678')
        self.assertTrue(hasattr(mppt, 'senderAccountNumber'))

    def test_hasPurchaseIdentifier(self):
        mppt = MerchantPushPaymentTransaction(stan=123456, purchase_identifier='123-45')
        self.assertTrue(hasattr(mppt, 'purchaseIdentifier'))

    def test_hasCardAcceptor(self):
        mppt = MerchantPushPaymentTransaction(stan=123456, card_acceptor=object)
        self.assertTrue(hasattr(mppt, 'cardAcceptor'))
