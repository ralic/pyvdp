from pyvdp.paai.dispatcher import VisaPaaiDispatcher


API = 'generalattinq'
METHOD = 'cardattributes/generalinquiry'


def send(data):
    """Submits General Card Attributes Inquiry request.

    :param GeneralInquiryModel data: **Required**. 
        Instance of :func:`~pyvdp.paai.generalattinq.cardattributes.GeneralInquiryModel`
    :return: Dictionary with VDP response.
    
    **Usage:**
    
    ..  code-block:: python
    
        from pyvdp.paai.geeneralattinq.cardattributes import generalinquiry, GeneralInquiryModel
        
        gim_kwargs = {
            "primaryAccountNumber": "4957030420210512",
        }
        
        data = GeneralInquiryModel(**gim_kwargs)
        
        result = generalinquiry.send(data=data)
        print(result)    
    """
    c = VisaPaaiDispatcher(api=API, method=METHOD, http_verb='POST', data=data)
    return c.send()
