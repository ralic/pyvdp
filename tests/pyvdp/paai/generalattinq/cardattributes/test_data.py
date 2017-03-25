import unittest

from pyvdp.paai.generalattinq.cardattributes.data import GeneralInquiryData


class TestGeneralInquiryData(unittest.TestCase):

    def setUp(self):
        self.gid = GeneralInquiryData(pan='12345678')

    def test_hasPrimaryAccountNumber(self):
        self.assertTrue(hasattr(self.gid, 'primaryAccountNumber'), 'missing pan')
