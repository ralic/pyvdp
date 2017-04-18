import unittest

from pyvdp.globalatmlocator.localatms.models import AbstractInquiryModel


class TestAbstractInquiryModel(unittest.TestCase):
    def setUp(self):
        self.attrs = {
            'wsRequestHeaderV2': object,
            'requestData': object
        }


class TestAbstractRequestData(unittest.TestCase):
    def setUp(self):
        self.attrs = {
            'culture': str,
            'distance': int,
            'distanceUnit': str,
            'location': object,
            'metaDataOptions': int,
            'options': object
        }


class TestAbstractWsRequestHeaderV2(unittest.TestCase):
    def setUp(self):
        self.attrs = {
            'applicationId': str,
            'correlationId': int,
            'requestMessageId': str,
            'requestTs': object,
            'userBid': int,
            'userId': object
        }


class TestAbstractLocation(unittest.TestCase):
    def setUp(self):
        self.attrs = {
            'placeName': str,
            'geocodes': object
        }


class TestAbstractGeocodes(unittest.TestCase):
    def setUp(self):
        self.attrs = {
            'latitude': int,
            'longitude': int
        }


class TestAbstractOptions(unittest.TestCase):
    def setUp(self):
        self.attrs = {
            'range': object,
            'sort': object,
            'operationName': object,
            'findFilters': [object],
            'useFirstAmbiguous': bool
        }


class TestAbstractRange(unittest.TestCase):
    def setUp(self):
        self.attrs = {
            'count': int,
            'start': int
        }


class TestAbstractFilter(unittest.TestCase):
    def setUp(self):
        self.attrs = {
            'filterName': str,
            'filterValue': str,
        }


class TestAbstractSort(unittest.TestCase):
    def setUp(self):
        self.attrs = {
            'primary': str,
            'direction': str,
            'secondary': str
        }
