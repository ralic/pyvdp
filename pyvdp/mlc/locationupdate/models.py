from datetime import datetime


class LocationsModel(object):
    """Visa Mobile Location Confirmation Location Update data object model.
    
    https://developer.visa.com/products/mlc/reference#mlc__mlc1
    
    :param pyvdp.mlc.locationupdate.LocationModel.Header header: **Required**. 
        Instance of :func:`~pyvdp.mlc.locationupdate.LocationsModel.Header`.
    :param str accuracy: **Optional**. Accuracy coefficient around returned coordinates. 0-10000 integer.
    :param str cloudNotificationKey: **Optional**. Unique ID, assigned by mobile OS vendor that identifies device
        for push notifications purposes. This enables VISA to send a location update request on expiration.
        4K string.
    :param int cloudNotificationProvider: **Optional**. Mobile OS vendor ID. Possible values are: 1 - Google,
        2 - Apple, 3 - Microsoft.
    :param str deviceId: **Required**. Device ID value, that must match device id, sent during enrollment request.
        See :func:`pyvdp.mlc.enrollment.enrollments`. Max 50 characters string.
    :param str issuerId: **Required**. Issuer ID provided by VISA during onboarding. 6 digits string.
    :param str deviceLocationDateTime: **Required**. Datetime for location update on mobile device. This is generated
        by mobile app. 50 characters string, YYYY-MMDDTHH:MM:SS.fffZ.
    :param GeoLocationCoordinate geoLocationCoordinate: **Required**.
        Instance of :func:`~pyvdp.mld.locationupdate.LocationsModel.GeoLocationCoordinate`.
    :param int provider: **Optional**. Location provider value. Possible values are 1 (mobile app), 2 (mobile network
        operator). Currently only '1' is supported.
    :param int source: **Required**. Mobile device event, that triggered location update. Possible values are:
        1 - location change event, 2 - wi-fi connection event.
    """
    ATTRS = [
        'header',
        'accuracy',
        'cloudNotificationKey',
        'cloudNotificationProvider',
        'deviceId',
        'deviceLocationDateTime',
        'geoLocationCoordinate',
        'issuerId',
        'provider',
        'source'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)

    class Header(object):
        """Location update request header.
        
        A part of :func:`~pyvdp.mlc.locationupdate.LocationsModel`.
        
        :param str messageId: **Required**. Unique message identifier. Max 50 characters string.
        """
        ATTRS = [
            'messageId'
        ]

        def __init__(self, **kwargs):
            for attr, value in kwargs.items():
                if attr in self.ATTRS and value:
                    self.__setattr__(attr, value)

            self.messageDateTime = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

    class GeoLocationCoordinate(object):
        """Location update request geo coordinates data model.
        
        A part of :func:`~pyvdp.mlc.locationupdate.LocationsModel`
        
        :param float latitude: **Required**. Latitude, decimal value between -90.0 and 90.0.
        :param float longitude: **Required**. Longitude, decimal value between -180.0 and 180.0
        """
        ATTRS = [
            'latitude',
            'longitude'
        ]

        def __init__(self, **kwargs):
            for attr, value in kwargs.items():
                if attr in self.ATTRS and value:
                    self.__setattr__(attr, value)
