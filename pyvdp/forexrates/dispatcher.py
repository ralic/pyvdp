from pyvdp.dispatcher import VisaDispatcher


class VisaForexRatesDispatcher(VisaDispatcher):
    """Implements HTTP requests to Visa Foreign Exchange Rates APIs.

    https://developer.visa.com/products/foreign_exchange

    :param str query_string: **Conditional**. Query string to append to URL
    :param MerchantSearch data: **Conditional**. Instance of :func:`~pyvdp.forexrates.ForeignExchangeRatesModel` 
    :param dict headers: **Optional**. Additional headers as dictionary
    """

    def __init__(self, query_string='', data=None, headers=None):

        super(VisaForexRatesDispatcher, self).__init__(resource='forexrates',
                                                       api='',
                                                       method='foreignexchangerates',
                                                       http_verb='POST',
                                                       query_string=query_string,
                                                       data=data,
                                                       headers=headers)
