from pyvdp.visadirect import VisaDirectDispatcher

API = 'fundstransfer'
METHOD = 'pullfundstransactions'


def send(data, multi=False):
    """Submits a PullFunds (AFT) request.

    :param data: **Required**. Instance of :func:`~pyvdp.visadirect.fundstransfer.PullFundsTransactionModel` or 
        :func:`~pyvdp.visadirect.fundstransfer.MultiPullFundsTransactionModel`.
    :param bool multi: **Conditional**. Indicates that transaction is a batch 
        (:func:`~pyvdp.visadirect.fundstransfer.MultiPullFundsTransactionModel`)
    :return: Dictionary with VDP API response.
    
    **Usage:**
    
    ..  code-block:: python
    
        from pyvdp.visadirect import CardAcceptorModel
        from pyvdp.visadirect.fundstransfer import pullfunds, PullFundsTransactionModel
        
        ca_address_kwargs = {
            "country": "USA",
            "county": "San Mateo",
            "state": "CA",
            "zipCode": "94404"            
        }
        
        ca_kwargs = {
            "address": CardAcceptorModel.CardAcceptorAddress(**ca_address_kwargs),
            "idCode": "ABCD1234ABCD123",
            "name": "Visa Inc. USA-Foster City",
            "terminalId": "ABCD1234"            
        }
        
        pftm_kwargs = {
            "cardAcceptor": CardAcceptorModel(**ca_kwargs),
            "acquirerCountryCode": 840,
            "acquiringBin": 408999,
            "amount": 124.02,
            "businessApplicationId": "AA",
            "cavv": "0700100038238906000013405823891061668252",
            "foreignExchangeFeeTransaction": "11.99",
            "localTransactionDateTime": "2017-03-17T08:20:42",
            "senderCardExpiryDate": "2015-10",
            "senderCurrencyCode": "USD",
            "senderPrimaryAccountNumber": "4895142232120006",
            "surcharge": "11.99",                            
        }
        
        data = PullFundsTransactionModel(**pftm_kwargs)
        result = pullfunds.send(data=data)
        print(result)
    """
    method = METHOD

    if multi:
        method = 'multipullfundstransactions'

    c = VisaDirectDispatcher(api=API, method=method, http_verb='POST', data=data)
    response = c.send()

    return response


def get(query, multi=False):
    """Fetches a status of previously submitted PullFunds request.
    
    Returns a status of :func:`~pyvdp.visadirect.fundstransfer.PullFundsTransactionModel` or  
    :func:`~pyvdp.visadirect.fundstransfer.MultiPullFundsTransactionModel` request by transaction identifier, 
    returned with  202 response.

    :param str query: **Required**. Transaction status identifier.
    :param bool multi: **Conditional**. Indicates that transaction is a batch 
        (:func:`~pyvdp.visadirect.fundstransfer.MultiPullFundsTransactionModel`)
    :return: Dictionary with VDP API response.
    
    **Usage:**
    
    ..  code-block:: python
        
        from pyvdp.visadirect.fundstransfer import pullfunds
        
        status_id = '1491819372_186_81_l73c003_VDP_ARM'

        result = pullfunds.get(status_id)
        print(result)
    """

    method = METHOD

    if multi:
        method = 'multipullfundstransactions'

    query_string = '/' + query

    c = VisaDirectDispatcher(api=API, method=method, http_verb='GET', query_string=query_string)
    return c.send()
