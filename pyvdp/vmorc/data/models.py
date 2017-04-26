class MerchantAddressModel(object):
    """Visa MORC Reference Data API - Merchant Address data model.
    
    https://developer.visa.com/products/vmorc/reference#vmorc__reference_data_api__v1__retrieve_data_by_merchant_address
    
    :param str merchantIds: **Required**. Comma-separated list of merchant identifiers.
    :param int start_index: **Optional**. Index of starting element in resulting collection. Default is 1.
    
    **Request:**
    
    ..  code:: http
    
        GET vmorc/data/v1/merchantAddress?merchantIds=101456,101457&start_index=2
    
    **Response:**
    
    ..  code:: json
 
        {
            "ReturnedResults": 1,
            "StartIndex": 1,
            "MerchantsAddresses": [
                [
                    {
                        "key": 104366,
                        "address1": "12345 Address Drive",
                        "address2": "",
                        "city": "Lima ",
                        "state": "Chorrillos",
                        "postalCode": "656565a",
                        "countryName": "Peru",
                        "languageName": "Portuguese (Brazillian)",
                        "latitude": "",
                        "longitude": "",
                        "languageIds": [
                            22
                        ],
                        "languages": [
                            "Portuguese (Brazillian)"
                        ],
                        "merchantKey": 100057,
                        "merchantValue": "Merchant One",
                        "indexNumber": 1
                    }
                ]
            ],
            "TotalFoundResults": 1
        } 
 
    """
    ATTRS = [
        'merchantIds',
        'start_index',
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)


class MerchantModel(object):
    """Visa MORC Reference Data API - Merchant request data model.
    
    https://developer.visa.com/products/vmorc/reference#vmorc__reference_data_api__v1__retrieve_data_by_merchant

    :param str program: **Optional**. Program identifier.
    :param int start_index: **Optional**. Index of starting element in resulting collection. Default is 1.
    
    **Request:**
    
    ..  code:: http
    
        GET vmorc/data/v1/merchant?program=100760
        
    **Response:**
    
    ..  code:: json
    
        {
            "ReturnedResults": 1,
            "Merchants": [
                {
                    "key": 100057,
                    "value": "Merchant One",
                    "languageId": 1,
                    "translations": [
                        {
                            "value": "Merchant One",
                            "languageId": 1
                        }
                    ],
                    "alternativeNames": [ ],
                    "images": [
                        {
                            "key": 103988,
                            "fileName": "merchantLogo_100057_320x120.png",
                            "imageResolution": "High",
                            "description": "",
                            "promotionId": 3,
                            "promotionChannel": "Online",
                            "promotionIds": [
                                3,
                                83
                            ],
                            "promotionChannels": [
                                "Online",
                                "Mobile"
                            ],
                            "fileLocation": "http://visateam.visa.stage.qts.visa.com/images/merchantoffers/2015-03/1426103572663.merchantLogo_100057_320x120.png",
                            "imageFileSize": "20.0 KB",
                            "imageFileHeight": "120 px",
                            "imageFileWidth": "320 px",
                            "languageIds": [
                                1,
                                22
                            ],
                            "languages": [
                                "English",
                                "Portuguese (Brazillian)"
                            ],
                            "logoAltTag": ""
                        },
                        {
                            "key": 103987,
                            "fileName": "merchantLogo_100057_160x60.png",
                            "imageResolution": "High",
                            "description": "",
                            "promotionId": 3,
                            "promotionChannel": "Online",
                            "promotionIds": [
                                3,
                                83
                            ],
                            "promotionChannels": [
                                "Online",
                                "Mobile"
                            ],
                            "fileLocation": "http://visateam.visa.stage.qts.visa.com/images/merchantoffers/2015-03/1426103556313.merchantLogo_100057_160x60.png",
                            "imageFileSize": "6.0 KB",
                            "imageFileHeight": "60 px",
                            "imageFileWidth": "160 px",
                            "languageIds": [
                                1,
                                22
                            ],
                            "languages": [
                                "English",
                                "Portuguese (Brazillian)"
                            ],
                            "logoAltTag": ""
                        }
                    ],
                    "indexNumber": 1
                }
            ],
            "StartIndex": 1,
            "language": [
                {
                    "key": 7,
                    "value": "Arabic"
                },
                {
                    "key": 14,
                    "value": "Azeri"
                },
                { ... },
                { ... },
                { ... }
            ],
            "TotalFoundResults": 1
        }        
    """
    ATTRS = [
        'start_index',
        'program'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)


class RefModel(object):
    """Visa MORC Reference Data API - request by reference data model.
    
    https://developer.visa.com/products/vmorc/reference#vmorc__offers_data_api__v1__retrieve_offers_by_filter
    
    See `Request and Response codes <https://developer.visa.com/products/vmorc/reference#vmorc__offers_data_api__v1__retrieve_offers_by_filter>`_
    for details regarding attributes.

    :param str resources: **Optional**. Comma-separated list of resources. 
        See `resources <https://developer.visa.com/guides/request_response_codes#resources>`_
    :param str languages: **Optional**. Comma-separated list of language identifiers. Default returns all languages.
    :param str programIds: **Optional**. TODO: Undocumented.
    
    **Request:**
    
    ..  code:: http
    
        GET vmorc/data/v1/ref?resources=business_segment,category&languages=1,8&programIds=100740
    
    **Response:**
    
    ..  code:: json
    
        {
            "business_segment": [
                {
                    "key": 7,
                    "value": "Commercial",
                    "languageId": 1,
                    "translations": [
                        {
                            "value": "Comercial",
                            "languageId": 22
                        },
                        {
                            "value": "Commercial",
                            "languageId": 1
                        },
                        { ... },
                        { ... },
                        { ... }
                    ]
                },
                {
                    "key": 8,
                    "value": "Consumer",
                    "languageId": 1,
                    "translations": [
                        {
                            "value": "Consumidor",
                            "languageId": 22
                        },
                        {
                            "value": "Consumidor",
                            "languageId": 3
                        },
                        { ... },
                        { ... },
                        { ... }
                    ]
                },
                {
                    "key": 39,
                    "value": "Small Business",
                    "languageId": 1,
                    "translations": [
                        {
                            "value": "Empresarial",
                            "languageId": 4
                        },
                        {
                            "value": "Small Business",
                            "languageId": 1
                        },
                        { ... },
                        { ... },
                        { ... }
                    ]
                }
            ],
            "language": [
                {
                    "key": 7,
                    "value": "Arabic"
                },
                {
                    "key": 14,
                    "value": "Azeri"
                },
                { ... },
                { ... },
                { ... }
            ]
        }    
       
    """
    ATTRS = [
        'resources',
        'languages',
        'programIds'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)
