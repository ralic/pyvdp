class CardInquiryModel(object):
    """Card Inquiry data model.
    
    :param str direct_dan: **Required**. Direct debit account number. 6-22 characters string.
    :param str routing_number: **Required**. Routing number. 6-12 characters string.
    :param CardholderName cardholder_name: **Optional**. 
        Instance of :func:`~pyvdp.dcas.cardinquiry.accounts.CardInquiryModel.CardholderName`
    
    **Example:**
        ..  code-block:: json
        
            {
                "directDebitAccountNumber": "0987654321",
                "routingNumber": "1234567890",
                "cardholderName": {
                    "firstName": "JACK",
                    "lastName": "DADE"
                }
            }
    """
    ATTR_MAPPINGS = {
        'direct_dan': 'directDebitAccountNumber',
        'routing_number': 'routingNumber',
        'cardholder_name': 'cardholderName'
    }

    def __init__(self, **kwargs):
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)

    class CardholderName(object):
        """Cardholder name data model.
        
        Part of Card Inquiry data model.
        
        :param str first_name: **Optional**. Cardholder first name.
        :param str last_name: **Optional**. Cardholder last name.
        """
        ATTR_MAPPINGS = {
            'first_name': 'firstName',
            'last_name': 'lastName'
        }

        def __init__(self, **kwargs):
            self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)