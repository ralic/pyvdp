import unittest

from pyvdp.paai.generalattinq.cardattributes import GeneralInquiryModel


class TestGeneralInquiryModel(unittest.TestCase):

    def test_attributes(self):

        attrs = {
            'primaryAccountNumber': '1234567812345678',
        }

        model = GeneralInquiryModel(**attrs)

        for attr, value in attrs.items():
            self.assertTrue(hasattr(model, attr), 'missing %s attribute' % attr)
            self.assertEqual(model.__getattribute__(attr), value)
