from pyvdp.visacardeligibilityservices.dispatcher import VisaCardEligibilityServicesDispatcher


def send(data):
    """Submits a VCES promo 'redeem' request.

    :param RedeemModel data: **Required**. 
        Instance of :func:`~pyvdp.visacardeligibilityservices.promo.RedeemModel`.
    :return: A response from VDP.

    **Usage:**

    ..  code:: python

        from pyvdp.visacardeligibilityservices.promo import redeem, RedeemModel
        
        request_kwargs = {
            "vendorUniqueId": "VAL_TENZ_GPID",
            "correlationId": "dfsdfasdsdf",
            "requestTimeStamp": "2/1/2017 11:05:20 AM",
            "permanentAccountNumber": "4111111111111111"        
        }
        
        data_kwargs = {
            "redeemRequest": RedeemModel.RedeemRequest(**request_kwargs)
        }
        
        data = RedeemModel(**data_kwargs)
        result = redeem.send(data)
        print(result)        
    """
    c = VisaCardEligibilityServicesDispatcher(resource='visacardeligibilityservices',
                                              api='',
                                              version='v1',
                                              method='promo/redeem',
                                              http_verb='POST',
                                              auth_method='ssl',
                                              data=data)
    return c.send()
