from .dispatcher import VisaMerchantMeasurementDispatcher


def send(data):
    """Submits a Merchant Search request.

    :param RetrieveMetricsPayloadModel data: **Required**. 
        Instance of :func:`~pyvdp.merchantmeasurement.RetrieveMetricsPayloadModel`.
    :return: A response from VDP.
    
    **Usage:**
    
    ..  code-block:: python
    
        from pyvdp.merchantmeasurement import merchantbenchmark, RetrieveMetricsPayloadModel
        
        data_kwargs = {
            'merchantCategoryCodes': ['5812'],
            'merchantCategoryGroupsCodes': [''],
            'zipList': ['77027'],
            'msaList': [''],
            'countryList': [''],
            'monthList': ['201501'],
            'groupList': ['standard'],
            'cardPresentIndicator': '2'
        }
                
        rmpm_kwargs = {
            'requestData': RetrieveMetricsPayloadModel.RequestData(**data_kwargs)
        }
        
        rmpm = RetrieveMetricsPayloadModel(**rmpm_kwargs)
        
        result = merchantbenchmark.send(data=rmpm)    
    """
    c = VisaMerchantMeasurementDispatcher(data=data)
    return c.send()
