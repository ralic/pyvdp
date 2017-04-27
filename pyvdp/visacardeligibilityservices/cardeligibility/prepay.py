from pyvdp.visacardeligibilityservices.dispatcher import VisaCardEligibilityServicesDispatcher


def send(data):
    """Submits a VCES 'prepay' request.

    :param PrepayModel data: **Required**. 
        Instance of :func:`~pyvdp.visacardeligibilityservices.eligibility.PrepayModel`.
    :return: A response from VDP.

    **Usage:**

    ..  code:: python

        from pyvdp.visacardeligibilityservices.cardeligibility import prepay, PrepayModel
        
        request_kwargs = {
            "vendoruniqueId": "VAL_TENZ_GPID",
            "correlationId": "dfsdfasdsdf",
            "requestTimeStamp": "27/4/2017 11:05:20 AM",
            "permanentAccountNumber": "4000000000000011"
        }
        
        data_kwargs = {
            "prepayRequest": PrepayModel.PrepayRequest(**request_kwargs)
        }
        
        data = PrepayModel(**data_kwargs)
        result = prepay.send(data)
        print(result)
    """
    c = VisaCardEligibilityServicesDispatcher(resource='visacardeligibilityservices',
                                              api='',
                                              version='v1',
                                              method='cardeligibility/prepay',
                                              http_verb='POST',
                                              auth_method='ssl',
                                              data=data)
    return c.send()
