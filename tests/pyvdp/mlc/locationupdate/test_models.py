import unittest

from pyvdp.mlc.locationupdate import LocationsModel


class TestLocationsModel(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'accuracy': str,
            'cloudNotificationKey': str,
            'cloudNotificationProvider': str,
            'deviceId': str,
            'deviceLocationDateTime': str,
            'geoLocationCoordinate': object,
            'header': object,
            'issuerId': str,
            'provider': str,
            'source': str
        }

        model = LocationsModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestGeoLocationCoordinate(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'latitude': float,
            'longitude': float
        }

        model = LocationsModel.GeoLocationCoordinate(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestHeader(unittest.TestCase):

    def test_attribute(self):
        attrs = {
            'messageId': str
        }

        model = LocationsModel.Header(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
