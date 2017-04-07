import unittest

from pyvdp.visadirect.watchlist import WatchlistDataModel


class TestWatchlistDataModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'name': 'Mohammed',
            'address': object,
            'acquiringBin': 12345,
            'acquirerCountryCode': 123
        }

        model = WatchlistDataModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestWatchlistDataAddress(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'city': 'San Francisco',
            'cardIssuerCountryCode': 'USA',
        }

        model = WatchlistDataModel.WatchlistDataAddress(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)

