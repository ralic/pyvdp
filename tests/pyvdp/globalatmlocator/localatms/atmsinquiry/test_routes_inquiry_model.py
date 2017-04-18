import unittest
from .test_abstract_inquiry_model import (TestAbstractInquiryModel,
                                          TestAbstractRequestData,
                                          TestAbstractWsRequestHeaderV2,
                                          TestAbstractSort,
                                          TestAbstractFilter,
                                          TestAbstractOptions,
                                          TestAbstractGeocodes,
                                          TestAbstractLocation)

from pyvdp.globalatmlocator.localatms.models import RoutesInquiryModel


class TestRoutesInquiryModel(TestAbstractInquiryModel):

    def test_attributes(self):
        model = RoutesInquiryModel(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestRoutesInquiryModelWsRequestHeaderV2(TestAbstractWsRequestHeaderV2):
    def test_attributes(self):
        model = RoutesInquiryModel.WsRequestHeaderV2(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)


class TestRoutesInquiryModelRequestData(TestAbstractRequestData):

    def setUp(self):
        self.attrs = {
            'doNotLocateOnRestrictedElements': bool,
            'features': [object],
            'travelMode': object,
            'type': str
        }

    def test_attributes(self):
        model = RoutesInquiryModel.RequestData(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestRoutesInquiryGeometry(unittest.TestCase):

    def setUp(self):
        self. attrs = {
            'x': float,
            'y': float,
        }

    def test_attributes(self):
        model = RoutesInquiryModel.RequestData.Geometry(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestRoutesInquiryTravelMode(unittest.TestCase):

    def setUp(self):
        self.attrs = {
            'type': str
        }

    def test_attributes(self):
        model = RoutesInquiryModel.RequestData.TravelMode(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
