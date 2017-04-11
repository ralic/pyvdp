from pyvdp.visadirect import VisaDirectDispatcher


API = 'mvisa'
METHOD = 'cashinpushpayments'


def send(data):
    """Submits VisaDirect mVISA CashinPushPayments request.

    :param CashinPushPaymentsModel data: **Required**. 
        Instance of :func:`~pyvdp.visadirect.mvisa.CashinPushPaymentsModel`.
    :return: Dictionary with VDP API response.
    
    **Usage:**
    
    ..  code-block:: python
    
        from pyvdp.visadirect import CardAcceptorModel
        from pyvdp.visadirect.mvisa import cashinpushpayments, CashinPushPaymentsModel
        
        ca_address_kwargs = {
            "city": "KOLKATA",
            "country": "IND"
        }
        
        ca_kwargs = {
            "address": CardAcceptorModel.CardAcceptorAddress(**ca_address_kwargs),
            "idCode": "CA-IDCode-77765",
            "name": "Visa Inc. USA-Foster City"            
        }
        
        cipp_kwargs = {
            "acquirerCountryCode": "643",
            "acquiringBin": "400171",
            "amount": "124.05",
            "businessApplicationId": "CI",            
            "cardAcceptor": CardAcceptorModel(**ca_kwargs),
            "merchantCategoryCode": "4829",
            "recipientPrimaryAccountNumber": "4123640062698797",
            "senderAccountNumber": "4541237895236",
            "senderName": "Mohammed Qasim",
            "senderReference": "1234",
            "transactionCurrencyCode": "USD",
            "transactionIdentifier": "381228649430015"                                        
        }
        
        data = CashinPushPaymentsModel(**cipp_kwargs)
        
        result = cashinpushpayments.send(data=data)
        print(result)
    """
    c = VisaDirectDispatcher(api=API, method=METHOD, http_verb='POST', data=data)
    return c.send()


def get(query):
    """Sends VisaDirect mVISA CashinPushPayments request.

    :param str query: **Required**. Transaction status identifier.
    :return: Dictionary with VDP API response.
    
    ..  code-block:: python
    
        from pyvdp.visadirect.mvisa import cashinpushpayments
        
        status_id = '1491819372_186_81_l73c003_VDP_ARM'
        result = cashinpushpayments.get(status_id)
        print(result)
    """
    query_string = '/' + query

    c = VisaDirectDispatcher(api=API, method=METHOD, http_verb='GET', query_string=query_string)
    return c.send()
