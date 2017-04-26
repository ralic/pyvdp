from pyvdp.vmorc.dispatcher import VisaMerchantOffersResourceCenterDispatcher


def get(data):
    """Visa Merchant Offers Resource Center Reference Data API - Data By Merchant.

    Retrieves data by Merchant.

    :param MerchantModel data: **Required**. 
        Instance of :func:`pyvdp.vmorc.data.MerchantModel`. 
    :return: response from VDP.

    **Usage:**

    ..  code:: python

        from pyvdp.vmorc.data import MerchantModel, merchant

        data_kwargs = {
            "program": 100760
        }

        data = MerchantModel(**data_kwargs)

        result = merchant.get(data)
        print(result)
    """
    c = VisaMerchantOffersResourceCenterDispatcher(resource='vmorc',
                                                   api='data',
                                                   version='v1',
                                                   method='merchant',
                                                   http_verb='GET',
                                                   auth_method='ssl',
                                                   data=data)

    return c.send()
