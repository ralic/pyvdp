from .dispatcher import VisaForexRatesDispatcher


def send(data):
    """Submits a Forex Rates Exchange request.

    :param ForeignExchangeRatesModel data: **Required**. 
        Instance of :func:`~pyvdp.forexrates.ForeignExchangeRatesModel`.
    :return: Response from VDP.
    
    **Usage:**
    
    ..  code-block:: python
    
            from pyvdp.forexrates import foreignexchangerates, ForeignExchangeRatesModel
    
            data_kwargs = {
                'destinationCurrencyCode': '840',
                'sourceAmount': 100.00,
                'sourceCurrencyCode': 643
            }
    
            data = ForeignExchangeRatesModel(**data_kwargs)
            result = foreignexchangerates.send(data)
            print(result)
    """
    c = VisaForexRatesDispatcher(resource='forexrates',
                                 api='',
                                 method='foreignexchangerates',
                                 http_verb='POST',
                                 auth_method='ssl',
                                 data=data)
    return c.send()
