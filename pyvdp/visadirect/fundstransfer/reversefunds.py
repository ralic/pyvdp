from pyvdp.visadirect import VisaDirectDispatcher


API = 'fundstransfer'
METHOD = 'reversefundstransactions'


def send(data, multi=False):
    """Submits a ReverseFunds request.

    :param data: **Required**. Instance of :func:`~visa.visadirect.fundstransfer.ReverseFundsTransaction` or 
        :func:`~visa.visadirect.fundstransfer.MultiReverseFundsTransaction`.
    :param bool multi: **Conditional**. Indicates that transaction is a batch 
        (:func:`~visa.visadirect.fundstransfer.MultiReverseFundsTransaction`).
    :return: Dictionary with VDP API response.
    """
    method = METHOD

    if multi:
        method = 'multireversefundstransactions'

    c = VisaDirectDispatcher(api=API, method=method, http_verb='POST', data=data)
    return c.send()


def get(query, multi=False):
    """Fetches a status of previously submitted ReverseFunds request.

    Returns a status of :func:`~pyvdp.visadirect.fundstransfer.ReverseFundsTransaction` or  
    :func:`~pyvdp.visadirect.fundstransfer.MultiReverseFundsTransaction` request by transaction identifier, returned 
    with 202 response.

    :param str query: **Required**. Transaction status identifier.
    :param bool multi: **Conditional**. Indicates that transaction is a batch 
        (:func:`~pyvdp.visadirect.fundstransfer.MultiReverseFundsTransaction`)
    :return: Dictionary with VDP API response
    """
    method = METHOD

    if multi:
        method = 'multireversefundstransactions'

    query_string = '/' + query

    c = VisaDirectDispatcher(api=API, method=method, http_verb='GET', query_string=query_string)
    return c.send()
