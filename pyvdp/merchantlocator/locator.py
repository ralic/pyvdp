from .dispatcher import VisaMerchantLocatorDispatcher


def send(data):
    """Submits a MerchantLocator request.

    :param MerchantLocatorModel data: **Required**. 
        Instance of :func:`~pyvdp.merchantlocator.MerchantLocatorModel`.
    :return: A response from VDP.
    
    **Usage:**
    
    ..  code-block:: python
    
            from pyvdp.merchantlocator import locator, MerchantLocatorModel
            
            search_attrs_kwargs = {
                "merchantName": "Starbucks",
                "merchantCountryCode": "840",
                "latitude": "37.363922",
                "longitude": "-121.929163",
                "distance": "2",
                "distanceUnit": "M"            
            }
            
            search_options_kwargs = {
                "maxRecords": "5",
                "matchIndicators": "true",
                "matchScore": "true"            
            }
            
            mlm_kwargs = {
                "searchAttrList": MerchantLocatorModel.SearchAttrList(**search_attrs_kwargs),
                "searchOptions": MerchantLocatorModel.SearchOptions(**search_options_kwargs),
                "responseAttrList": ["GNLOCATOR"]
            }
            
            data = MerchantLocatorModel(**mlm_kwargs)            
            result = locator.send(data=data)
            print(result)
    """
    c = VisaMerchantLocatorDispatcher(data=data)
    return c.send()
