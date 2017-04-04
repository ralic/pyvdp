from pyvdp.paai.dispatcher import VisaPaaiDispatcher


API = 'generalattinq'
METHOD = 'cardattributes/generalinquiry'


def send(data):
    """Submits General Card Attributes Inquiry request.

    :param data: **Required**. Instance of :func:`~pyvdp.paai.generalattinq.cardattributes.GeneralInquiryData`
    :return: Dictionary with VDP response
    """
    c = VisaPaaiDispatcher(api=API, method=METHOD, http_verb='POST', data=data)
    return c.send()
