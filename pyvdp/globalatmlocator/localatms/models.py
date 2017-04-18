from datetime import datetime


class AbstractInquiryModel(object):
    """Abstract base model for Global ATM Locator APIs.
    
    This class is not meant to be instantiated on its own. Instead it should be inherited by concrete
    models.
    
    :param pyvdp.globalatmlocator.localatms.AbstractInquiryModel.RequestData requestData: **Required**. 
        Instance of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel.RequestData`.
    :param WsRequestHeaderV2 wsRequestHeaderV2: **Required**. 
        Instance of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel.WsRequestHeaderV2`.
    """
    ATTRS = [
        'requestData',
        'wsRequestHeaderV2',
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)

    class WsRequestHeaderV2(object):
        """Abstract request header.
        
        Part of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel`.
        
        Implemented by child classes as a part of their models.
        
        :param str applicationId: **Optional**. Application short name of the request originator.
        :param str requestMessageId: **Optional**. Request unique identifier.
        :param str correlationId: **Optional**. A string used to identify set of requests.
        :param str userId: **Optional**. User ID of the requesting user. May be '0' or 'NONE'.
        :param str userBid: **Optional**. Business User ID of the requesting user. May be '0' or 'NONE'.
        """
        ATTRS = [
            'applicationId',
            'requestMessageId',
            'correlationId',
            'userId',
            'userBid'
        ]

        def __init__(self, **kwargs):
            for attr, value in kwargs.items():
                if attr in self.ATTRS and value:
                    self.__setattr__(attr, value)

            self.requestTs = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

    class RequestData(object):
        """Abstract request data.
        
        Part of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel`.
        
        Implemented by child classes as a part of their models.
        
        :param str culture: **Optional**. A culture. Possible values: en-US.
        :param str distance: **Optional**. Search radius from initial point.
        :param str distanceUnit: **Optional**. Distance units for *distance* argument. Possible values: *mi*, *km*.
        :param Location location: **Required**. 
            Instance of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel.RequestData.Location`.
        :param Options options: **Required**.
            Instance of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel.RequestData.Options`.
        :param str metaDataOptions: **TODO: Undocumented**.
        """
        ATTRS = [
            'culture',
            'distance',
            'distanceUnit',
            'location',
            'options',
            'metaDataOptions'
        ]

        def __init__(self, **kwargs):
            for attr, value in kwargs.items():
                if attr in self.ATTRS and value:
                    self.__setattr__(attr, value)

        class Location(object):
            """Abstract Location data.
            
            Part of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel.RequestData`.
            
            Implemented by child classes as a part of their models.
            
            :param str address: **TODO: Undocumented**.
            :param str placeName: **Conditional**. Single line address. Mandatory if Geocodes (latitude and/or 
                longitude) are not provided.
            :param Geocodes geocodes: **Conditional**. 
                Instance of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel.RequestData.Location.Geocodes`.
            """
            ATTRS = [
                'placeName',
                'geocodes'
            ]

            def __init__(self, **kwargs):
                for attr, value in kwargs.items():
                    if attr in self.ATTRS and value:
                        self.__setattr__(attr, value)

            class Geocodes(object):
                """Abstract Geocodes data.
                
                Part of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel.RequestData.Location`.
                
                Implemented by child classes as a part of their models.
                
                :param int latitude: **Conditional**. Search center point latitude. Required if placeName is not
                    provided.
                :param int longitude: **Conditional**. Search center point longitude. Required if placeName is not
                    provided.
                """
                ATTRS = [
                    'latitude',
                    'longitude'
                ]

                def __init__(self, **kwargs):
                    for attr, value in kwargs.items():
                        if attr in self.ATTRS and value:
                            self.__setattr__(attr, value)

        class Options(object):
            """Abstract request options.
            
            Part of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel.RequestData`.
            
            :param Range range: **Required**. 
                Instance of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel.RequestData.Options.Range`.
            :param Sort sort: **Required**.
                Instance of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel.RequestData.Options.Sort`.
            :param str operationName: **Optional**. Logical operation to apply on findFilters. Possible values:
                *and*, *or*.
            :param list findFilters: **Optional**. A list of filters. 'Filter' is a dictionary with 'filterName' 
                and 'filterValue' pairs. See https://developer.visa.com/products/atmlocator/reference for details.
            :param bool useFirstAmbiguous: **TODO: Undocumented**.
            """
            ATTRS = [
                'range',
                'sort',
                'operationName',
                'findFilters',
                'useFirstAmbiguous'
            ]

            def __init__(self, **kwargs):
                for attr, value in kwargs.items():
                    if attr in self.ATTRS and value:
                        self.__setattr__(attr, value)

            class Range(object):
                """Abstract request range.
                
                Part of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel.RequestData.Options`.
                
                :param int start: **Required**. Starting index of response records. E.g. *'0'*.
                :param int count: **Required**. A number of records to fetch. E.g. *'100'*.
                """
                ATTRS = [
                    'count',
                    'start'
                ]

                def __init__(self, **kwargs):
                    for attr, value in kwargs.items():
                        if attr in self.ATTRS and value:
                            self.__setattr__(attr, value)

            class Sort(object):
                """Abstract request sort.
                
                Part of :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel.RequestData.Options`.
                
                :param str primary: **Required**. Primary sort filter. Possible values: *distance*, *city*.
                :param str direction: **Required**. Sort direction. Possible values: *asc*, *desc*.
                :param str secondary: **Optional**. Secondary sort filter. Possible values: *distance*, *city*.
                """
                ATTRS = [
                    'direction',
                    'primary',
                    'secondary'
                ]

                def __init__(self, **kwargs):
                    for attr, value in kwargs.items():
                        if attr in self.ATTRS and value:
                            self.__setattr__(attr, value)


class AtmsInquiryModel(AbstractInquiryModel):
    """ATMs Inquiry data object model.
    
    https://developer.visa.com/products/atmlocator/guides#using_the_atms_inquiry_operation
    
    See :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel`.
    """
    def __init__(self, **kwargs):
        super(AtmsInquiryModel, self).__init__(**kwargs)


class TotalsInquiryModel(AbstractInquiryModel):
    """Totals Inquiry data object model.

    https://developer.visa.com/products/atmlocator/guides#using_the_totals_inquiry_operation

    See :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel`.
    """
    def __init__(self, **kwargs):
        super(TotalsInquiryModel, self).__init__(**kwargs)


class GeocodesInquiryModel(AbstractInquiryModel):
    """Geocodes Inquiry data object model.

    https://developer.visa.com/products/atmlocator/guides#using_the_geocode_inquiry_operation

    See :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel`.
    """
    def __init__(self, **kwargs):
        super(GeocodesInquiryModel, self).__init__(**kwargs)


class RoutesInquiryModel(AbstractInquiryModel):
    """Geocodes Inquiry data object model.

    https://developer.visa.com/products/atmlocator/guides#using_the_routes_inquiry_operation

    See :func:`~pyvdp.globalatmlocator.localatms.AbstractInquiryModel`.
    """
    def __init__(self, **kwargs):
        super(RoutesInquiryModel, self).__init__(**kwargs)

    class RequestData(object):
        """Routes Inquiry request data object model.
        
        Part of :func:`~pyvdp.globalatmlocator.localatms.RoutesInquiryModel`.
        
        :param bool doNotLocateOnRestrictedElements: **TODO: Undocumented**.
        :param list features: **TODO: Undocumented**. 
            A list of :func:`~pyvdp.globalatmlocator.localatms.RoutesInquiryModels.RequestData.Geometry` objects.
        :param pyvdp.globalatmlocator.localatms.RoutesInquiryModels.RequestData.TravelMode travelMode:
            **TODO: Undocumented**.
        :param str type: **TODO: Undocumented**.
        """
        ATTRS = [
            'doNotLocateOnRestrictedElements',
            'features',
            'travelMode',
            'type'
        ]

        def __init__(self, **kwargs):
            for attr, value in kwargs.items():
                if attr in self.ATTRS and value:
                    self.__setattr__(attr, value)

        class Geometry(object):
            """Geometry data object model.
            
            Part of :func:`~pyvdp.globalatmlocator.localatms.RoutesInquiryModel.RequestData`.
            
            :param float x: **Required**. X-coordinate. E.g. -122.4079.
            :param float y: **Required**. Y-coordinate. E.g. 37.782
            """
            ATTRS = [
                'x',
                'y'
            ]

            def __init__(self, **kwargs):
                for attr, value in kwargs.items():
                    if attr in self.ATTRS and value:
                        self.__setattr__(attr, value)

        class TravelMode(object):
            """Geocodes request travel mode data object model.
            
            Part of :func:`~pyvdp.globalatmlocator.localatms.RoutesInquiryModel.RequestData`.
            
            :param str type: **TODO: Undocumented**.
            """
            ATTRS = [
                'type'
            ]

            def __init__(self, **kwargs):
                for attr, value in kwargs.items():
                    if attr in self.ATTRS and value:
                        self.__setattr__(attr, value)
