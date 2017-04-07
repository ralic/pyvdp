from pyvdp.visadirect import VisaDirectDispatcher

API = 'fundstransfer'
METHOD = 'pullfundstransactions'


def send(data, multi=False):
    """Submits a PullFunds (AFT) request.

    :param data: **Required**. Instance of :func:`~pyvdp.visadirect.fundstransfer.PullFundsTransactionModel` or 
        :func:`~pyvdp.visadirect.fundstransfer.MultiPullFundsTransactionModel`.
    :param bool multi: **Conditional**. Indicates that transaction is a batch 
        (:func:`~pyvdp.visadirect.fundstransfer.MultiPullFundsTransactionModel`)
    :return: Dictionary with VDP API response
    """
    method = METHOD

    if multi:
        method = 'multipullfundstransactions'

    c = VisaDirectDispatcher(api=API, method=method, http_verb='POST', data=data)
    response = c.send()

    return response


def get(query, multi=False):
    """Fetches a status of previously submitted PullFunds request.
    
    Returns a status of :func:`~pyvdp.visadirect.fundstransfer.PullFundsTransactionModel` or  
    :func:`~pyvdp.visadirect.fundstransfer.MultiPullFundsTransactionModel` request by transaction identifier, returned with 
    202 response.

    :param str query: **Required**. Transaction status identifier.
    :param bool multi: **Conditional**. Indicates that transaction is a batch 
        (:func:`~pyvdp.visadirect.fundstransfer.MultiPullFundsTransactionModel`)
    :return: Dictionary with VDP API response
    """

    method = METHOD

    if multi:
        method = 'multipullfundstransactions'

    query_string = '/' + query

    c = VisaDirectDispatcher(api=API, method=method, http_verb='GET', query_string=query_string)
    return c.send()
