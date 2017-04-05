import unittest

from pyvdp.merchantsearch import MerchantSearch


class TestMerchantSearchData(unittest.TestCase):

    def test_attributes(self):

        params = {
            'header': object,
            'search_attr_list': object,
            'response_attr_list': list,
            'options': object
        }

        data = MerchantSearch(**params)

        attrs = [
            'header',
            'searchAttrList',
            'responseAttrList',
            'searchOptions',
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestMerchantSearchHeader(unittest.TestCase):

    def test_attributes(self):

        params = {
            'message_id': 'Request_007',
            'start_index': 0
        }

        data = MerchantSearch.MerchantSearchHeader(**params)

        attrs = [
            'requestMessageId',
            'startIndex'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestMerchantSearchAttrList(unittest.TestCase):

    def test_attributes(self):

        params = {
            'merchant_name': 'ACME',
            'merchant_street_address': 'ELm Street',
            'merchant_city': 'LA',
            'merchant_state': 'CA',
            'merchant_postal_code': '12345',
            'merchant_country_code': '1234',
            'merchant_phone_number': '111111111',
            'merchant_url': 'http://localhost',
            'visa_merchant_id': '123',
            'visa_store_id': '123',
            'business_registration_id': '123',
            'acquirer_card_acceptor_id': '123',
            'acquiring_bin': '123',
        }

        data = MerchantSearch.MerchantSearchAttrList(**params)

        attrs = [
            'merchantName',
            'merchantStreetAddress',
            'merchantCity',
            'merchantState',
            'merchantPostalCode',
            'merchantCountryCode',
            'merchantPhoneNumber',
            'merchantUrl',
            'visaMerchantId',
            'visaStoreId',
            'businessRegistrationId',
            'acquirerCardAcceptorId',
            'acquiringBin'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)


class TestMerchantSearchOptions(unittest.TestCase):

    def test_attributes(self):

        params = {
            'max_records': '123',
            'match_indicators': '123',
            'match_score': '123',
        }

        data = MerchantSearch.MerchantSearchOptions(**params)

        attrs = [
            'maxRecords',
            'matchIndicators',
            'matchScore'
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)

