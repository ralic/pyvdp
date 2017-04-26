from pyvdp.vmorc.dispatcher import VisaMerchantOffersResourceCenterDispatcher


def get(data):
    """Visa Merchant Offers Resource Center Offers Data API - Offers by Filter.

    Retrieves current offers by Filter.

    :param ByFilterModel data: **Required**. Instance of :func:`pyvdp.vmorc.offers.ByFilterModel`. 
    :return: response from VDP.

    **Usage:**

    ..  code:: python

        from pyvdp.vmorc.offers import ByFilterModel, byfilter

        data_kwargs = {
            "business_segment": 7,
        }

        data = ByFilterModel(**data_kwargs)

        result = byfilter.get(data)
        print(result)
    """
    c = VisaMerchantOffersResourceCenterDispatcher(resource='vmorc',
                                                   api='offers',
                                                   version='v1',
                                                   method='byfilter',
                                                   http_verb='GET',
                                                   auth_method='ssl',
                                                   data=data)

    return c.send()
