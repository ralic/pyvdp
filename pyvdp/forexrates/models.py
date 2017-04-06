class ForeignExchangeRatesModel(object):
    """Foreign Exchange Rates data object model.
    
    https://developer.visa.com/products/foreign_exchange/reference
    
    :param str destination_cur_code: **Required**. Source currency `ISO code <https://developer.visa.com/request_response_codes#isoCodes>`_.
        3 characters string.
    :param str source_cur_code: **Required**. Destination currency `ISO code <https://developer.visa.com/request_response_codes#isoCodes>`_.
        3 characters string.
    :param float source_amount: **Required**. Amount of source currency to exchange. 3 digits, 2 fractions float. 
    :param str markup_rate: **Optional**. Exchange markup rate if client wants to apply a certain markup rate.
        0-6 characters string. E.g. 0.07 equals to 0.07% markup rate.
    :param int stan: **Optional**. Systems Trace Audit Number. 6 digits integer.
    :param int acquiring_bin: **Optional**. Acquiring BIN for funds transfer operations. 6-11 digits integer.
    :param str acquirer_country_code: **Optional**. Acquirer `ISO country code <https://developer.visa.com/request_response_codes#isoCodes>`_ 
        for BIN provided. 3 characters numeric string.
    :param CardAcceptor card_acceptor: **Optional**. Instance of :func:`~pyvdp.visadirect.CardAcceptor`
    """
    ATTR_MAPPINGS = {
        'destination_cur_code': 'destinationCurrencyCode',
        'source_cur_code': 'sourceCurrencyCode',
        'source_amount': 'sourceAmount',
        'markup_rate': 'markUpRate',
        'stan': 'systemsTraceAuditNumber',
        'acquiring_bin': 'acquiringBin',
        'acquirer_country_code': 'acquirerCountryCode',
        'card_acceptor': 'cardAcceptor'
    }

    def __init__(self, **kwargs):
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)