from pyvdp.visadirect import VisaDirectDispatcher


API = 'mvisa'
METHOD = 'merchantpushpayments'


def send(data):
    """Submits VisaDirect mVISA MerchantPushPayments request.

    :param MerchantPushPaymentsModel data: **Required**. 
        Instance of :func:`~pyvdp.visadirect.mvisa.MerchantPushPaymentsModel`.
    :return: Dictionary with VDP API response.
    
    ..  code-block:: python
    
        from pyvdp.visadirect import CardAcceptorModel
        from pyvdp.visadirect.mvisa import merchantpushpayments, MerchantPushPaymentsModel, PurchaseIdentifierModel
        
        ca_address_kwargs = {
            "city": "KOLKATA",
            "country": "IND"        
        }
        
        ca_kwargs = {
            "address": CardAcceptorModel.CardAcceptorAddress(**ca_address_kwargs),
            "idCode": "CA-IDCode-77765",
            "name": "Visa Inc. USA-Foster City"                    
        }
        
        pi_kwargs = {
            "referenceNumber": "REF_123456789123456789123",
            "type": "1"        
        }
        
        mpp_kwargs = {
            "acquirerCountryCode": "356",
            "acquiringBin": "408972",
            "amount": "124.05",
            "businessApplicationId": "MP",
            "cardAcceptor": CardAcceptorModel(**ca_kwargs),
            "feeProgramIndicator": "123",
            "purchaseIdentifier": PurchaseIdentifierModel(**pi_kwargs),            
            "recipientName": "Jasper",
            "recipientPrimaryAccountNumber": "4123640062698797",
            "secondaryId": "123TEST",
            "senderAccountNumber": "4027290077881587",
            "senderName": "Jasper",
            "senderReference": "",
            "transactionCurrencyCode": "INR",
            "transactionIdentifier": "381228649430015"            
        }
        
        data = MerchantPushPaymentsModel(**mpp_kwargs)
        
        result = merchantpushpayments.send(data=data)
        print(result)
    """
    c = VisaDirectDispatcher(api=API, method=METHOD, http_verb='POST', data=data)
    return c.send()


def get(query):
    """Sends VisaDirect mVISA MerchantPushPayments request.

    :param str query: **Required**. Transaction status identifier.
    :return: Dictionary with VDP API response.
    
    ..  code-block:: python
    
        from pyvdp.visadirect.mvisa import merchantpushpayments
        
        status_id = '1491819372_186_81_l73c003_VDP_ARM'
        result = merchantpushpayments.get(status_id)
        print(result)    
    """
    query_string = '/' + query

    c = VisaDirectDispatcher(api=API, method=METHOD, http_verb='GET', query_string=query_string)
    return c.send()
