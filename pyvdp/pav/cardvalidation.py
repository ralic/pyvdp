from pyvdp.pav import VisaPavDispatcher


def send(data):
    """Submits a payment account validation request.

    :param PavTransaction data: **Required**. Instance of :func:`~pyvdp.pav.PavData`.
    :return: A response from VDP.
    """
    c = VisaPavDispatcher(method='cardvalidation', http_verb='post', data=data)
    return c.send()
