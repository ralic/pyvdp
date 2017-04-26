from pyvdp.vmorc.dispatcher import VisaMerchantOffersResourceCenterDispatcher


def get(data):
    """Visa Merchant Offers Resource Center Offers Data API - Offers by Content Id.

        Retrieves current offers by Content Id.

        :param AllModel data: **Required**. 
            Instance of :func:`pyvdp.vmorc.offers.AllModel`. 
        :return: response from VDP.

        **Usage:**

        ..  code:: python

            from pyvdp.vmorc.offers import AllModel, all

            data_kwargs = {}

            data = AllModel(**data_kwargs)

            result = all.get(data)
            print(result)
        """
    c = VisaMerchantOffersResourceCenterDispatcher(resource='vmorc',
                                                   api='offers',
                                                   version='v1',
                                                   method='all',
                                                   http_verb='GET',
                                                   auth_method='ssl',
                                                   data=data)

    return c.send()
