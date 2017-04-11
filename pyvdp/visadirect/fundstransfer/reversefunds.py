from pyvdp.visadirect import VisaDirectDispatcher


API = 'fundstransfer'
METHOD = 'reversefundstransactions'


def send(data, multi=False):
    """Submits a ReverseFunds request.

    :param data: **Required**. Instance of :func:`~pyvdp.visadirect.fundstransfer.ReverseFundsTransactionModel` or 
        :func:`~pyvdp.visadirect.fundstransfer.MultiReverseFundsTransactionModel`.
    :param bool multi: **Conditional**. Indicates that transaction is a batch 
        (:func:`~pyvdp.visadirect.fundstransfer.MultiReverseFundsTransactionModel`).
    :return: Dictionary with VDP API response.
    
    **Usage:**
    
    ..  code-block:: python
    
        from pyvdp.visadirect import (CardAcceptorModel, 
                                      OriginalDataElementsModel, 
                                      PointOfServiceCapabilityModel, 
                                      PointOfServiceDataModel)
        from pyvdp.visadirect.fundstransfer import reversefunds, ReverseFundsTransactionModel
        
        ode_kwargs = {
            "acquiringBin": "408999",
            "approvalCode": "20304B",
            "systemsTraceAuditNumber": "897825",
            "transmissionDateTime": "2017-03-17T09:02:32"        
        }
        
        posc_kwargs = {
            "posTerminalEntryCapability": "2",
            "posTerminalType": "4"        
        }
        
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
            "idCode": "VMT200911026070",
            "name": "Visa Inc. USA-Foster City",
            "terminalId": "365539"                    
        }
        
        rftm_kwargs = {
            "cardAcceptor": CardAcceptorModel(**ca_kwargs),
            "originalDataElements": OriginalDataElementsModel(**ode_kwargs),
            "pointOfServiceCapability": PointOfServiceCapabilityModel(**posc_kwargs),
            "pointOfServiceData": PointOfServiceDataModel(**posd_kwargs),
            "senderCardExpiryDate": "2015-10",
            "senderCurrencyCode": "USD",
            "senderPrimaryAccountNumber": "4895100000055127",
            "transactionIdentifier": "381228649430011",
            "acquirerCountryCode": "608",
            "acquiringBin": "408999",
            "amount": "24.01",                        
        }
        
        data = ReverseFundsTransactionModel(**rftm_kwargs)
        result = reversefunds.send(data=data)
        print(result)
    """
    method = METHOD

    if multi:
        method = 'multireversefundstransactions'

    c = VisaDirectDispatcher(api=API, method=method, http_verb='POST', data=data)
    return c.send()


def get(query, multi=False):
    """Fetches a status of previously submitted ReverseFunds request.

    Returns a status of :func:`~pyvdp.visadirect.fundstransfer.ReverseFundsTransactionModel` or  
    :func:`~pyvdp.visadirect.fundstransfer.MultiReverseFundsTransactionModel` request by transaction identifier, returned 
    with 202 response.

    :param str query: **Required**. Transaction status identifier.
    :param bool multi: **Conditional**. Indicates that transaction is a batch 
        (:func:`~pyvdp.visadirect.fundstransfer.MultiReverseFundsTransactionModel`)
    :return: Dictionary with VDP API response
    
    **Usage:**
    
    ..  code-block:: python
    
        from pyvdp.visadirect.fundstransfer import reversefunds
        
        status_id = '1491819372_186_81_l73c003_VDP_ARM'
        
        result = reversefunds.get(status_id)
        print(result)
    """
    method = METHOD

    if multi:
        method = 'multireversefundstransactions'

    query_string = '/' + query

    c = VisaDirectDispatcher(api=API, method=method, http_verb='GET', query_string=query_string)
    return c.send()
