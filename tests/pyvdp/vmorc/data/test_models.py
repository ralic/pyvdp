import unittest

from pyvdp.vmorc.data import RefModel, MerchantModel, MerchantAddressModel


class TestMerchantAddressModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'merchantIds': str,
            'start_index': str
        }

        model = MerchantAddressModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestMerchantModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'start_index': int,
            'program': str
        }

        model = MerchantModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestRefModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'resources': str,
            'languages': str,
            'programIds': str
        }

        model = RefModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
