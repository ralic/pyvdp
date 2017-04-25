from pyvdp.paai.dispatcher import VisaPaaiDispatcher


def send(data):
    """Submits General Card Attributes Inquiry request.

    :param GeneralInquiryModel data: **Required**. 
        Instance of :func:`~pyvdp.paai.generalattinq.cardattributes.GeneralInquiryModel`
    :return: Dictionary with VDP response.
    
    **Usage:**
    
    ..  code:: python
    
        from pyvdp.paai.generalattinq.cardattributes import generalinquiry, GeneralInquiryModel
        
        data_kwargs = {
            "systemsTraceAuditNumber": 123456,
            "primaryAccountNumber": "4957030420210512",
        }
        
        data = GeneralInquiryModel(**data_kwargs)
        result = generalinquiry.send(data)
        print(result)    
    """
    c = VisaPaaiDispatcher(resource='paai',
                           api='generalattinq',
                           method='cardattributes/generalinquiry',
                           http_verb='POST',
                           auth_method='ssl',
                           data=data)
    return c.send()
