import unittest

from pyvdp.visadirect.watchlist import WatchListInquiryModel


class TestWatchlistDataModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'name': 'Mohammed',
            'address': object,
            'acquiringBin': 12345,
            'acquirerCountryCode': 123
        }

        model = WatchListInquiryModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestWatchlistDataAddress(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'city': 'San Francisco',
            'cardIssuerCountryCode': 'USA',
        }

        model = WatchListInquiryModel.WatchListInquiryAddress(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)

