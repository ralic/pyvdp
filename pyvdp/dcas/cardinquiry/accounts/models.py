class CardInquiryModel(object):
    """Card Inquiry data model.
    
    :param str directDebitAccountNumber: **Required**. Direct debit account number. 6-22 characters string.
    :param str routingNumber: **Required**. Routing number. 6-12 characters string.
    :param CardholderName cardholderName: **Optional**. 
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
    ATTRS = [
        'directDebitAccountNumber',
        'routingNumber',
        'cardholderName'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)

    class CardholderName(object):
        """Cardholder name data model.
        
        Part of Card Inquiry data model.
        
        :param str firstName: **Optional**. Cardholder first name.
        :param str lastName: **Optional**. Cardholder last name.
        """
        ATTRS = [
            'firstName',
            'lastName'
        ]

        def __init__(self, **kwargs):
            for attr, value in kwargs.items():
                if attr in self.ATTRS and value:
                    self.__setattr__(attr, value)
