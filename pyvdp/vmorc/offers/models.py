class ByOfferIdModel(object):
    """Visa MORC Offers Data API Offer ID data model.
    
    https://developer.visa.com/products/vmorc/reference#vmorc__offers_data_api__v1__retrieve_offers_by_offer_id
    
    :param str offerid: **Required**. Offer identifier. Can be comma-separated set of identifiers.
    :param str updatefrom: **Optional**. Offers, that are updated after specified date. yyyymmdd string.
    :param str updateto: **Optional**. Offers, that are updated before a specified date. yyyymmdd string.
    :param int start_index: **Optional**. Index of starting element in resulting collection. Default is 1.
    :param int max_offers: **Optional**. Maximum amount of offers in resulting collection. Default is 500.
    
    **Request:**
    
    ..  code:: http
    
        GET vmorc/offers/v1/byofferid?offerid=101854&updatefrom=20140801&updateto=20161030
    
    **Response:**
    
    ..  code:: json
    
        {
            "ReturnedResults": 1,
            "StartIndex": 1,
            "Offers": [
                {
                    "indexNumber": 1,
                    "offerContentId": 104863,
                    "offerId": 101854,
                    "currentVersion": 6,
                    "activeIndicator": true,
                    "soldOut": false,
                    "offerStatus": "Approved",
                    "lastModifiedDatetime": "Wed, 11 Mar 2015 19:58:02 GMT",
                    "programId": 100530,
                    "programName": "VMORC Offer Program",
                    "languageId": 1,
                    "language": "English",
                    "merchantList": [
                        {
                            "merchantId": 100057,
                            "merchant": "Merchant One",
                            "merchantAddress": [],
                            "merchantImages": [
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
                                    "defaultMerchImg": false,
                                    "imageFileSize": "6.0 KB",
                                    "imageFileHeight": "60 px",
                                    "imageFileWidth": "160 px",
                                    "languageIds": [
                                        22,
                                        1
                                    ],
                                    "languages": [
                                        "Portuguese (Brazillian)",
                                        "English"
                                    ],
                                    "logoAltTag": ""
                                },
                                { ... },
                                { ... }
                            ]
                        }
                    ],
                    "offerTitle": "Save 20%",
                    "featuredOfferIndicator": false,
                    "validityFromDate": "May 1, 2014 GMT",
                    "validityToDate": "Dec 31, 2016 GMT",
                    "promotionFromDate": "May 1, 2014 GMT",
                    "promotionToDate": "Dec 31, 2016 GMT",
                    "promotionChannelList": [
                        {
                            "key": 1,
                            "value": "Print"
                        },
                        {
                            "key": 3,
                            "value": "Online"
                        },
                        { ... },
                        { ... },
                        { ... }
                    ],
                    "socialMediaSharingTypes": [
                        {
                            "key": 121,
                            "value": "Email"
                        },
                        {
                            "key": 122,
                            "value": "Facebook"
                        },
                        {
                            "key": 123,
                            "value": "Twitter"
                        }
                    ],
                    "shareTitle": "Save 20% with your Visa card",
                    "redemptionChannelList": [
                        {
                            "key": 48,
                            "value": "Online /Web/eCommerce"
                        },
                        {
                            "key": 49,
                            "value": "Call Phone #"
                        }
                    ],
                    "promotionRestrictions": {
                        "richText": "",
                        "text": ""
                    },
                    "isOfferEvent": false,
                    "eventSubTitle": "",
                    "dateLocations": [],
                    "offerShortDescription": {
                        "richText": "<p>Save 20% on your purchase!</p>",
                        "text": "Save 20% on your purchase!"
                    },
                    "offerCopy": {
                        "richText": "<p>Save 20%* on the merchandise value** of your purchase when you pay with your Visa card.</p>",
                        "text": "Save 20%* on the merchandise value** of your purchase when you pay with your Visa card."
                    },
                    "legalCountryExclusions": {
                        "richText": "",
                        "text": ""
                    },
                    "merchantTerms": {
                        "richText": "<ul>
                        <li>Items may vary and are subject to availability and delivery rules and times.</li></ul>",
                        "text": "Items may vary and are subject to availability and delivery rules and times."
                    },
                    "visaTerms": {
                        "richText": "<ul> <li>Offer subject to change</li> </ul>",
                        "text": "Offer subject to change"
                    },
                    "fAQs": {
                        "richText": "",
                        "text": ""
                    },
                    "redemptionTelephone": {
                        "richText": "",
                        "text": ""
                    },
                    "redemptionUrl": "<a href="http://www.visa.com/>http://www.visa.com/</a>",
                    "redemptionEmail": "",
                    "redemptionCode": "VISA",
                    "imageList": [
                        {
                            "key": 110371,
                            "imageResolution": "Low",
                            "description": "",
                            "fileLocation": "http://visateam.visa.stage.qts.visa.com/images/merchantoffers/2014-09-30/1412117522602.offerImage_770x550.png",
                            "imageFileSize": "691.0 KB",
                            "imageFileHeight": "550 px",
                            "imageFileWidth": "770 px",
                            "offerImagePromotionChannels": [
                                "Print",
                                "Email",
                                "Online",
                                "Mobile",
                                "SMS",
                                "In Store / Offline",
                                "Social",
                                "Direct Mail"
                            ],
                            "offerImagePromotionChannelIds": [
                                1,
                                82,
                                3,
                                83,
                                84,
                                5,
                                85,
                                6
                            ],
                            "imageAltTag": ""
                        }
                    ],
                    "barcode": null,
                    "redemptionFormatInstructions": "",
                    "qrCode": null,
                    "offerSource": "Aimia Marketing",
                    "offerSourceContact": "",
                    "redemptionCountries": [
                        {
                            "key": 234,
                            "value": "United States of America"
                        }
                    ],
                    "promotingCountries": [
                        {
                            "key": 234,
                            "value": "United States of America"
                        }
                    ],
                    "cardProductList": [
                        {
                            "key": 15,
                            "value": "Visa Platinum"
                        },
                        {
                            "key": 16,
                            "value": "Visa Gold"
                        },
                        { ... },
                        { ... },
                        { ... }
                    ],
                    "cardPaymentTypeList": [
                        {
                            "key": 9,
                            "value": "Credit"
                        },
                        {
                            "key": 10,
                            "value": "Debit"
                        },
                        {
                            "key": 11,
                            "value": "Pre-Paid"
                        },
                        {
                            "key": 86,
                            "value": "Visa PayWave"
                        }
                    ],
                    "businessSegmentList": [
                        {
                            "key": 7,
                            "value": "Commercial"
                        },
                        {
                            "key": 8,
                            "value": "Consumer"
                        },
                        {
                            "key": 39,
                            "value": "Small Business"
                        }
                    ],
                    "categorySubcategoryList": [
                        {
                            "key": 97,
                            "value": "Retail",
                            "subcategories": [
                                {
                                    "key": 101,
                                    "value": "Flowers / Gifts"
                                }
                            ]
                        }
                    ],
                    "offerType": [
                        {
                            "key": 36,
                            "value": "% Off"
                        }
                    ],
                    "creativeApprovalsEmail": "",
                    "creativeGuidelines": "",
                    "bins": [ ],
                    "rpins": [ ],
                    "binstorpins": [ ],
                    "accountranges": [ ],
                    "accountrangestorpins": [ ],
                    "offerMetadata": [ ],
                    "supData1": {
                        "richText": "",
                        "text": ""
                    },
                    "supData2": {
                        "richText": "",
                        "text": ""
                    },
                    "supData3": {
                        "richText": "",
                        "text": ""
                    },
                    "supData4": {
                        "richText": "",
                        "text": ""
                    }
                }
            ],
            "TotalFoundResults": 1
        }    
    """
    ATTRS = [
        'offerid',
        'updatefrom',
        'updateto',
        'start_index',
        'max_offers'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)


class ByContentIdModel(object):
    """Visa MORC Offers Data API Content ID data model.
    
    https://developer.visa.com/products/vmorc/reference#vmorc__offers_data_api__v1__retrieve_offers_by_content_id

    :param str contentid: **Required**. Content identifier. Can be comma-separated set of identifiers.
    :param str updatefrom: **Optional**. Offers, that are updated after specified date. yyyymmdd string.
    :param str updateto: **Optional**. Offers, that are updated before a specified date. yyyymmdd string.
    :param int start_index: **Optional**. Index of starting element in resulting collection. Default is 1.
    :param ing max_offers: **Optional**. Maximum amount of offers in resulting collection. Default is 500.
    
    **Request:**
    
    ..  code:: http
    
        GET vmorc/offers/v1/bycontentid?contentid=104863&updatefrom=20140101&updateto=20161231
        
    **Response:**
    
    ..  code:: json
    
        {
            "ReturnedResults": 1,
            "StartIndex": 1,
            "Offers": [
                {
                    "indexNumber": 1,
                    "offerContentId": 104863,
                    "offerId": 101854,
                    "currentVersion": 6,
                    "activeIndicator": true,
                    "soldOut": false,
                    "offerStatus": "Approved",
                    "lastModifiedDatetime": "Wed, 11 Mar 2015 19:58:02 GMT",
                    "programId": 100530,
                    "programName": "VMORC Offer Program",
                    "languageId": 1,
                    "language": "English",
                    "merchantList": [
                        {
                            "merchantId": 100057,
                            "merchant": "Merchant One",
                            "merchantAddress": [ ],
                            "merchantImages": [
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
                                    "defaultMerchImg": false,
                                    "imageFileSize": "6.0 KB",
                                    "imageFileHeight": "60 px",
                                    "imageFileWidth": "160 px",
                                    "languageIds": [
                                        22,
                                        1
                                    ],
                                    "languages": [
                                        "Portuguese (Brazillian)",
                                        "English"
                                    ],
                                    "logoAltTag": ""
                                },
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
                                    "defaultMerchImg": false,
                                    "imageFileSize": "20.0 KB",
                                    "imageFileHeight": "120 px",
                                    "imageFileWidth": "320 px",
                                    "languageIds": [
                                        22,
                                        1
                                    ],
                                    "languages": [
                                        "Portuguese (Brazillian)",
                                        "English"
                                    ],
                                    "logoAltTag": ""
                                }
                            ]
                        }
                    ],
                    "offerTitle": "Save 20%",
                    "featuredOfferIndicator": false,
                    "validityFromDate": "May 1, 2014 GMT",
                    "validityToDate": "Dec 31, 2016 GMT",
                    "promotionFromDate": "May 1, 2014 GMT",
                    "promotionToDate": "Dec 31, 2016 GMT",
                    "promotionChannelList": [
                        {
                            "key": 1,
                            "value": "Print"
                        },
                        {
                            "key": 3,
                            "value": "Online"
                        },
                        {
                            "key": 5,
                            "value": "In Store / Offline"
                        },
                        { ... },
                        { ... },
                        { ... }
                        
                    ],
                    "socialMediaSharingTypes": [
                        {
                            "key": 121,
                            "value": "Email"
                        },
                        {
                            "key": 122,
                            "value": "Facebook"
                        },
                        {
                            "key": 123,
                            "value": "Twitter"
                        }
                    ],
                    "shareTitle": "Save 20% with your Visa card",
                    "redemptionChannelList": [
                        {
                            "key": 48,
                            "value": "Online /Web/eCommerce"
                        },
                        {
                            "key": 49,
                            "value": "Call Phone #"
                        }
                    ],
                    "promotionRestrictions": {
                        "richText": "",
                        "text": ""
                    },
                    "isOfferEvent": false,
                    "eventSubTitle": "",
                    "dateLocations": [ ],
                    "offerShortDescription": {
                        "richText": "<p>Save 20% on your purchase!</p>",
                        "text": "Save 20% on your purchase!"
                    },
                    "offerCopy": {
                        "richText": "<p>Save 20%* on the merchandise value** of your purchase when you pay with your Visa card.</p>",
                        "text": "Save 20%* on the merchandise value** of your purchase when you pay with your Visa card."
                    },
                    "legalCountryExclusions": {
                        "richText": "",
                        "text": ""
                    },
                    "merchantTerms": {
                        "richText": "<ul>
                        <li>Items may vary and are subject to availability and delivery rules and times.</li></ul>",
                        "text": "Items may vary and are subject to availability and delivery rules and times."
                    },
                    "visaTerms": {
                        "richText": "<ul> <li>Offer subject to change</li> </ul>",
                        "text": "Offer subject to change"
                    },
                    "fAQs": {
                        "richText": "",
                        "text": ""
                    },
                    "redemptionTelephone": {
                        "richText": "",
                        "text": ""
                    },
                    "redemptionUrl": "<a href="http://www.visa.com/>http://www.visa.com/</a>",
                    "redemptionEmail": "",
                    "redemptionCode": "VISA",
                    "imageList": [
                        {
                            "key": 110371,
                            "imageResolution": "Low",
                            "description": "",
                            "fileLocation": "http://visateam.visa.stage.qts.visa.com/images/merchantoffers/2014-09-30/1412117522602.offerImage_770x550.png",
                            "imageFileSize": "691.0 KB",
                            "imageFileHeight": "550 px",
                            "imageFileWidth": "770 px",
                            "offerImagePromotionChannels": [
                                "Print",
                                "Email",
                                "Online",
                                "Mobile",
                                "SMS",
                                "In Store / Offline",
                                "Social",
                                "Direct Mail"
                            ],
                            "offerImagePromotionChannelIds": [
                                1,
                                82,
                                3,
                                83,
                                84,
                                5,
                                85,
                                6
                            ],
                            "imageAltTag": ""
                        }
                    ],
                    "barcode": null,
                    "redemptionFormatInstructions": "",
                    "qrCode": null,
                    "offerSource": "Aimia Marketing",
                    "offerSourceContact": "",
                    "redemptionCountries": [
                        {
                            "key": 234,
                            "value": "United States of America"
                        }
                    ],
                    "promotingCountries": [
                        {
                            "key": 234,
                            "value": "United States of America"
                        }
                    ],
                    "cardProductList": [
                        {
                            "key": 15,
                            "value": "Visa Platinum"
                        },
                        {
                            "key": 16,
                            "value": "Visa Gold"
                        },
                        { ... },
                        { ... },
                        { ... }
                    ],
                    "cardPaymentTypeList": [
                        {
                            "key": 9,
                            "value": "Credit"
                        },
                        {
                            "key": 10,
                            "value": "Debit"
                        },
                        {
                            "key": 11,
                            "value": "Pre-Paid"
                        },
                        {
                            "key": 86,
                            "value": "Visa PayWave"
                        }
                    ],
                    "businessSegmentList": [
                        {
                            "key": 7,
                            "value": "Commercial"
                        },
                        {
                            "key": 8,
                            "value": "Consumer"
                        },
                        {
                            "key": 39,
                            "value": "Small Business"
                        }
                    ],
                    "categorySubcategoryList": [
                        {
                            "key": 97,
                            "value": "Retail",
                            "subcategories": [
                                {
                                    "key": 101,
                                    "value": "Flowers / Gifts"
                                }
                            ]
                        }
                    ],
                    "offerType": [
                        {
                            "key": 36,
                            "value": "% Off"
                        }
                    ],
                    "creativeApprovalsEmail": "",
                    "creativeGuidelines": "",
                    "bins": [ ],
                    "rpins": [ ],
                    "binstorpins": [ ],
                    "accountranges": [ ],
                    "accountrangestorpins": [ ],
                    "offerMetadata": [ ],
                    "supData1": {
                        "richText": "",
                        "text": ""
                    },
                    "supData2": {
                        "richText": "",
                        "text": ""
                    },
                    "supData3": {
                        "richText": "",
                        "text": ""
                    },
                    "supData4": {
                        "richText": "",
                        "text": ""
                    }
                }
            ],
            "TotalFoundResults": 1
        }    
    """
    ATTRS = [
        'contentid',
        'updatefrom',
        'updateto',
        'start_index',
        'max_offers'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)


class ByFilterModel(object):
    """Visa MORC Offers Data API - Filter data model.
    
    https://developer.visa.com/products/vmorc/reference#vmorc__offers_data_api__v1__retrieve_offers_by_filter
    
    See `Request and Response codes <https://developer.visa.com/products/vmorc/reference#vmorc__offers_data_api__v1__retrieve_offers_by_filter>`_
    for details regarding attributes.

    :param str business_segment: **Optional**. 
    :param str card_payment_type: **Optional**. 
    :param str card_product: **Optional**. 
    :param str category: **Optional**. 
    :param str subcategory: **Optional**. 
    :param str merchant: **Optional**. 
    :param str program: **Optional**. 
    :param str promotion_channel: **Optional**. 
    :param str promoting_region: **Optional**. 
    :param str promoting_country: **Optional**. 
    :param str redemption_region: **Optional**. 
    :param str redemption_country: **Optional**. 
    :param str merchant_region: **Optional**. 
    :param str merchant_country: **Optional**. 
    :param str language: **Optional**. 
    :param bool expired: **Optional**. 
    :param str validfrom: **Optional**. Offer redemption date is on or after this date. yyyymmdd string.
    :param str validto: **Optional**. Offer redemption date is on or before this date. yyyymmdd string.
    :param str promotedfrom: **Optional**. Offer promotion date is on or after this date. yyyymmdd string.  
    :param str promotedto: **Optional**. Offer promotion date is on or before  this date yyyymmdd string.
    :param str updatefrom: **Optional**. Offer last modified date is on or after this date. yyyymmdd string.
    :param str updateto: **Optional**. Offer last modified date is on or before this date. yyyymmdd string. 
    :param bool featured: **Optional**. `True` if include only featured offers.
    :param int start_index: **Optional**. Starting index in resulting collection. Default is 1.
    :param int max_offers: **Optional**. Maximum count of offers in resulting collection. Default is 500.
    :param str bins: **Optional**. Request for offers, that fulfill to one or more comma-separated BINs.
    :param str rpins: **Optional**. Request for offers, that fulfill one or more comma-separated RPINs.
    :param str bins_to_rpins: **Optional**. Request for offers, that fulfill one or more BIN to RPIN pairing options.
    :param str accountranges: **Optional**. 
    :param str accountranges_to_rpins: **Optional**. 
    :param str pans: **Optional**. 
    :param bool non_cardAttribute: **Optional**. 
    :param str origin: **Optional**. 
    :param float radius: **Optional**. 
    :param float unit: **Optional**. 
    :param bool non_geo: **Optional**. 
    
    **Request:**
    
    ..  code:: http
    
        GET vmorc/offers/v1/byfilter?business_segment=7
    
    **Response:**
    
    ..  code:: json
    
        {
            "ReturnedResults": 1,
            "StartIndex": 1,
            "Offers": [
                {
                    "indexNumber": 1,
                    "offerContentId": 104863,
                    "offerId": 101854,
                    "currentVersion": 6,
                    "activeIndicator": true,
                    "soldOut": false,
                    "offerStatus": "Approved",
                    "lastModifiedDatetime": "Wed, 11 Mar 2015 19:58:02 GMT",
                    "programId": 100530,
                    "programName": "VMORC Offer Program",
                    "languageId": 1,
                    "language": "English",
                    "merchantList": [
                        {
                            "merchantId": 100057,
                            "merchant": "Merchant One",
                            "merchantAddress": [ ],
                            "merchantImages": [
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
                                    "defaultMerchImg": false,
                                    "imageFileSize": "6.0 KB",
                                    "imageFileHeight": "60 px",
                                    "imageFileWidth": "160 px",
                                    "languageIds": [
                                        22,
                                        1
                                    ],
                                    "languages": [
                                        "Portuguese (Brazillian)",
                                        "English"
                                    ],
                                    "logoAltTag": ""
                                },
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
                                    "defaultMerchImg": false,
                                    "imageFileSize": "20.0 KB",
                                    "imageFileHeight": "120 px",
                                    "imageFileWidth": "320 px",
                                    "languageIds": [
                                        22,
                                        1
                                    ],
                                    "languages": [
                                        "Portuguese (Brazillian)",
                                        "English"
                                    ],
                                    "logoAltTag": ""
                                }
                            ]
                        }
                    ],
                    "offerTitle": "Save 20%",
                    "featuredOfferIndicator": false,
                    "validityFromDate": "May 1, 2014 GMT",
                    "validityToDate": "Dec 31, 2016 GMT",
                    "promotionFromDate": "May 1, 2014 GMT",
                    "promotionToDate": "Dec 31, 2016 GMT",
                    "promotionChannelList": [
                        {
                            "key": 1,
                            "value": "Print"
                        },
                        {
                            "key": 3,
                            "value": "Online"
                        },
                        {
                            "key": 5,
                            "value": "In Store / Offline"
                        },
                        { ... },
                        { ... },
                        { ... }
                    ],
                    "socialMediaSharingTypes": [
                        {
                            "key": 121,
                            "value": "Email"
                        },
                        {
                            "key": 122,
                            "value": "Facebook"
                        },
                        {
                            "key": 123,
                            "value": "Twitter"
                        }
                    ],
                    "shareTitle": "Save 20% with your Visa card",
                    "redemptionChannelList": [
                        {
                            "key": 48,
                            "value": "Online /Web/eCommerce"
                        },
                        {
                            "key": 49,
                            "value": "Call Phone #"
                        }
                    ],
                    "promotionRestrictions": {
                        "richText": "",
                        "text": ""
                    },
                    "isOfferEvent": false,
                    "eventSubTitle": "",
                    "dateLocations": [ ],
                    "offerShortDescription": {
                        "richText": "<p>Save 20% on your purchase!</p>",
                        "text": "Save 20% on your purchase!"
                    },
                    "offerCopy": {
                        "richText": "<p>Save 20%* on the merchandise value** of your purchase when you pay with your Visa card.</p>",
                        "text": "Save 20%* on the merchandise value** of your purchase when you pay with your Visa card."
                    },
                    "legalCountryExclusions": {
                        "richText": "",
                        "text": ""
                    },
                    "merchantTerms": {
                        "richText": "<ul>
                        <li>Items may vary and are subject to availability and delivery rules and times.</li></ul>",
                        "text": "Items may vary and are subject to availability and delivery rules and times."
                    },
                    "visaTerms": {
                        "richText": "<ul> <li>Offer subject to change</li> </ul>",
                        "text": "Offer subject to change"
                    },
                    "fAQs": {
                        "richText": "",
                        "text": ""
                    },
                    "redemptionTelephone": {
                        "richText": "",
                        "text": ""
                    },
                    "redemptionUrl": "<a href="http://www.visa.com/>http://www.visa.com/</a>",
                    "redemptionEmail": "",
                    "redemptionCode": "VISA",
                    "imageList": [
                        {
                            "key": 110371,
                            "imageResolution": "Low",
                            "description": "",
                            "fileLocation": "http://visateam.visa.stage.qts.visa.com/images/merchantoffers/2014-09-30/1412117522602.offerImage_770x550.png",
                            "imageFileSize": "691.0 KB",
                            "imageFileHeight": "550 px",
                            "imageFileWidth": "770 px",
                            "offerImagePromotionChannels": [
                                "Print",
                                "Email",
                                "Online",
                                "Mobile",
                                "SMS",
                                "In Store / Offline",
                                "Social",
                                "Direct Mail"
                            ],
                            "offerImagePromotionChannelIds": [
                                1,
                                82,
                                3,
                                83,
                                84,
                                5,
                                85,
                                6
                            ],
                            "imageAltTag": ""
                        }
                    ],
                    "barcode": null,
                    "redemptionFormatInstructions": "",
                    "qrCode": null,
                    "offerSource": "Aimia Marketing",
                    "offerSourceContact": "",
                    "redemptionCountries": [
                        {
                            "key": 234,
                            "value": "United States of America"
                        }
                    ],
                    "promotingCountries": [
                        {
                            "key": 234,
                            "value": "United States of America"
                        }
                    ],
                    "cardProductList": [
                        {
                            "key": 15,
                            "value": "Visa Platinum"
                        },
                        {
                            "key": 16,
                            "value": "Visa Gold"
                        },
                        { ... },
                        { ... },
                        { ... }
                    ],
                    "cardPaymentTypeList": [
                        {
                            "key": 9,
                            "value": "Credit"
                        },
                        {
                            "key": 10,
                            "value": "Debit"
                        },
                        { ... },
                        { ... },
                        { ... }
                    ],
                    "categorySubcategoryList": [
                        {
                            "key": 97,
                            "value": "Retail",
                            "subcategories": [
                                {
                                    "key": 101,
                                    "value": "Flowers / Gifts"
                                }
                            ]
                        }
                    ],
                    "offerType": [
                        {
                            "key": 36,
                            "value": "% Off"
                        }
                    ],
                    "creativeApprovalsEmail": "",
                    "creativeGuidelines": "",
                    "bins": [ ],
                    "rpins": [ ],
                    "binstorpins": [ ],
                    "accountranges": [ ],
                    "accountrangestorpins": [ ],
                    "offerMetadata": [ ],
                    "supData1": {
                        "richText": "",
                        "text": ""
                    },
                    "supData2": {
                        "richText": "",
                        "text": ""
                    },
                    "supData3": {
                        "richText": "",
                        "text": ""
                    },
                    "supData4": {
                        "richText": "",
                        "text": ""
                    }
                }
            ],
            "TotalFoundResults": 1
        }    
    """
    ATTRS = [
        'business_segment',
        'card_payment_type',
        'card_product',
        'category',
        'subcategory',
        'merchant',
        'program',
        'promotion_channel',
        'promoting_region',
        'promoting_country',
        'redemption_region',
        'redemption_country',
        'merchant_region',
        'merchant_country',
        'language',
        'expired',
        'validfrom',
        'validto',
        'promotedfrom',
        'promotedto',
        'updatefrom',
        'updateto',
        'featured',
        'start_index',
        'max_offers',
        'bins',
        'rpins',
        'bins_to_rpins',
        'accountranges',
        'accountranges_to_rpins',
        'pans',
        'non_cardAttribute',
        'origin',
        'radius',
        'unit',
        'non_geo'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)


class AllModel(object):
    """VISA MORC Offers Data API - Retrieve all offers data object model.
    
    https://developer.visa.com/products/vmorc/reference#vmorc__offers_data_api__v1__retrieve_all_offers
    
    :param int start_index: **Optional**. Starting index in resulting collection. Default is 1.
    :param int max_offers: **Optional**. Maximum records in resulting collection. Default is 500.
    
    **Request:**
    
    ..  code:: http
    
        GET rc/offers/v1/all?
        
    **Response:**
    
    ..  code:: json
    
        {
            "ReturnedResults": 1,
            "StartIndex": 1,
            "Offers": [
                {
                    "indexNumber": 1,
                    "offerContentId": 104863,
                    "offerId": 101854,
                    "currentVersion": 6,
                    "activeIndicator": true,
                    "soldOut": false,
                    "offerStatus": "Approved",
                    "lastModifiedDatetime": "Wed, 11 Mar 2015 19:58:02 GMT",
                    "programId": 100530,
                    "programName": "VMORC Offer Program",
                    "languageId": 1,
                    "language": "English",
                    "merchantList": [
                        {
                            "merchantId": 100057,
                            "merchant": "Merchant One",
                            "merchantAddress": [],
                            "merchantImages": [
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
                                    "defaultMerchImg": false,
                                    "imageFileSize": "6.0 KB",
                                    "imageFileHeight": "60 px",
                                    "imageFileWidth": "160 px",
                                    "languageIds": [
                                        22,
                                        1
                                    ],
                                    "languages": [
                                        "Portuguese (Brazillian)",
                                        "English"
                                    ],
                                    "logoAltTag": ""
                                },
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
                                    "defaultMerchImg": false,
                                    "imageFileSize": "20.0 KB",
                                    "imageFileHeight": "120 px",
                                    "imageFileWidth": "320 px",
                                    "languageIds": [
                                        22,
                                        1
                                    ],
                                    "languages": [
                                        "Portuguese (Brazillian)",
                                        "English"
                                    ],
                                    "logoAltTag": ""
                                }
                            ]
                        }
                    ],
                    "offerTitle": "Save 20%",
                    "featuredOfferIndicator": false,
                    "validityFromDate": "May 1, 2014 GMT",
                    "validityToDate": "Dec 31, 2016 GMT",
                    "promotionFromDate": "May 1, 2014 GMT",
                    "promotionToDate": "Dec 31, 2016 GMT",
                    "promotionChannelList": [
                        {
                            "key": 1,
                            "value": "Print"
                        },
                        {
                            "key": 3,
                            "value": "Online"
                        },
                        { ... },
                        { ... },
                        { ... }
                    ],
                    "socialMediaSharingTypes": [
                        {
                            "key": 121,
                            "value": "Email"
                        },
                        {
                            "key": 122,
                            "value": "Facebook"
                        },
                            {
                            "key": 123,
                            "value": "Twitter"
                        }
                    ],
                    "shareTitle": "Save 20% with your Visa card",
                    "redemptionChannelList": [
                        {
                            "key": 48,
                            "value": "Online /Web/eCommerce"
                        },
                        {
                            "key": 49,
                            "value": "Call Phone #"
                        }
                    ],
                    "promotionRestrictions": {
                        "richText": "",
                        "text": ""
                    },
                    "isOfferEvent": false,
                    "eventSubTitle": "",
                    "dateLocations": [ ],
                    "offerShortDescription": {
                        "richText": "<p>Save 20% on your purchase!</p>",
                        "text": "Save 20% on your purchase!"
                    },
                    "offerCopy": {
                        "richText": "<p>Save 20%* on the merchandise value** of your purchase when you pay with your Visa card.</p>",
                        "text": "Save 20%* on the merchandise value** of your purchase when you pay with your Visa card."
                    },
                    "legalCountryExclusions": {
                        "richText": "",
                        "text": ""
                    },
                    "merchantTerms": {
                        "richText": "<ul>
                        <li>Items may vary and are subject to availability and delivery rules and times.</li></ul>",
                        "text": "Items may vary and are subject to availability and delivery rules and times."
                    },
                    "visaTerms": {
                        "richText": "<ul> <li>Offer subject to change</li> </ul>",
                        "text": "Offer subject to change"
                    },
                    "fAQs": {
                        "richText": "",
                        "text": ""
                    },
                    "redemptionTelephone": {
                        "richText": "",
                        "text": ""
                    },
                    "redemptionUrl": "<a href="http://www.visa.com/>http://www.visa.com/</a>",
                    "redemptionEmail": "",
                    "redemptionCode": "VISA",
                    "imageList": [
                        {
                            "key": 110371,
                            "imageResolution": "Low",
                            "description": "",
                            "fileLocation": "http://visateam.visa.stage.qts.visa.com/images/merchantoffers/2014-09-30/1412117522602.offerImage_770x550.png",
                            "imageFileSize": "691.0 KB",
                            "imageFileHeight": "550 px",
                            "imageFileWidth": "770 px",
                            "offerImagePromotionChannels": [
                                "Print",
                                "Email",
                                "Online",
                                "Mobile",
                                "SMS",
                                "In Store / Offline",
                                "Social",
                                "Direct Mail"
                            ],
                            "offerImagePromotionChannelIds": [
                                1,
                                82,
                                3,
                                83,
                                84,
                                5,
                                85,
                                6
                            ],
                            "imageAltTag": ""
                        }
                    ],
                    "barcode": null,
                    "redemptionFormatInstructions": "",
                    "qrCode": null,
                    "offerSource": "Aimia Marketing",
                    "offerSourceContact": "",
                    "redemptionCountries": [
                        {
                            "key": 234,
                            "value": "United States of America"
                        }
                    ],
                    "promotingCountries": [
                        {
                            "key": 234,
                            "value": "United States of America"
                        }
                    ],
                    "cardProductList": [
                        {
                            "key": 15,
                            "value": "Visa Platinum"
                        },
                        {
                            "key": 16,
                            "value": "Visa Gold"
                        },
                        { ... },
                        { ... },
                        { ... }                        
                    ],
                    "cardPaymentTypeList": [
                        {
                            "key": 9,
                            "value": "Credit"
                        },
                        {
                            "key": 10,
                            "value": "Debit"
                        },
                        {
                            "key": 11,
                            "value": "Pre-Paid"
                        },
                        {
                            "key": 86,
                            "value": "Visa PayWave"
                        }
                    ],
                    "businessSegmentList": [
                        {
                            "key": 7,
                            "value": "Commercial"
                        },
                        {
                            "key": 8,
                            "value": "Consumer"
                        },
                        {
                            "key": 39,
                            "value": "Small Business"
                        }
                    ],
                    "categorySubcategoryList": [
                        {
                            "key": 97,
                            "value": "Retail",
                            "subcategories": [
                                {
                                    "key": 101,
                                    "value": "Flowers / Gifts"
                                }
                            ]
                        }
                    ],
                    "offerType": [
                        {
                            "key": 36,
                            "value": "% Off"
                        }
                    ],
                    "creativeApprovalsEmail": "",
                    "creativeGuidelines": "",
                    "bins": [ ],
                    "rpins": [ ],
                    "binstorpins": [ ],
                    "accountranges": [ ],
                    "accountrangestorpins": [ ],
                    "offerMetadata": [ ],
                    "supData1": {
                        "richText": "",
                        "text": ""
                    },
                    "supData2": {
                        "richText": "",
                        "text": ""
                    },
                    "supData3": {
                        "richText": "",
                        "text": ""
                    },
                    "supData4": {
                        "richText": "",
                        "text": ""
                    }
                }
            ],
            "TotalFoundResults": 1
        }    
    """
    ATTRS = [
        'start_index',
        'max_offers'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)
