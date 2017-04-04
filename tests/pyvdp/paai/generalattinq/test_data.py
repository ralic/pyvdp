import unittest

from pyvdp.paai.generalattinq.cardattributes import GeneralInquiryData


class TestGeneralInquiryData(unittest.TestCase):

    def test_attributes(self):

        params = {
            'pan': '1234567812345678',
        }

        data = GeneralInquiryData(**params)

        attrs = [
            'primaryAccountNumber',
        ]

        for attr in attrs:
            self.assertTrue(hasattr(data, attr), 'missing %s attribute' % attr)
