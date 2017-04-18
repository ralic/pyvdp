from .test_abstract_inquiry_model import (TestAbstractInquiryModel,
                                          TestAbstractRequestData,
                                          TestAbstractWsRequestHeaderV2,
                                          TestAbstractSort,
                                          TestAbstractRange,
                                          TestAbstractFilter,
                                          TestAbstractOptions,
                                          TestAbstractGeocodes,
                                          TestAbstractLocation)

from pyvdp.globalatmlocator.localatms.models import GeocodesInquiryModel


class TestGeocodesInquiry(TestAbstractInquiryModel):
    def test_attributes(self):
        model = GeocodesInquiryModel(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestGeocodesInquiryWsRequestHeaderV2(TestAbstractWsRequestHeaderV2):
    def test_attributes(self):
        model = GeocodesInquiryModel.WsRequestHeaderV2(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)


class TestGeocodesRequestData(TestAbstractRequestData):
    def test_attributes(self):
        model = GeocodesInquiryModel.RequestData(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestGeocodesLocation(TestAbstractLocation):
    def test_attributes(self):
        model = GeocodesInquiryModel.RequestData.Location(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestGeocodesGeocodes(TestAbstractGeocodes):
    def test_attributes(self):
        model = GeocodesInquiryModel.RequestData.Location.Geocodes(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestGeocodesOptions(TestAbstractOptions):
    def test_attributes(self):
        model = GeocodesInquiryModel.RequestData.Options(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestGeocodesRange(TestAbstractRange):
    def test_attributes(self):
        model = GeocodesInquiryModel.RequestData.Options.Range(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestGeocodesSort(TestAbstractSort):
    def test_attributes(self):
        model = GeocodesInquiryModel.RequestData.Options.Sort(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
