from pyvdp.pav.dispatcher import VisaPavDispatcher


def send(data):
    """Submits a payment account validation request.

    :param PavTransaction data: **Required**. Instance of :func:`~pyvdp.pav.CardValidationModel`.
    :return: A response from VDP.
    
    **Usage:**
    
    ..  code-block:: python
    
        from pyvdp.visadirect import CardAcceptorModel
        from pyvdp.pav import cardvalidation, CardValidationModel
        
        ca_address_kwargs = {
            "city": "fostr city",
            "country": "PAKISTAN",
            "county": "CA",
            "state": "CA",
            "zipCode": "94404"
        }
        
        ca_kwargs = {
            "address": CardAcceptorModel.CardAcceptorAddress(**ca_address_kwargs),
            "idCode": "111111",
            "name": "rohan",
            "terminalId": "123"            
        }
        
        avr_kwargs = {
            "postalCode": "T4B 3G5",
            "street": "2881 Main Street Sw"        
        }
        
        pav_kwargs = {
            "addressVerificationResults": CardValidationModel.AddressVerificationResults(**avr_kwargs),
            "cardAcceptor": CardAcceptorModel(**ca_kwargs),
            "cardCvv2Value": "672",
            "cardExpiryDate": "2018-06",
            "primaryAccountNumber": "4957030000313108",
            "retrievalReferenceNumber": "015221743720",
            "systemsTraceAuditNumber": "743720"            
        }
        
        data = CardValidationModel(**pav_kwargs)        
        result = cardvalidation.send(data=data)        
        print(result)
    """
    c = VisaPavDispatcher(method='cardvalidation', http_verb='post', data=data)
    return c.send()
