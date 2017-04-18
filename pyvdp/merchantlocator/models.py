import time

from datetime import datetime


class MerchantLocatorModel(object):
    """MerchantLocatorModel data object model for Merchant Locator APIs.
    
    https://developer.visa.com/products/merchant_locator/reference
    
    :param pyvdp.merchantlocator.MerchantLocatorModel.Header header: **Optional**. 
        Instance of :func:`~pyvdp.merchantlocator.MerchantLocatorModel.Header`.
        If not provided, will be set automatically. See docs for Header subclass.
    :param SearchAttrList searchAttrList: **Required**. 
        Instance of :func:`~pyvdp.merchantlocator.MerchantLocatorModel.SearchAttrList`.
    :param list responseAttrList: **Required**. A list of response attributes.
    :param SearchOptions searchOptions: **Required**. 
        Instance of :func:`~pyvdp.merchantlocator.MerchantLocatorModel.SearchOptions`.
    """
    ATTRS = [
        'header',
        'searchAttrList',
        'responseAttrList',
        'searchOptions'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)

        if 'header' not in kwargs:
            self.header = MerchantLocatorModel.Header()

    class Header(object):
        """Merchant Locator request header object.
        
        Part of MerchantLocatorModel object.
        
        :param str requestMessageId: **Optional**. Unique request identifier. If not provided, generated automatically.
        :param int startIndex: **Optional**. Starting index in response object. Default 0.
        """

        def __init__(self, **kwargs):
            self.messageDateTime = self._get_datetime()

            if kwargs and 'requestMessageId' in kwargs:
                self.requestMessageId = kwargs['requestMessageId']
            else:
                self.requestMessageId = self._get_message_id()

            if kwargs and 'startIndex' in kwargs:
                self.startIndex = kwargs['startIndex']
            else:
                self.startIndex = 0

        @staticmethod
        def _get_datetime():
            date_format = '%Y-%m-%dT%H:%M:%S.%f'
            now = datetime.now()
            return now.strftime(date_format)[:-3]

        @staticmethod
        def _get_message_id():
            return 'Request_' + str(int(time.time()))

    class SearchAttrList(object):
        """Merchant Locator search attributes object.
        
        Part of MerchantLocatorModel object.
        
        :param str merchantName: **Conditional**. Name of the merchant. Not required if MCC or phone number provided.
        :param str merchantCategoryCode: **Conditional**. Merchant category code or codes. Not required if merchant
            name or phone number provided. Can be a list of comma-separated values.
        :param int merchantCountryCode: **Required**. Merchant country ISO code. 3 characters string.
        :param int distance: **Required**. Distance value. Integer in 0-100 range.
        :param str distanceUnit: **Required**. Distance unit. M or KM.
        :param str merchantStreetAddress: **Optional**. Merchant street address.
        :param str merchantCity: **Optional**. Merchant city name. 
        :param str merchantState: **Optional**. Merchant state code.
        :param str merchantPostalCode: **Conditional**. Merchant postal code. Must not be provided if latitude and
            longitude are set.
        :param str longitude: **Conditional**. Longitude value between -180 and +180. Must not be provided if postal 
            code is set.
        :param str latitude: **Conditional**. Latitude value between -90 and +90. Must not be provided if postal 
            code is set. 
        :param int merchantPhoneNumber: **Optional**. Phone number of the registered Merchant.
        """
        ATTRS = [
            'merchantName',
            'merchantCategoryCode',
            'merchantCountryCode',
            'distance',
            'distanceUnit',
            'merchantStreetAddress',
            'merchantCity',
            'merchantState',
            'merchantPostalCode',
            'longitude',
            'latitude',
            'merchantPhoneNumber'
        ]

        def __init__(self, **kwargs):
            for attr, value in kwargs.items():
                if attr in self.ATTRS and value:
                    self.__setattr__(attr, value)

    class SearchOptions(object):
        """Merchant locator search options object.
        
        Part of MerchantLocatorModel object.
        
        :param int maxRecords: **Optional**. Maximum number of records in the response. Default 25.
        :param bool matchIndicators: **Optional**. If set to True, matching request attributes will be included in 
            response.
        :param bool matchScore: **Optional**. If set to True, matching score will be included in response.
        :param str proximity: **Optional**. A proximity search tag on merchant name. Ignored if wildcard is provided.
        :param str wildcard: **Optional**. A wildcard search on merchant name.
        """
        ATTRS = [
            'maxRecords',
            'matchIndicators',
            'matchScore',
            'proximity',
            'wildcard'
        ]

        def __init__(self, **kwargs):
            for attr, value in kwargs.items():
                if attr in self.ATTRS and value:
                    self.__setattr__(attr, value)
