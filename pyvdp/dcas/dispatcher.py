from pyvdp.dispatcher import VisaDispatcher


class VisaDcasDispatcher(VisaDispatcher):
    """Implements HTTP requests to Visa Digital Card and Accounts APIs.

    https://developer.visa.com/products/dcas/guides

    :param str query_string: **Conditional**. Query string to append to URL
    :param CardInquiryModel data: **Conditional**. 
        Instance of :func:`~pyvdp.dcas.cardinquiry.accounts.CardInquiryModel` 
    :param dict headers: **Optional**. Additional headers as dictionary
    """
    def __init__(self, api, method, http_verb, query_string='', data=None, headers=None):
        super(VisaDcasDispatcher, self).__init__(resource='dcas',
                                                 api=api,
                                                 method=method,
                                                 http_verb=http_verb,
                                                 query_string=query_string,
                                                 data=data,
                                                 headers=headers)
