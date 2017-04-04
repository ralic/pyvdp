from pyvdp.merchantsearch import MerchantSearchData, VisaMerchantSearchRequest


def send(data):
    """Submits a Merchant Search request.

    :param MerchantSearchData data: **Required**. Instance of :func:`~pyvdp.merchantsearch.MerchantSearchData`.
    :return: A response from VDP.
    """
    c = VisaMerchantSearchRequest(data=data)
    return c.send()
