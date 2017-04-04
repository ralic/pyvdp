from pyvdp.visadirect import VisaDirectDispatcher


API = 'fundstransfer'
METHOD = 'pushfundstransactions'


def send(data, multi=False):
    """Submits a PushFunds (OCT) request.

    :param data: **Required**. Instance of :func:`~pyvdp.visadirect.fundstransfer.PushFundsTransaction` or 
        :func:`~pyvdp.visadirect.fundstransfer.MultiPushFundsTransaction`.
    :param bool multi: **Conditional**. Indicates that transaction is a batch 
        (:func:`~pyvdp.visadirect.fundstransfer.MultiPushFundsTransaction`).
    :return: Dictionary with VDP API response.
    """
    method = METHOD

    if multi:
        method = 'multipushfundstransactions'

    c = VisaDirectDispatcher(api=API, method=method, http_verb='POST', data=data)
    return c.send()


def get(query, multi=False):
    """Fetches a status of previously submitted PushFunds request.

    Returns a status of :func:`~pyvdp.visadirect.fundstransfer.PushFundsTransaction` or  
    :func:`~pyvdp.visadirect.fundstransfer.MultiPushFundsTransaction` request by transaction identifier, returned with 
    202 response.

    :param str query: **Required**. Transaction status identifier.
    :param bool multi: **Conditional**. Indicates that transaction is a batch 
        (:func:`~pyvdp.visadirect.fundstransfer.MultiPushFundsTransaction`)
    :return: Dictionary with VDP API response
    """
    method = METHOD

    if multi:
        method = 'multipushfundstransactions'

    query_string = '/' + query

    c = VisaDirectDispatcher(api=API, method=method, http_verb='GET', query_string=query_string)
    return c.send()
