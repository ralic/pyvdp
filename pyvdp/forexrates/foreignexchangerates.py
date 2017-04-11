from .dispatcher import VisaForexRatesDispatcher


def send(data):
    """Submits a Forex Rates Exchange request.

    :param ForeignExchangeRatesModel data: **Required**. 
        Instance of :func:`~pyvdp.forexrates.ForeignExchangeRatesModel`.
    :return: A response from VDP.
    
    **Usage:**
    
    ..  code-block:: python
    
            from pyvdp.forexrates import foreignexchangerates, ForeignExchangeRatesModel
    
            fex_kwargs = {
                'destination_cur_code': '840',
                'source_amount': 100.00,
                'source_cur_code': 643
            }
    
            fex = ForeignExchangeRatesModel(**fex_kwargs)
            result = foreignexchangerates.send(data=fex)
            print(result)
    """
    c = VisaForexRatesDispatcher(data=data)
    return c.send()
