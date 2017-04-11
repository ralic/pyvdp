from pyvdp.visadirect import VisaDirectDispatcher


API = 'fundstransfer'
METHOD = 'pushfundstransactions'


def send(data, multi=False):
    """Submits a PushFunds (OCT) request.

    :param data: **Required**. Instance of :func:`~pyvdp.visadirect.fundstransfer.PushFundsTransactionModel` or 
        :func:`~pyvdp.visadirect.fundstransfer.MultiPushFundsTransactionModel`.
    :param bool multi: **Conditional**. Indicates that transaction is a batch 
        (:func:`~pyvdp.visadirect.fundstransfer.MultiPushFundsTransactionModel`).
    :return: Dictionary with VDP API response.
    
    **Usage:**
    
    ..  code-block:: python
    
        from pyvdp.visadirect import CardAcceptorModel, PointOfServiceDataModel
        from pyvdp.visadirect.fundstransfer import pushfunds, PushFundsTransactionModel
        
        posd_kwargs = {
            "motoECIIndicator": "0",
            "panEntryMode": "90",
            "posConditionCode": "00"            
        }
             
        ca_address_kwargs = {
            "country": "USA",
            "county": "San Mateo",
            "state": "CA",
            "zipCode": "94404"        
        }
        
        ca_kwargs = {
            "address": CardAcceptorModel.CardAcceptorAddress(**ca_address_kwargs),
            "idCode": "CA-IDCode-77765",
            "name": "Visa Inc. USA-Foster City",
            "terminalId": "TID-9999"        
        }
        
        pftm_kwargs = {
            "cardAcceptor": CardAcceptorModel(**ca_kwargs),
            "pointOfServiceData": PointOfServiceDataModel(**posd_kwargs),
            "acquirerCountryCode": "840",
            "acquiringBin": "408999",
            "amount": "124.05",
            "businessApplicationId": "AA",
            "recipientName": "rohan",
            "recipientPrimaryAccountNumber": "4957030420210462",
            "senderAccountNumber": "4957030420210454",
            "senderAddress": "901 Metro Center Blvd",
            "senderCity": "Foster City",
            "senderCountryCode": "124",
            "senderName": "Mohammed Qasim",
            "senderReference": "",
            "senderStateCode": "CA",
            "sourceOfFundsCode": "05",
            "transactionCurrencyCode": "USD",
            "transactionIdentifier": "381228649430015"                        
        }
        
        data = PushFundsTransactionModel(**pftm_kwargs)
        
        result = pushfunds.send(data=data)
        print(result)
    """
    method = METHOD

    if multi:
        method = 'multipushfundstransactions'

    c = VisaDirectDispatcher(api=API, method=method, http_verb='POST', data=data)
    return c.send()


def get(query, multi=False):
    """Fetches a status of previously submitted PushFunds request.

    Returns a status of :func:`~pyvdp.visadirect.fundstransfer.PushFundsTransactionModel` or  
    :func:`~pyvdp.visadirect.fundstransfer.MultiPushFundsTransactionModel` request by transaction identifier, returned 
    with  202 response.

    :param str query: **Required**. Transaction status identifier.
    :param bool multi: **Conditional**. Indicates that transaction is a batch 
        (:func:`~pyvdp.visadirect.fundstransfer.MultiPushFundsTransactionModel`)
    :return: Dictionary with VDP API response.
    
    **Usage:**
    
    ..  code-block:: python
    
        from pyvdp.visadirect.fundstransfer import pushfunds
        
        status_id = "1491819372_186_81_l73c003_VDP_ARM"
        result = pushfunds.send(status_id)
        print(result)
    """
    method = METHOD

    if multi:
        method = 'multipushfundstransactions'

    query_string = '/' + query

    c = VisaDirectDispatcher(api=API, method=method, http_verb='GET', query_string=query_string)
    return c.send()
