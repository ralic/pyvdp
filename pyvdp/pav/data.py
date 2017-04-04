class PavData(object):
    """Visa Payment Account Validation Object data object model.

    :param int stan: **Required**. Systems Trace Audit Number (STAN), 6-digits integer.
    :param str pan: **Required**. Primary Account Number (PAN), 13-19 digits string.
    :param str card_expiry_date: **Conditional**. Card expiration date, YYYY-MM. Required when cvv2 is present.
    :param PavAddressVerificationResults avr: **Conditional**. Instance of :func:`~pyvdp.pav.PavData.PavAddressVerificationResults`
    :param str cvv2: **Conditional**. Card CVV2 value. 3-4 characters string.
    :param int acquiring_bin: **Optional**. Bank identification number under which a funds transfer is registered.
        6-11 digits integer.
    :param int acquirer_country_code: **Optional**. `ISO country code <https://developer.visa.com/request_response_codes#isoCodes>`_ 
        for acquiring bank. 3 digits integer.
    :param CardAcceptor card_acceptor: **Optional**. Instance of :func:`~pyvdp.visadirect.CardAcceptor`.

    **Example:**
        ..  code-block:: json

            {
                "addressVerificationResults": {
                    "postalCode": "T4B 3G5",
                    "street": "2881 Main Street Sw"
                },
                "cardAcceptor": {
                    "address": {
                        "city": "fostr city",
                        "country": "PAKISTAN",
                        "county": "CA",
                        "state": "CA",
                        "zipCode": "94404"
                    },
                    "idCode": "111111",
                    "name": "rohan",
                    "terminalId": "123"
                },
                "cardCvv2Value": "672",
                "cardExpiryDate": "2018-06",
                "primaryAccountNumber": "4957030000313108",
                "retrievalReferenceNumber": "015221743720",
                "systemsTraceAuditNumber": "743720"
            }
    """
    ATTR_MAPPINGS = {
        'stan': 'systemsTraceAuditNumber',
        'pan': 'primaryAccountNumber',
        'card_expiry_date': 'cardExpiryDate',
        'avr': 'addressVerificationResults',
        'cvv2': 'cardCvv2Value',
        'acquiring_bin': 'acquiringBin',
        'acquirer_country_code': 'acquirerCountryCode',
        'card_acceptor': 'cardAcceptor'
    }

    def __init__(self, **kwargs):
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)

    class AddressVerificationResults(object):
        """AddressVerificationResults data object model.
        
        A subclass for Payment Account Validation data object model.
        
        :param str street: **Conditional**. Street address for card holder. Required when :func:`~pyvdp.pav.PavData.cvv2`
            is not present. 1-20 characters string.
        :param str postal_code: **Conditional**. Postal code for card holder address. Required when 
            :func:`~pyvdp.pav.PavData.cvv2` is not present. 1-20 characters string. 
        """
        ATTR_MAPPINGS = {
            'street': 'street',
            'postal_code': 'postalCode',
        }

        def __init__(self, **kwargs):
            self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)
