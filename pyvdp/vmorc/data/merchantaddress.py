from pyvdp.vmorc.dispatcher import VisaMerchantOffersResourceCenterDispatcher


def get(data):
    """Visa Merchant Offers Resource Center Reference Data API - Data By Merchant Address.

    Retrieves data by Merchant Address.

    :param MerchantAddressModel data: **Required**. 
        Instance of :func:`pyvdp.vmorc.data.MerchantAddressModel`. 
    :return: response from VDP.

    **Usage:**

    ..  code:: python

        from pyvdp.vmorc.data import MerchantAddressModel, merchantaddress
        
        data_kwargs = {
            "merchantIds": "101456,101457",
            "start_index": 2
        }

        data = MerchantAddressModel(**data_kwargs)

        result = merchantaddress.get(data)
        print(result)
    """
    c = VisaMerchantOffersResourceCenterDispatcher(resource='vmorc',
                                                   api='data',
                                                   version='v1',
                                                   method='merchantAddress',
                                                   http_verb='GET',
                                                   auth_method='ssl',
                                                   data=data)

    return c.send()
