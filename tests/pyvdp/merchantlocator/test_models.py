import unittest

from pyvdp.merchantlocator import LocatorModel


class TestMerchantLocatorModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'header': object,
            'searchAttrList': object,
            'responseAttrList': object,
            'searchOptions': object
        }

        model = LocatorModel(**attrs)

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

        model = LocatorModel.Header(**attrs)

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

        model = LocatorModel.SearchAttrList(**attrs)

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

        model = LocatorModel.SearchOptions(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
