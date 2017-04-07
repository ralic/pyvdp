from pyvdp.merchantsearch import VisaMerchantSearchDispatcher


def send(data):
    """Submits a Merchant Search request.

    :param MerchantSearch data: **Required**. Instance of :func:`~pyvdp.merchantsearch.MerchantSearchData`.
    :return: A response from VDP.
    """
    c = VisaMerchantSearchDispatcher(data=data)
    return c.send()
