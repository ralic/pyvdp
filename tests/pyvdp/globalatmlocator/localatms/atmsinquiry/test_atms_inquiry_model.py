from .test_abstract_inquiry_model import (TestAbstractInquiryModel,
                                          TestAbstractRequestData,
                                          TestAbstractWsRequestHeaderV2,
                                          TestAbstractSort,
                                          TestAbstractFilter,
                                          TestAbstractOptions,
                                          TestAbstractGeocodes,
                                          TestAbstractLocation,
                                          TestAbstractRange)

from pyvdp.globalatmlocator.localatms.models import AtmsInquiryModel


class TestAtmsInquiryModel(TestAbstractInquiryModel):
    def test_attributes(self):
        model = AtmsInquiryModel(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestAtmsInquiryModelRequestData(TestAbstractRequestData):
    def test_attributes(self):
        model = AtmsInquiryModel.RequestData(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestAtmsInquiryModelWsRequestHeaderV2(TestAbstractWsRequestHeaderV2):
    def test_attributes(self):
        model = AtmsInquiryModel.WsRequestHeaderV2(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)


class TestAtmsInquiryModelLocation(TestAbstractLocation):
    def test_attributes(self):
        model = AtmsInquiryModel.RequestData.Location(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestAtmsInquiryModelGeocodes(TestAbstractGeocodes):
    def test_attributes(self):
        model = AtmsInquiryModel.RequestData.Location.Geocodes(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestAtmsInquiryModelOptions(TestAbstractOptions):
    def test_attributes(self):
        model = AtmsInquiryModel.RequestData.Options(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestAtmsInquiryModelRange(TestAbstractRange):
    def test_attributes(self):
        model = AtmsInquiryModel.RequestData.Options.Range(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestAtmsInquiryModelSort(TestAbstractSort):
    def test_attributes(self):
        model = AtmsInquiryModel.RequestData.Options.Sort(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
