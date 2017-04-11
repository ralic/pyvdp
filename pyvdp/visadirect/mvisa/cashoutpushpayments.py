from pyvdp.visadirect import VisaDirectDispatcher


API = 'mvisa'
METHOD = 'cashoutpushpayments'


def send(data):
    """Submits VisaDirect mVISA CashoutPushPayments request.

    :param CashoutPushPaymentsModel data: **Required**. 
        Instance of :func:`~pyvdp.visadirect.mvisa.CashoutPushPaymentsModel`.
    :return: Dictionary with VDP API response.
    
    **Usage:**
    
    ..  code-block:: python
    
        from pyvdp.visadirect import CardAcceptorModel
        from pyvdp.visadirect.mvisa import cashoutpushpayments, CashoutPushPaymentsModel
        
        ca_address_kwargs = {
            "city": "mVisa cashout",
            "country": "IND"            
        }
        
        ca_kwargs = {
            "address": CardAcceptorModel.CardAcceptorAddress(**ca_address_kwargs),
            "idCode": "CA-IDCode-77765",
            "name": "mVisa cashout"        
        }
        
        copp_kwargs = {
            "acquirerCountryCode": "643",
            "acquiringBin": "400171",
            "amount": "124.05",
            "businessApplicationId": "CO",
            "address": CardAcceptorModel(**ca_kwargs),
            "merchantCategoryCode": "6012",
            "recipientPrimaryAccountNumber": "4123640062698797",
            "senderAccountNumber": "456789123456",
            "senderName": "Mohammed Qasim",
            "senderReference": "REFNUM123",
            "transactionCurrencyCode": "USD",
            "transactionIdentifier": "381228649430015"            
        }
        
        data = CashoutPushPaymentsModel(**copp_kwargs)
        result = cashoutpushpayments.send(data=data)
        print(result)
        
    """
    c = VisaDirectDispatcher(api=API, method=METHOD, http_verb='POST', data=data)
    return c.send()


def get(query):
    """Sends VisaDirect mVISA CashoutPushPayments request.

    :param str query: **Required**. Transaction status identifier.
    :return: Dictionary with VDP API response.
    
    ..  code-block:: python
    
        from pyvdp.visadirect.mvisa import cashoutpushpayments
        
        status_id = '1491819372_186_81_l73c003_VDP_ARM'
        result = cashoutpushpayments.get(status_id)
        print(result)
    """
    query_string = '/' + query

    c = VisaDirectDispatcher(api=API, method=METHOD, http_verb='GET', query_string=query_string)
    return c.send()
