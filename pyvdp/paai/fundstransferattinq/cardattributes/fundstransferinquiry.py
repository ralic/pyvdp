from pyvdp.paai.request import PaaiRequest


API = 'fundstransferattinq'
METHOD = 'cardattributes/fundstransferinquiry'


def send(data):
    """Submits Funds Transfer Inquiry request.

    :param data: **Required**. Instance of :func:`~visa.paai.fundstransferattinq.cardattributes.data.FundsTransferInquiryData`
    :return: Dictionary with VDP response
    """
    c = PaaiRequest(api=API, method=METHOD, http_verb='POST', data=data)
    return c.send()
