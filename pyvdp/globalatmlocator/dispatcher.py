from pyvdp.dispatcher import VisaDispatcher


class VisaGlobalAtmLocatorDispatcher(VisaDispatcher):
    """Implements HTTP requests to Visa Global ATM Locator APIs.

    https://developer.visa.com/products/atmlocator/guides
    """
    def __init__(self, method, query_string='', data=None, headers=None):
        super(VisaGlobalAtmLocatorDispatcher, self).__init__(resource='globalatmlocator',
                                                             api='',
                                                             method=method,
                                                             http_verb='POST',
                                                             query_string=query_string,
                                                             data=data,
                                                             headers=headers)

