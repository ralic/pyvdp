import unittest

from pyvdp.merchantsearch import SearchModel


class TestMerchantSearchModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'header': object,
            'searchAttrList': object,
            'responseAttrList': list,
            'searchOptions': object
        }

        model = SearchModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestMerchantSearchHeader(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'requestMessageId': 'Request_007',
            'startIndex': 0
        }

        model = SearchModel.MerchantSearchHeader(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestMerchantSearchAttrList(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'merchantName': 'ACME',
            'merchantStreetAddress': 'ELm Street',
            'merchantCity': 'LA',
            'merchantState': 'CA',
            'merchantPostalCode': '12345',
            'merchantCountryCode': '1234',
            'merchantPhoneNumber': '111111111',
            'merchantUrl': 'http://localhost',
            'visaMerchantId': '123',
            'visaStoreId': '123',
            'businessRegistrationId': '123',
            'acquirerCardAcceptorId': '123',
            'acquiringBin': '123',
        }

        model = SearchModel.MerchantSearchAttrList(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestMerchantSearchOptions(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'maxRecords': '123',
            'matchIndicators': '123',
            'matchScore': '123',
            'proximity': 'acme',
            'wildcards': 'acme'
        }

        model = SearchModel.MerchantSearchOptions(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
