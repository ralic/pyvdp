import unittest

from pyvdp.vmorc.offers import ByFilterModel, AllModel, ByContentIdModel, ByOfferIdModel


class TestByOfferIdModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'offerid': str,
            'updatefrom': str,
            'updateto': str,
            'start_index': int,
            'max_offers': int
        }

        model = ByOfferIdModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestByContentIdModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'contentid': str,
            'updatefrom': str,
            'updateto': str,
            'start_index': int,
            'max_offers': int
        }

        model = ByContentIdModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestByFilterModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'business_segment': str,
            'card_payment_type': str,
            'card_product': str,
            'category': str,
            'subcategory': str,
            'merchant': str,
            'program': str,
            'promotion_channel': str,
            'promoting_region': str,
            'promoting_country': str,
            'redemption_region': str,
            'redemption_country': str,
            'merchant_region': str,
            'merchant_country': str,
            'language': str,
            'expired': str,
            'validfrom': str,
            'validto': str,
            'promotedfrom': str,
            'promotedto': str,
            'updatefrom': str,
            'updateto': str,
            'featured': bool,
            'start_index': int,
            'max_offers': int,
            'bins': str,
            'rpins': str,
            'bins_to_rpins': str,
            'accountranges': str,
            'accountranges_to_rpins': str,
            'pans': str,
            'non_cardAttribute': bool,
            'origin': float,
            'radius': float,
            'unit': str,
            'non_geo': bool
        }

        model = ByFilterModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)


class TestAllModel(unittest.TestCase):

    def test_attributes(self):
        attrs = {
            'start_index': int,
            'max_offers': int
        }

        model = AllModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
