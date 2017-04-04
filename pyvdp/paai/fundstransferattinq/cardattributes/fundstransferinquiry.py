from pyvdp.paai.dispatcher import VisaPaaiDispatcher


API = 'fundstransferattinq'
METHOD = 'cardattributes/fundstransferinquiry'


def send(data):
    """Submits Funds Transfer Inquiry request.

    :param data: **Required**. Instance of :func:`~pyvdp.paai.fundstransferattinq.cardattributes.FundsTransferInquiryData`
    :return: Dictionary with VDP response
    """
    c = VisaPaaiDispatcher(api=API, method=METHOD, http_verb='POST', data=data)
    return c.send()
