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
                {
                    "key": 12,
                    "value": "Bahasa Indonesia"
                },
                {
                    "key": 20,
                    "value": "Canadian English"
                },
                {
                    "key": 21,
                    "value": "Canadian French"
                },
                {
                    "key": 28,
                    "value": "Croatian"
                },
                {
                    "key": 1,
                    "value": "English"
                },
                {
                    "key": 13,
                    "value": "French"
                },
                {
                    "key": 16,
                    "value": "Georgian"
                },
                {
                    "key": 25,
                    "value": "German"
                },
                {
                    "key": 27,
                    "value": "Hebrew"
                },
                {
                    "key": 26,
                    "value": "Italian"
                },
                {
                    "key": 2,
                    "value": "Japanese"
                },
                {
                    "key": 15,
                    "value": "Kazakh"
                },
                {
                    "key": 24,
                    "value": "Khmer"
                },
                {
                    "key": 19,
                    "value": "Kinyarwanda"
                },
                {
                    "key": 6,
                    "value": "Korean"
                },
                {
                    "key": 22,
                    "value": "Portuguese (Brazillian)"
                },
                {
                    "key": 3,
                    "value": "Portuguese (Regular)"
                },
                {
                    "key": 5,
                    "value": "Russian"
                },
                {
                    "key": 18,
                    "value": "Serbian"
                },
                {
                    "key": 8,
                    "value": "Simplified Chinese"
                },
                {
                    "key": 4,
                    "value": "Spanish"
                },
                {
                    "key": 11,
                    "value": "Thai"
                },
                {
                    "key": 23,
                    "value": "Traditional Chinese (HK)"
                },
                {
                    "key": 9,
                    "value": "Traditional Chinese (TW)"
                },
                {
                    "key": 17,
                    "value": "Ukrainian"
                },
                {
                    "key": 10,
                    "value": "Vietnamese"
                }
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
                            "value": "تجاري",
                            "languageId": 7
                        },
                        {
                            "value": "Коммерческий",
                            "languageId": 5
                        },
                        {
                            "value": "商務卡",
                            "languageId": 9
                        },
                        {
                            "value": "상용",
                            "languageId": 6
                        },
                        {
                            "value": "商務卡",
                            "languageId": 23
                        },
                        {
                            "value": "Comercial",
                            "languageId": 3
                        },
                        {
                            "value": "Commercial",
                            "languageId": 1
                        },
                        {
                            "value": "Affaires et Professionnels",
                            "languageId": 13
                        },
                        {
                            "value": "商务卡",
                            "languageId": 8
                        },
                        {
                            "value": "Comercial",
                            "languageId": 4
                        }
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
                        {
                            "value": "個人卡",
                            "languageId": 23
                        },
                        {
                            "value": "개인",
                            "languageId": 6
                        },
                        {
                            "value": "個人卡",
                            "languageId": 9
                        },
                        {
                            "value": "Потребитель",
                            "languageId": 5
                        },
                        {
                            "value": "مستهلك",
                            "languageId": 7
                        },
                        {
                            "value": "Consumer",
                            "languageId": 1
                        },
                        {
                            "value": "Particuliers",
                            "languageId": 13
                        },
                        {
                            "value": "个人卡",
                            "languageId": 8
                        },
                        {
                            "value": "Consumidor",
                            "languageId": 4
                        }
                    ]
                },
                {
                    "key": 39,
                    "value": "Small Business",
                    "languageId": 1,
                    "translations": [
                        {
                            "value": "小企业卡",
                            "languageId": 8
                        },
                        {
                            "value": "Empresarial",
                            "languageId": 4
                        },
                        {
                            "value": "Small Business",
                            "languageId": 1
                        },
                        {
                            "value": "Pequeno negócio",
                            "languageId": 22
                        },
                        {
                            "value": "شركة صغيرة",
                            "languageId": 7
                        },
                        {
                            "value": "Малый бизнес",
                            "languageId": 5
                        },
                        {
                            "value": "中小企業卡",
                            "languageId": 9
                        },
                        {
                            "value": "중소기업",
                            "languageId": 6
                        },
                        {
                            "value": "小企業卡",
                            "languageId": 23
                        },
                        {
                            "value": "Pequeno negócio",
                            "languageId": 3
                        },
                        {
                            "value": "Professionnels",
                            "languageId": 13
                        }
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
                {
                    "key": 12,
                    "value": "Bahasa Indonesia"
                },
                {
                    "key": 20,
                    "value": "Canadian English"
                },
                {
                    "key": 21,
                    "value": "Canadian French"
                },
                {
                    "key": 28,
                    "value": "Croatian"
                },
                {
                    "key": 1,
                    "value": "English"
                },
                {
                    "key": 13,
                    "value": "French"
                },
                {
                    "key": 16,
                    "value": "Georgian"
                },
                {
                    "key": 25,
                    "value": "German"
                },
                {
                    "key": 27,
                    "value": "Hebrew"
                },
                {
                    "key": 26,
                    "value": "Italian"
                },
                {
                    "key": 2,
                    "value": "Japanese"
                },
                {
                    "key": 15,
                    "value": "Kazakh"
                },
                {
                    "key": 24,
                    "value": "Khmer"
                },
                {
                    "key": 19,
                    "value": "Kinyarwanda"
                },
                {
                    "key": 6,
                    "value": "Korean"
                },
                {
                    "key": 22,
                    "value": "Portuguese (Brazillian)"
                },
                {
                    "key": 3,
                    "value": "Portuguese (Regular)"
                },
                {
                    "key": 5,
                    "value": "Russian"
                },
                {
                    "key": 18,
                    "value": "Serbian"
                },
                {
                    "key": 8,
                    "value": "Simplified Chinese"
                },
                {
                    "key": 4,
                    "value": "Spanish"
                },
                {
                    "key": 11,
                    "value": "Thai"
                },
                {
                    "key": 23,
                    "value": "Traditional Chinese (HK)"
                },
                {
                    "key": 9,
                    "value": "Traditional Chinese (TW)"
                },
                {
                    "key": 17,
                    "value": "Ukrainian"
                },
                {
                    "key": 10,
                    "value": "Vietnamese"
                }
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
