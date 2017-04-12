from pyvdp.dispatcher import VisaDispatcher


class VisaMerchantLocatorDispatcher(VisaDispatcher):
    """Implements HTTP requests to Visa Merchant Locator APIs.

    https://developer.visa.com/products/merchant_locator/guides

    :param str query_string: **Conditional**. Query string to append to URL
    :param MerchantLocatorModel data: **Conditional**. 
        Instance of :func:`~pyvdp.merchantlocator.MerchantLocatorModel` 
    :param dict headers: **Optional**. Additional headers as dictionary
    """

    def __init__(self, query_string='', data=None, headers=None):

        super(VisaMerchantLocatorDispatcher, self).__init__(resource='merchantlocator',
                                                            api='',
                                                            method='locator',
                                                            http_verb='POST',
                                                            query_string=query_string,
                                                            data=data,
                                                            headers=headers)

