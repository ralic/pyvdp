import unittest

from pyvdp.merchantlocator import MerchantLocatorModel


class TestMerchantLocatorModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'header': object,
            'searchAttrList': object,
            'responseAttrList': object,
            'searchOptions': object
        }

        model = MerchantLocatorModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestMerchantLocatorHeader(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'messageDateTime': str,
            'requestMessageId': str,
            'startIndex': int,
        }

        model = MerchantLocatorModel.Header(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)


class TestMerchantLocatorSearchAttrList(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'merchantName': str,
            'merchantCountryCode': int,
            'latitude': float,
            'longitude': float,
            'distance': int,
            'distanceUnit': str
        }

        model = MerchantLocatorModel.SearchAttrList(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestMerchantLocatorSearchOptions(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'maxRecords': int,
            'matchIndicators': bool,
            'matchScore': bool
        }

        model = MerchantLocatorModel.SearchOptions(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
