from pyvdp.vmorc.dispatcher import VisaMerchantOffersResourceCenterDispatcher


def get(data):
    """Visa Merchant Offers Resource Center Reference Data API - Data By Reference.

    Retrieves data by Reference.

    :param RefModel data: **Required**. 
        Instance of :func:`pyvdp.vmorc.data.RefModel`. 
    :return: response from VDP.

    **Usage:**

    ..  code:: python

        from pyvdp.vmorc.data import RefModel, ref

        data_kwargs = {
            "resources": "business_segment,category",
            "languages": "1,8",
            "programIds": "100740"
        }

        data = RefModel(**data_kwargs)

        result = ref.get(data)
        print(result)
    """
    c = VisaMerchantOffersResourceCenterDispatcher(resource='vmorc',
                                                   api='data',
                                                   version='v1',
                                                   method='ref',
                                                   http_verb='GET',
                                                   auth_method='ssl',
                                                   data=data)

    return c.send()
