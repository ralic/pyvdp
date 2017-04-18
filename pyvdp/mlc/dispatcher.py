from pyvdp.dispatcher import VisaDispatcher


class VisaMobileLocationConfirmationDispatcher(VisaDispatcher):
    """Implements HTTP requests to Visa Mobile Location Confirmation APIs.

    https://developer.visa.com/products/mlc/guides

    :param data: **Required**. Instance of MLC model.
    :param dict headers: **Optional**. Additional headers as dictionary
    """

    def __init__(self, api, method, data=None, headers=None):

        super(VisaMobileLocationConfirmationDispatcher, self).__init__(resource='mlc',
                                                                       api=api,
                                                                       method=method,
                                                                       http_verb='POST',
                                                                       data=data,
                                                                       headers=headers)

