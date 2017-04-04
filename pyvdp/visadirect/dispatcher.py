from pyvdp.dispatcher import VisaDispatcher


class VisaDirectDispatcher(VisaDispatcher):
    """Implements HTTP requests to Visa Direct APIs.

    https://developer.visa.com/products/visa_direct/guides

    :param str api: **Required**. VDP API name
    :param str method: **Required**. VDP API method name
    :param str http_verb: **Required**. VDP API HTTP verb (GET, POST)
    :param str query_string: **Conditional**. Query string to append to URL
    :param object data: **Conditional**. Payload for POST/PUT requests
    :param dict headers: **Optional**. Additional headers as dictionary
    """

    def __init__(self, api, method, http_verb, query_string='', data=None, headers=None):

        super(VisaDirectDispatcher, self).__init__(resource='visadirect',
                                                   api=api,
                                                   method=method,
                                                   http_verb=http_verb,
                                                   query_string=query_string,
                                                   data=data,
                                                   headers=headers)
