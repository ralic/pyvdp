from pyvdp.vmorc.dispatcher import VisaMerchantOffersResourceCenterDispatcher


def get(data):
    """Visa Merchant Offers Resource Center Offers Data API - Offers by Content Id.
    
    Retrieves current offers by Content Id.
    
    :param ByContentIdModel data: **Required**. 
        Instance of :func:`pyvdp.vmorc.offers.ByContentIdModel`. 
    :return: response from VDP.
    
    **Usage:**
    
    ..  code:: python
    
        from pyvdp.vmorc.offers import ByContentIdModel, bycontentid
        
        data_kwargs = {
            "contentid": 105513,
            "updatefrom": 20160801,
        }
        
        data = ByContentIdModel(**data_kwargs)
        
        result = bycontentid.get(data)
        print(result)
    """
    c = VisaMerchantOffersResourceCenterDispatcher(resource='vmorc',
                                                   api='offers',
                                                   version='v1',
                                                   method='bycontentid',
                                                   http_verb='GET',
                                                   auth_method='ssl',
                                                   data=data)

    return c.send()
