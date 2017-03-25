import unittest

from pyvdp.visadirect.data import CardAcceptor


class TestCardAcceptor(unittest.TestCase):

    def test_hasName(self):
        t = CardAcceptor(name='test')
        self.assertTrue(hasattr(t, 'name'))

    def test_hasTerminalId(self):
        t = CardAcceptor(terminal_id='test')
        self.assertTrue(hasattr(t, 'terminalId'))

    def test_hasIdCode(self):
        t = CardAcceptor(id_code='test')
        self.assertTrue(hasattr(t, 'idCode'))

    def test_hasAddress(self):
        t = CardAcceptor(address={'country': 'RU'})
        self.assertTrue(hasattr(t, 'address'))


class TestCardAcceptorAddress(unittest.TestCase):

    def setUp(self):
        self.ca = CardAcceptor

    def test_hasCountry(self):
        a = self.ca.CardAcceptorAddress(country='RU')
        self.assertTrue(hasattr(a, 'country'))

    def test_hasZipCode(self):
        a = self.ca.CardAcceptorAddress(zip_code='123')
        self.assertTrue(hasattr(a, 'zipCode'))

    def test_hasState(self):
        a = self.ca.CardAcceptorAddress(state='CA')
        self.assertTrue(hasattr(a, 'state'))

    def test_hasCity(self):
        a = self.ca.CardAcceptorAddress(city='SFO')
        self.assertTrue(hasattr(a, 'city'))

