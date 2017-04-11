from pyvdp.dcas.dispatcher import VisaDcasDispatcher

API = 'cardinquiry'
METHOD = 'accounts/debitcardinquiry'


def send(data):
    """Submits a Digital Card and Accounts request.
    
    :param CardInquiryModel data: **Required**.
        Instance of :func:`~pyvdp.dcas.cardinquiry.accounts.CardInquiryModel`. 
    :return: Response from VDP
     
    **Usage**: 
    
    ..  code-block:: python
    
            from pyvdp.dcas.cardinquiry.accounts import debitcardinquiry, CardInquiryModel
    
            cn_kwargs = {
                'first_name': 'John',
                'last_name': 'Doe'
            }
    
            cim_kwargs = {
                'direct_dan': '0987654321',
                'routing_number': '1234567890',
                'cardholder_name': CardInquiryModel.CardholderName(**cn_kwargs)
            }
    
            cim = CardInquiryModel(**cim_kwargs)
            result = debitcardinquiry.send(data=cim)
            print(result)     
    """
    c = VisaDcasDispatcher(api=API, method=METHOD, http_verb='POST', data=data)
    return c.send()
