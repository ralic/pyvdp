from pyvdp.visadirect import VisaDirectTransaction


class CashinPushPaymentTransaction(VisaDirectTransaction):
    """VisaDirect mVISA CashinPushPayments data object model.

    :param int stan: **Required**. Systems trace audit number. 6 digits integer.
    :param str recipient_pan: **Required**. Recipient primary account number (PAN). 13-19 characters string.
    :param float amount: **Required**. Transaction amount. 12 digits, 3 fractions.
    :param int mcc: **Optional**. Merchant category code, populated by Originator. 4 digits integer. **6012** for mVISA.
    :param int acquiring_bin: **Required**. Business identification number. 6-11 digits integer.
    :param int acquirer_country_code: **Required**. Country `ISO code <https://developer.visa.com/request_response_codes#isoCodes>`_ 
        of originator BIN. 3 digits integer.
    :param CardAcceptor card_acceptor: **Required**. Instance of :func:`~pyvdp.visadirect.CardAcceptor` data object.
    :param str transaction_currency_code: **Required**. Transaction currencyt `ISO code <https://developer.visa.com/request_response_codes#isoCodes>`_.
            3 characters string.
    :param str business_application_id: **Required**. Business application identifier. **CI** for cash-in operations.
        See `BAI codes <https://developer.visa.com/request_response_codes#businessApplicationId>`_ for details.
    :param str sender_reference: **Optional**. Unique agent reference. Max 16 characters string.
    :param str sender_account_number: **Optional**. Sender account number.
    :param str sender_name: **Required**. Agent name. Max 30 characters string.
    
    **Example:**
        ..  code-block:: json

            {
                "acquirerCountryCode": "643",
                "acquiringBin": "400171",
                "amount": "124.05",
                "businessApplicationId": "CI",
                "cardAcceptor": {
                    "address": {
                        "city": "Bangalore",
                        "country": "IND"
                    },
                    "idCode": "ID-Code123",
                    "name": "Card Accpector ABC"
                },
                "localTransactionDateTime": "2017-03-17T05:42:01",
                "merchantCategoryCode": "4829",
                "recipientPrimaryAccountNumber": "4123640062698797",
                "retrievalReferenceNumber": "430000367618",
                "senderAccountNumber": "4541237895236",
                "senderName": "Mohammed Qasim",
                "senderReference": "1234",
                "systemsTraceAuditNumber": "313042",
                "transactionCurrencyCode": "USD",
                "transactionIdentifier": "381228649430015"
            }
    """
    # Mappings between constructor arguments and VISA API fields
    # {'constructor argument': 'VISA API field name'}
    ATTR_MAPPINGS = {
        'recipient_pan': 'recipientPrimaryAccountNumber',
        'amount': 'amount',
        'mcc': 'merchantCategoryCode',
        'acquiring_bin': 'acquiringBin',
        'acquirer_country_code': 'acquirerCountryCode',
        'card_acceptor': 'cardAcceptor',
        'transaction_currency_code': 'transactionCurrencyCode',
        'business_application_id': 'businessApplicationId',
        'sender_reference': 'senderReference',
        'sender_account_number': 'senderAccountNumber',
        'sender_name': 'senderName',
    }

    def __init__(self, **kwargs):
        super(CashinPushPaymentTransaction, self).__init__(kwargs['stan'])
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)


class CashoutPushPaymentTransaction(VisaDirectTransaction):
    """VisaDirect mVISA CashoutPushPayments data object model.

    :param int stan: **Required**. Systems trace audit number. 6 digits integer.
    :param str recipient_pan: **Required**. Recipient primary account number (PAN). 13-19 characters string.
    :param float amount: **Required**. Transaction amount. 12 digits, 3 fractions.
    :param int mcc: **Optional**. Merchant category code, populated by Originator. 4 digits integer. **6012** for mVISA.
    :param int acquiring_bin: **Required**. Business identification number. 6-11 digits integer.
    :param int acquirer_country_code: **Required**. Country `ISO code <https://developer.visa.com/request_response_codes#isoCodes>`_ 
        of originator BIN. 3 digits integer.
    :param CardAcceptor card_acceptor: **Required**. Instance of :func:`~pyvdp.visadirect.CardAcceptor` data object.
    :param str transaction_currency_code: **Required**. Transaction currencyt `ISO code <https://developer.visa.com/request_response_codes#isoCodes>`_.
            3 characters string.
    :param str business_application_id: **Required**. Business application identifier. **CO** for cash-out operations.
        See `BAI codes <https://developer.visa.com/request_response_codes#businessApplicationId>`_ for details.
    :param str sender_reference: **Optional**. Unique agent reference. Max 16 characters string.
    :param str sender_account_number: **Optional**. Sender account number.
    :param str sender_name: **Required**. Agent name. Max 30 characters string.

    **Example:**
        ..  code-block:: json

            {
                "acquirerCountryCode": "643",
                "acquiringBin": "400171",
                "amount": "124.05",
                "businessApplicationId": "CO",
                "cardAcceptor": {
                    "address": {
                        "city": "mVisa cashout",
                        "country": "IND"
                    },
                    "idCode": "CA-IDCode-77765",
                    "name": "mVisa cashout"
                },
                "localTransactionDateTime": "2017-03-17T05:46:12",
                "merchantCategoryCode": "6012",
                "recipientPrimaryAccountNumber": "4123640062698797",
                "retrievalReferenceNumber": "412123412878",
                "senderAccountNumber": "456789123456",
                "senderName": "Mohammed Qasim",
                "senderReference": "REFNUM123",
                "systemsTraceAuditNumber": "567889",
                "transactionCurrencyCode": "USD",
                "transactionIdentifier": "381228649430015"
            }

    ..  seealso::

        `VisaDirect mVISA CashoutPushPayments Reference <https://developer.visa.com/products/visa_direct/reference#visa_direct__mvisa__v1__cash_out_push_payments_post>`_

    """
    # Mappings between constructor arguments and VISA API fields
    # {'constructor argument': 'VISA API field name'}
    ATTR_MAPPINGS = {
        'recipient_pan': 'recipientPrimaryAccountNumber',
        'amount': 'amount',
        'mcc': 'merchantCategoryCode',
        'acquiring_bin': 'acquiringBin',
        'acquirer_country_code': 'acquirerCountryCode',
        'card_acceptor': 'cardAcceptor',
        'transaction_currency_code': 'transactionCurrencyCode',
        'business_application_id': 'businessApplicationId',
        'sender_reference': 'senderReference',
        'sender_account_number': 'senderAccountNumber',
        'sender_name': 'senderName',
    }

    def __init__(self, **kwargs):
        super(CashoutPushPaymentTransaction, self).__init__(kwargs['stan'])
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)


class MerchantPushPaymentTransaction(VisaDirectTransaction):
    """VisaDirect mVISA MerchantPushPayments data object model.

    :param int stan: **Required**. Systems trace audit number. 6 digits integer.
    :param str recipient_pan: **Required**. Recipient primary account number (PAN). 13-19 characters string.
    :param float amount: **Required**. Transaction amount. 12 digits, 3 fractions.
    :param int mcc: **Optional**. Merchant category code, populated by Originator. 4 digits integer. **6012** for mVISA.
    :param int acquiring_bin: **Required**. Business identification number. 6-11 digits integer.
    :param int acquirer_country_code: **Required**. Country `ISO code <https://developer.visa.com/request_response_codes#isoCodes>`_ 
        of originator BIN. 3 digits integer.
    :param float transaction_fee_amount: **Required**. Convenience fee amount. 8 digits, 3 fractions. 
    :param CardAcceptor card_acceptor: **Required**. Instance of :func:`~pyvdp.visadirect.CardAcceptor` data object.
    :param str transaction_currency_code: **Required**. Transaction currency `ISO code <https://developer.visa.com/request_response_codes#isoCodes>`_.
        3 characters string.
    :param PurchaseIdentifier purchase_id: **Required**. Instance of :func:`~pyvdp.visadirect.mvisa.PurchaseIdentifier` 
        data object.
    :param str secondary_id: **Conditional**. Second field with additional transaction data. Max 28 characters string. 
    :param str business_application_id: **Required**. Business application identifier. **MP** for merchant payments 
        operations. See `BAI codes <https://developer.visa.com/request_response_codes#businessApplicationId>`_ for 
        details.
    :param str sender_reference: **Optional**. Unique agent reference. Max 16 characters string.
    :param str sender_account_number: **Required**. Sender account number. Max 34 characters string.
    :param str sender_name: **Required**. Agent name. Max 30 characters string.

    **Example:**
        ..  code-block:: json

            {
                "acquirerCountryCode": "356",
                "acquiringBin": "408972",
                "amount": "124.05",
                "businessApplicationId": "MP",
                "cardAcceptor": {
                    "address": {
                        "city": "KOLKATA",
                        "country": "IND"
                    },
                    "idCode": "CA-IDCode-77765",
                    "name": "Visa Inc. USA-Foster City"
                },
                "feeProgramIndicator": "123",
                "localTransactionDateTime": "2017-03-17T05:51:16",
                "purchaseIdentifier": {
                    "referenceNumber": "REF_123456789123456789123",
                    "type": "1"
                },
                "recipientName": "Jasper",
                "recipientPrimaryAccountNumber": "4123640062698797",
                "retrievalReferenceNumber": "412770451035",
                "secondaryId": "123TEST",
                "senderAccountNumber": "4027290077881587",
                "senderName": "Jasper",
                "senderReference": "",
                "systemsTraceAuditNumber": "451035",
                "transactionCurrencyCode": "INR",
                "transactionIdentifier": "381228649430015"
            }
    """

    # Mappings between constructor arguments and VISA API fields
    # {'constructor argument': 'VISA API field name'}
    ATTR_MAPPINGS = {
        'recipient_pan': 'recipientPrimaryAccountNumber',
        'amount': 'amount',
        'mcc': 'merchantCategoryCode',
        'acquiring_bin': 'acquiringBin',
        'acquirer_country_code': 'acquirerCountryCode',
        'transaction_fee_amount': 'transactionFeeAmount',
        'card_acceptor': 'cardAcceptor',
        'transaction_currency_code': 'transactionCurrencyCode',
        'purchase_id': 'purchaseIdentifier',
        'secondary_id': 'secondaryId',
        'business_application_id': 'businessApplicationId',
        'sender_reference': 'senderReference',
        'sender_name': 'senderName',
        'sender_account_number': 'senderAccountNumber'
    }

    def __init__(self, **kwargs):
        super(MerchantPushPaymentTransaction, self).__init__(kwargs['stan'])
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)


class PurchaseIdentifier(object):
    """VisaDirect mVISA PurchaseIdentifier data object model.

    Used as a part of :func:`~pyvdp.visadirect.mvisa.MerchantPushPaymentTransaction`.

    :param str type: **Required**. Primary ID as defined by mVISA. 1 character string.
    :param str reference_number: **Required**. Key data element for matching a message to others within a given
        transaction set. Value will be the same as what has been provided in the request. Max 13 characters string.
    """

    ATTR_MAPPINGS = {
        'type': 'type',
        'reference_number': 'referenceNumber',
    }

    def __init__(self, **kwargs):
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)
