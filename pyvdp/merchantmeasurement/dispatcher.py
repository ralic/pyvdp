from pyvdp.dispatcher import VisaDispatcher


class VisaMerchantMeasurementDispatcher(VisaDispatcher):
    """Implements HTTP requests to Visa MerchantMeasurement APIs.

    https://developer.visa.com/products/merchant_measurement/guides

    :param str query_string: **Conditional**. Query string to append to URL
    :param RetrieveMetricsPayloadModel data: **Conditional**. 
        Instance of :func:`~pyvdp.merchantmeasurement.RetrieveMetricsPayloadModel` 
    :param dict headers: **Optional**. Additional headers as dictionary
    """

    def __init__(self, query_string='', data=None, headers=None):

        super(VisaMerchantMeasurementDispatcher, self).__init__(resource='merchantmeasurement',
                                                                api='',
                                                                method='merchantbenchmark',
                                                                http_verb='POST',
                                                                query_string=query_string,
                                                                data=data,
                                                                headers=headers)

