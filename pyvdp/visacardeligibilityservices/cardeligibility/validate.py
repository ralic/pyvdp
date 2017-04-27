from pyvdp.visacardeligibilityservices.dispatcher import VisaCardEligibilityServicesDispatcher


def send(data):
    """Submits a VCES 'validate' request.

    :param ValidateModel data: **Required**. 
        Instance of :func:`~pyvdp.visacardeligibilityservices.eligibility.ValidateModel`.
    :return: A response from VDP.

    **Usage:**

    ..  code:: python
    
        from pyvdp.visacardeligibilityservices.cardeligibility import validate, ValidateModel
        
        request_kwargs = {
            "vendorUniqueId": "VAL_TENZ_GPID",
            "correlationId": "dfsdfasdsdf",
            "requestTimeStamp": "2/1/2017 11:05:20 AM",
            "permanentAccountNumber": "4111111111111111"        
        }
        
        data_kwargs = {
            "prepayRequest": ValidateModel.ValidateRequest(**request_kwargs)
        }
        
        data = ValidateModel(**data_kwargs)
        result = validate.send(data)
        print(result)
    """
    c = VisaCardEligibilityServicesDispatcher(resource='visacardeligibilityservices',
                                              api='',
                                              version='v1',
                                              method='cardeligibility/validate',
                                              http_verb='POST',
                                              auth_method='ssl',
                                              data=data)
    return c.send()
