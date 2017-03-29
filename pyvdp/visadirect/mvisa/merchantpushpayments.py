from pyvdp.visadirect.request import VisaDirectRequest


API = 'mvisa'
METHOD = 'merchantpushpayments'


def send(data):
    """Submits VisaDirect mVISA MerchantPushPayments request.

    :param MerchantPushPaymentTransaction data: **Required**. Instance of MerchantPushPaymentTransaction.
    :return: Dictionary with VDP API response.
    """
    c = VisaDirectRequest(api=API, method=METHOD, http_verb='POST', data=data)
    return c.send()


def get(query):
    """Sends VisaDirect mVISA MerchantPushPayments request.

    :param str query: **Required**. Transaction status identifier.
    :return: Dictionary with VDP API response
    """
    query_string = '/' + query

    c = VisaDirectRequest(api=API, method=METHOD, http_verb='GET', query_string=query_string)
    return c.send()
