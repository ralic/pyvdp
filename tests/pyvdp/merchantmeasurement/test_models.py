import unittest

from pyvdp.merchantmeasurement import MerchantBenchmarkModel


class TestRetrieveMetricsPayloadModel(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'requestHeader': object,
            'requestData': object
        }

        model = MerchantBenchmarkModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestRequestHeader(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'messageDateTime': str,
            'requestMessageId': str
        }

        model = MerchantBenchmarkModel.RequestHeader(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)


class TestRequestData(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'merchantCategoryCodes': list,
            'merchantCategoryGroupsCodes': list,
            'zipList': list,
            'msaList': list,
            'countryList': list,
            'monthList': list,
            'groupList': list,
            'cardPresentIndicator': '2'
        }

        model = MerchantBenchmarkModel.RequestData(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
