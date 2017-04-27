class RedeemModel(object):
    """Visa Card Eligility Services redeem request data object model.

    https://developer.visa.com/products/vces/reference#vces__visa_card_eligibility_service__v1__redeem

    :param RedeemRequest redeemRequest: **Required**. 
        Instance of :func:`~pyvdp.visacardeligibilityservices.RedeemModel.RedeemRequest`.

    **Request:**

    ..  code:: json

        {
            "redeemRequest": {
                "vendoruniqueId": "VAL_TENZ_GPID",
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
        'redeemRequest'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)

    class RedeemRequest(object):
        """Payload for VCES redeem request.

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
