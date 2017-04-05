from datetime import datetime

try:
    import configparser as parser
except ImportError:
    import ConfigParser as parser

transaction_datetime = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


class VisaDirectTransaction(object):
    """Abstract VISA Transaction object model.

    Constructs and populates general attributes, such as systemsTraceAuditNumber (stan), retrievalReferenceNumber
    (rrn) and localTransactionDateTime.

    :param str stan: **Required**. Systems Trace Audit Number (STAN), 6 digits integer.
    """
    def __init__(self, stan):
        self.systemsTraceAuditNumber = stan
        self.localTransactionDateTime = transaction_datetime
        self.retrievalReferenceNumber = self._get_rrn()

    def _get_rrn(self):
        """Generates RRN (retrievalReferenceNumber).

        :return: str rrn: Last digit of current year + number of current day in the year + current hour + STAN
        """
        now = datetime.now()
        year_last_digit = now.strftime('%Y')[3]
        day_of_the_year = now.strftime('%j')
        current_hour = now.strftime('%H')

        return year_last_digit + day_of_the_year + current_hour + str(self.systemsTraceAuditNumber)


class VisaDirectTransactionBatch(object):
    """Abstract TransactionBatch object model.

    Constructs and populates a 'transaction of transactions', normally submitted with `multi` requests.
    This class is not supposed to be instantiated on its own, it is just providing a `shell` for batch requests

    :param list request: **Required**. List of :func:`~pyvdp.visadirect.VisaDirectTransaction` objects.
    """
    def __init__(self, request):
        self.localTransactionDateTime = transaction_datetime
        self.request = request


class CardAcceptor(object):
    """Card Acceptor object model.

    :param str name: **Required**. Name of the originator or money transfer operator. Max 25 characters string.
    :param str terminal_id: **Required**. Identifier of the terminal at a card acceptor location. Max 8 characters
        string.
    :param str id_code: **Required**. Identifier of card acceptor (Visa Direct Originator). Max 15 characters string.
    :param dict address: **Required**. See :func:`~pyvdp.visadirect.CardAcceptor.CardAcceptorAddress` class for 
        allowed keys.
    """

    ATTR_MAPPINGS = {
        'name': 'name',
        'terminal_id': 'terminalId',
        'id_code': 'idCode',
        'address': 'address'
    }

    def __init__(self, **kwargs):
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)

        try:
            self.address = self.CardAcceptorAddress(**kwargs['address'])
        except KeyError:
            # If address is missing, skip silently, errors will be handled by VDP
            pass

    class CardAcceptorAddress(object):
        """Card Acceptor address object model (part of :func:`~pyvdp.visadirect.CardAcceptor` object).

        Populated from `address` dictionary argument for :func:`~pyvdp.visadirect.CardAcceptor` class ctor.

        :param str country: **Required**. Address country `ISO code <https://developer.visa.com/request_response_codes#isoCodes>`_.
            3 characters string.
        :param str county: **Optional**. Address county code. 3 characters string.
        :param str zip_code: **Conditional**. Address ZIP code. 5-9 characters string.
        :param str state: **Condtional**. Address state code. 2 characters string.
        :param str city: **Conditional**. Agent city name. Max 13 characters string. 
        """
        ATTR_MAPPINGS = {
            'country': 'country',
            'zip_code': 'zipCode',
            'state': 'state',
            'county': 'county',
            'city': 'city'
        }

        def __init__(self, **kwargs):
            self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)


class OriginalDataElements(object):
    """Object model for Original Data Elements object, used for reverse transactions.

    https://en.wikipedia.org/wiki/ISO_8583#Data_elements

    :param int stan: **Required**. Systems trace audit number, 6 digits integer.
    :param int acquiring_bin: **Required**. Original AFT acquiring BIN value. 6-11 digits integer.
    :param str transmission_datetime: **Required**. Original AFT Datetime YYYY-MM-DDThh:mm:ss
    :param str approval_code: **Optional**. Approval code from original AFT, 6 characters string.
    """
    ATTR_MAPPINGS = {
        'stan': 'systemsTraceAuditNumber',
        'approval_code': 'approvalCode',
        'transmission_datetime': 'transmissionDateTime',
        'acquiring_bin': 'acquiringBin'
    }

    def __init__(self, **kwargs):
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)


class PointOfServiceData(object):
    """Object model for PointOfServiceData data object.

    Optional data structure, included in VisaDirect transactions.

    :param int pan_entry_mode: **Optional**. Required for Card Present scenarios. 1 digit integer.
    :param int condition_code: **Optional**. Required for Card Present scenarios. 2 digits integer.
    :param str moto_eci_indicator: **Optional**. If posConditionCode is 59, motoECIIndicator must be between 5-8.
        Default is set to 5 if not provided. If posConditionCode is 0, motoECIIndicator will not be sent. 1 character
        string.
    """

    ATTR_MAPPINGS = {
        'pan_entry_mode': 'panEntryMode',
        'condition_code': 'posConditionCode',
        'moto_eci_indicator': 'motoECIIndicator'
    }

    def __init__(self, **kwargs):
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)


class PointOfServiceCapability(object):
    """Object model for PointOfServiceCapability data object.

    Optional data structure, included in VisaDirect transactions.

    :param int type: **Optional**. For Card Present scenarios valid values are 0,3,4. For CNP - 5. 1 digit integer.
    :param int entry_capability: **Optional**. For CP valid values are 0,2,9. For CNP - 5. 1 digit integer.
    """

    ATTR_MAPPINGS = {
        'type': 'posTerminalType',
        'entry_capability': 'posTerminalEntryCapability',
    }

    def __init__(self, **kwargs):
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)


class MerchantVerificationValue(object):
    """Object model for MerchantVerificationValue data object.

    Optional data structure, included in VisaDirect transactions.

    :param str visa_assigned: Visa assigned MVV value. 6 characters hexbin string.
    :param str acquirer_assigned: Visa assists the acquirer in assigning the last four. 4 characters hexbin string.
    """

    ATTR_MAPPINGS = {
        'acquirer_assigned': 'mvvAcquirerAssigned',
        'visa_assigned': 'mvvVisaAssigned'
    }

    def __init__(self, **kwargs):
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)
