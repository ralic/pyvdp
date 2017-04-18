from .test_abstract_inquiry_model import (TestAbstractLocation,
                                          TestAbstractGeocodes,
                                          TestAbstractOptions,
                                          TestAbstractFilter,
                                          TestAbstractSort,
                                          TestAbstractWsRequestHeaderV2,
                                          TestAbstractRequestData,
                                          TestAbstractInquiryModel)

from pyvdp.globalatmlocator.localatms.models import TotalsInquiryModel


class TestTotalsInquiryModel(TestAbstractInquiryModel):
    def test_attributes(self):
        model = TotalsInquiryModel(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestTotalsInquiryModelRequestData(TestAbstractRequestData):
    def test_attributes(self):
        model = TotalsInquiryModel.RequestData(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestTotalsInquiryModelWsRequestHeaderV2(TestAbstractWsRequestHeaderV2):
    def test_attributes(self):
        model = TotalsInquiryModel.WsRequestHeaderV2(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)


class TestTotalsInquiryModelLocation(TestAbstractLocation):
    def test_attributes(self):
        model = TotalsInquiryModel.RequestData.Location(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestTotalsInquiryModelGeocodes(TestAbstractGeocodes):
    def test_attributes(self):
        model = TotalsInquiryModel.RequestData.Location.Geocodes(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestTotalsInquiryModelOptions(TestAbstractOptions):
    def test_attributes(self):
        model = TotalsInquiryModel.RequestData.Options(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestTotalsInquiryModelSort(TestAbstractSort):
    def test_attributes(self):
        model = TotalsInquiryModel.RequestData.Options.Sort(**self.attrs)
        for attr, value in self.attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
