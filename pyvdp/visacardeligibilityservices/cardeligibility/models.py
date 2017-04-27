class ValidateModel(object):
    """Visa Card Eligility Services validate request data object model.
    
    https://developer.visa.com/products/vces/reference#vces__visa_card_eligibility_service__v1__validate
    
    :param ValidateRequest validateRequest: **Required**. 
        Instance of :func:`~pyvdp.visacardeligibilityservices.cardeligibility.ValidateModel.ValidateRequest`.
        
    **Request:**
    
    ..  code:: json
    
        {
            "validateRequest": {
                "vendorUniqueId": "VAL_TENZ_GPID",
                "correlationId": "dfsdfasdsdf",
                "requestTimeStamp": "2/1/2017 11:05:20 AM",
                "permanentAccountNumber": "4111111111111111",
                "extendedData": "asddd"
            }
        }
            
    **Response:**
    
    ..  code:: json
    
        {
            "validateResponse": {
                "statuscode": "300",
                "statusDescription": "Card Ineligible",
                "correlationId": "dfsdfasdsdf",
                "responseTimeStamp": "",
                "issuerBid": "123",
                "productType": "xxxx",
                "productSubType": "xxxx",
                "countryCode": "xxx",
                "binIndicator": "xxx",
                "cardBenefits": [
                    {
                        "cardBenefit": [
                            {
                                "benefitName": "XXXXXXXXXXXX1235   ",
                                "benefitDesc": "Visa Signature",
                                "phoneNumberDetails": "xx",
                                "cardEnhanceTypeCode": "xx"
                            },
                            {
                                "benefitName": "XXXXXXXXXXXX1234   ",
                                "benefitDesc": "Visa Infinite",
                                "phoneNumberDetails": "xx",
                                "cardEnhanceTypeCode": "xx"
                            }
                        ]
                    }
                ],
                "eligibilityLevel": "xxxx",
                "acctFundSrce": "xxxx",
                "acctFundSrceSubTyp": "xxxxx",
                "iseligible": "True",
                "cardID": "12456",
                "cardHolderId": "4567"
            }
        }    
    """
    ATTRS = [
        'validateRequest'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)

    class ValidateRequest(object):
        """Payload for VCES validate request.
        
        :param str vendorUniqueId: **Required**. TODO: Undocumented. Vendor Unique ID.
        :param str extendedData: **Optional**. TODO: Undocumented. 
        :param str permanentAccountNumber: **Optional**. TODO: Undocumented.
        :param str requestTimeStamp: **Required**. TODO: Undocumented. Request timestamp.
        :param str correlationId: **Required**. TODO: Undocumented. 
        """
        ATTRS = [
            'vendorUniqueId',
            'extendedData',
            'permanentAccountNumber',
            'requestTimeStamp',
            'correlationId'
        ]

        def __init__(self, **kwargs):
            for attr, value in kwargs.items():
                if attr in self.ATTRS and value:
                    self.__setattr__(attr, value)


class PrepayModel(object):
    """Visa Card Eligility Services prepay request data object model.

    https://developer.visa.com/products/vces/reference#vces__visa_card_eligibility_service__v1__prepay

    :param PrepayRequest prepayRequest: **Required**. 
        Instance of :func:`~pyvdp.visacardeligibilityservices.cardelibility.PrepayModel.PrepayRequest`.

    **Request:**

    ..  code:: json

        {
            "redeemRequest": {
                "vendorUniqueId": "VAL_TENZ_GPID",
                "correlationId": "dfsdfasdsdf",
                "requestTimeStamp": "2/1/2017 11:05:20 AM",
                "permanentAccountNumber": "4111111111111111"
            }
        }

    **Response:**

    ..  code:: json

        {
            "redeemResponse": {
                "correlationId": "dfsdfasdsdf",
                "responsetimestamp": "",
                "statuscode": "300",
                "statusdescription": "Card InElgiibile"
            }
        }
    """
    ATTRS = [
        'prepayRequest'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)

    class PrepayRequest(object):
        """Payload for VCES prepay request.

        :param str vendorUniqueId: **Required**. TODO: Undocumented. Vendor Unique ID.
        :param str permanentAccountNumber: **Optional**. TODO: Undocumented.
        :param str requestTimeStamp: **Required**. TODO: Undocumented. Request timestamp.
        :param str correlationId: **Required**. TODO: Undocumented. 
        """
        ATTRS = [
            'vendorUniqueId',
            'permanentAccountNumber',
            'requestTimeStamp',
            'correlationId'
        ]

        def __init__(self, **kwargs):
            for attr, value in kwargs.items():
                if attr in self.ATTRS and value:
                    self.__setattr__(attr, value)
