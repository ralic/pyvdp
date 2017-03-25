import unittest

from pyvdp.visadirect.watchlist.data import WatchlistObject, WatchlistObjectAddress


class TestWatchlistObject(unittest.TestCase):

    def test_hasName(self):
        wo = WatchlistObject(city='', issuer_country_code='', name='John Doe')
        self.assertTrue(hasattr(wo, 'name'))

    def test_hasReferenceNumber(self):
        wo = WatchlistObject(city='', issuer_country_code='')
        self.assertTrue(hasattr(wo, 'referenceNumber'))

    def test_hasAddress(self):
        wo = WatchlistObject(city='', issuer_country_code='', address=object)
        self.assertTrue(hasattr(wo, 'address'))


class TestWatchlistObjectAddress(unittest.TestCase):

    def test_hasCity(self):
        woa = WatchlistObjectAddress(city='SFO')
        self.assertTrue(hasattr(woa, 'city'))

    def test_hasCardIssuerCountryCode(self):
        woa = WatchlistObjectAddress(issuer_country_code='US')
        self.assertTrue(hasattr(woa, 'cardIssuerCountryCode'))
