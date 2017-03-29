import unittest

from pyvdp.visadirect.watchlist import WatchlistData


class TestWatchlistData(unittest.TestCase):

    def test_attributes(self):

        params = {
            'name': 'Mohammed',
            'address': {},
            'acquiring_bin': 12345,
            'acquirer_country_code': 123
        }

        ca = WatchlistData(**params)

        attrs = [
            'name',
            'address',
            'acquiringBin',
            'acquirerCountryCode'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(ca, attr), 'missing %s attribute' % attr)


class TestWatchlistDataAddress(unittest.TestCase):

    def test_attributes(self):

        params = {
            'city': 'San Francisco',
            'issuer_country_code': 'USA',
        }

        ca = WatchlistData.WatchlistDataAddress(**params)

        attrs = [
            'city',
            'cardIssuerCountryCode',
        ]

        for attr in attrs:
            self.assertTrue(hasattr(ca, attr), 'missing %s attribute' % attr)
