from pyvdp.dcas.dispatcher import VisaDcasDispatcher


def send(data):
    """Submits DCAS Debit Card Inquiry request.
    
    :param DebitCardInquiryModel data: **Required**.
        Instance of :func:`~pyvdp.dcas.cardinquiry.accounts.DebitCardInquiryModel`. 
    :return: Response from VDP.
     
    **Usage**: 
    
    ..  code:: python
    
            from pyvdp.dcas.cardinquiry.accounts import debitcardinquiry, DebitCardInquiryModel
    
            cn_kwargs = {
                'firstName': 'John',
                'lastName': 'Doe'
            }
    
            data_kwargs = {
                'directDebitAccountNumber': '0987654321',
                'routingNumber': '1234567890',
                'cardholderName': DebitCardInquiryModel.CardholderName(**cn_kwargs)
            }
    
            data = DebitCardInquiryModel(**data_kwargs)
            result = debitcardinquiry.send(data)
            print(result)     
    """
    c = VisaDcasDispatcher(resource='dcas',
                           api='cardinquiry',
                           version='v1',
                           method='accounts/debitcardinquiry',
                           http_verb='POST',
                           auth_method='ssl',
                           data=data)
    return c.send()
