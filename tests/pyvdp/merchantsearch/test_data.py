import unittest

from pyvdp.merchantsearch.data import MerchantSearchData


class TestMerchantSearchData(unittest.TestCase):

    def setUp(self):
        self.msd = MerchantSearchData(header={},
                                      search_attrs={},
                                      response_attrs=[],
                                      options={})

    def test_hasHeader(self):
        self.assertTrue(hasattr(self.msd, 'header'))

    def test_hasSearchAttrList(self):
        self.assertTrue(hasattr(self.msd, 'searchAttrList'))

    def test_hasResponseAttrList(self):
        self.assertTrue(hasattr(self.msd, 'responseAttrList'))

    def test_hasSearchOptions(self):
        self.assertTrue(hasattr(self.msd, 'searchOptions'))


class TestMerchantSearchHeader(unittest.TestCase):

    def setUp(self):
        self.msh = MerchantSearchData.MerchantSearchHeader()

    def test_hasMessageDateTime(self):
        self.assertTrue(hasattr(self.msh, 'messageDateTime'))

    def test_hasRequestMessageId(self):
        self.assertTrue(hasattr(self.msh, 'requestMessageId'))

    def test_hasStartIndex(self):
        self.assertTrue(hasattr(self.msh, 'startIndex'))


class TestMerchantSearchAttrList(unittest.TestCase):

    def setUp(self):
        attrs = {
            'merchant_name': 'cmu edctn materials cntr',
            'merchant_street_address': '802 industrial dr',
            'merchant_city': 'Mount Pleasant',
            'merchant_state': 'MI',
            'merchant_postal_code': '48858',
            'merchant_country_code': 840,
            'merchant_phone_number': 19897747123,
            'merchant_url': 'https://www.google.com',
            'visa_merchant_id': '12345',
            'visa_store_id': '12345',
            'business_registration_id': '386004447',
            'acquirer_card_acceptor_id': '424295031886',
            'acquiring_bin': '476197',
        }
        self.msal = MerchantSearchData.MerchantSearchAttrList(**attrs)

    def test_hasMerchantName(self):
        self.assertTrue(hasattr(self.msal, 'merchantName'))

    def test_hasMerchantStreetAddress(self):
        self.assertTrue(hasattr(self.msal, 'merchantStreetAddress'))

    def test_hasMerchantCity(self):
        self.assertTrue(hasattr(self.msal, 'merchantCity'))

    def test_hasMerchantState(self):
        self.assertTrue(hasattr(self.msal, 'merchantState'))

    def test_hasMerchantPostalCode(self):
        self.assertTrue(hasattr(self.msal, 'merchantPostalCode'))

    def test_hasMerchantCountryCode(self):
        self.assertTrue(hasattr(self.msal, 'merchantCountryCode'))

    def test_hasMerchantPhoneNumber(self):
        self.assertTrue(hasattr(self.msal, 'merchantPhoneNumber'))

    def test_hasMerchantUrl(self):
        self.assertTrue(hasattr(self.msal, 'merchantUrl'))

    def test_hasVisaMerchantId(self):
        self.assertTrue(hasattr(self.msal, 'visaMerchantId'))

    def test_hasVisaStoreId(self):
        self.assertTrue(hasattr(self.msal, 'visaStoreId'))

    def test_hasBusinessRegistrationId(self):
        self.assertTrue(hasattr(self.msal, 'businessRegistrationId'))

    def test_hasAcquirerCardAcceptorId(self):
        self.assertTrue(hasattr(self.msal, 'acquirerCardAcceptorId'))

    def test_hasAcquiringBin(self):
        self.assertTrue(hasattr(self.msal, 'acquiringBin'))


class TestMerchantSearchOptions(unittest.TestCase):

    def test_hasMaxRecords(self):
        mso = MerchantSearchData.MerchantSearchOptions(max_records=1)
        self.assertTrue(hasattr(mso, 'maxRecords'))

    def test_hasMatchIndicators(self):
        mso = MerchantSearchData.MerchantSearchOptions(match_indicators=True)
        self.assertTrue(hasattr(mso, 'matchIndicators'))

    def test_hasMatchScore(self):
        mso = MerchantSearchData.MerchantSearchOptions(match_score=True)
        self.assertTrue(hasattr(mso, 'matchScore'))

    def test_hasProximity(self):
        mso = MerchantSearchData.MerchantSearchOptions(proximity=['merchantName'])
        self.assertTrue(hasattr(mso, 'proximity'))

    def test_hasWildcards(self):
        mso = MerchantSearchData.MerchantSearchOptions(wildcards=['*erchantNa*'])
        self.assertTrue(hasattr(mso, 'wildCards'))
