from pyvdp.vmorc.dispatcher import VisaMerchantOffersResourceCenterDispatcher


def get(data):
    """Visa Merchant Offers Resource Center Offers Data API - Offers by Offer Id.
    
    Retrieves current offers by Offer Id.
    
    :param ByOfferIdModel data: **Required**. Instance of :func:`pyvdp.vmorc.offers.ByOfferIdModel`. 
    :return: response from VDP.
    
    **Usage:**
    
    ..  code:: python
    
        from pyvdp.vmorc.offers import ByOfferIdModel, byofferid
        
        data_kwargs = {
            "offerid": 102355,
            "updatefrom": 20160801,
        }
        
        data = ByOfferIdModel(**data_kwargs)
        
        result = byofferid.get(data)
        print(result)
    """
    c = VisaMerchantOffersResourceCenterDispatcher(resource='vmorc',
                                                   api='offers',
                                                   version='v1',
                                                   method='byofferid',
                                                   http_verb='GET',
                                                   auth_method='ssl',
                                                   data=data)

    return c.send()
