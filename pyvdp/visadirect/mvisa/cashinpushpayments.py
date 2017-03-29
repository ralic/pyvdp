from pyvdp.visadirect import VisaDirectRequest


API = 'mvisa'
METHOD = 'cashinpushpayments'


def send(data):
    """Submits VisaDirect mVISA CashinPushPayments request.

    :param CashinPushPaymentTransaction data: **Required**. Instance of CashinPushPaymentTransaction.
    :return: Dictionary with VDP API response.
    """
    c = VisaDirectRequest(api=API, method=METHOD, http_verb='POST', data=data)
    return c.send()


def get(query):
    """Sends VisaDirect mVISA CashinPushPayments request.

    :param str query: **Required**. Transaction status identifier.
    :return: Dictionary with VDP API response
    """
    query_string = '/' + query

    c = VisaDirectRequest(api=API, method=METHOD, http_verb='GET', query_string=query_string)
    return c.send()
