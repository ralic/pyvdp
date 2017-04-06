from .dispatcher import VisaForexRatesDispatcher


def send(data):
    """Submits a Forex Rates Exchange request.

    :param ForeignExchangeRatesModel data: **Required**. Instance of :func:`~pyvdp.forexrates.ForeignExchangeRatesModel`.
    :return: A response from VDP.
    """
    c = VisaForexRatesDispatcher(data=data)
    return c.send()
