import hashlib
import hmac
import jsonpickle
import time
import unittest
import requests_mock

from pyvdp.exceptions import (VisaTimeoutError,
                              VisaMessageValidationError,
                              VisaDuplicateTransactionError,
                              VisaUnauthenticatedError,
                              VisaAccessDeniedError,
                              VisaNotFoundError,
                              VisaGeneralError)
from pyvdp.request import VisaRequest
from pyvdp.visadirect.data import VisaDirectTransaction


@requests_mock.Mocker()
class TestVisaRequest(unittest.TestCase):
    def setUp(self):
        self.t = VisaDirectTransaction(stan='123456')

        self.vr = VisaRequest(resource='', api='', method='', http_verb='POST', data=self.t)
        self.vr.user_id = 'testuser'
        self.vr.password = 'testpassword'
        self.vr.cert = 'testcert.pem'
        self.vr.key = 'testkey.pem'
        self.vr.shared_secret = 'secret'
        self.vr.api_endpoint = 'http://localhost'
        self.vr.enable_exceptions = True

    def test_sendReturnsDictionaryOnHTTP200(self, m):
        message = "{\"text\": \"this is a test\"}"
        m.register_uri('POST', self.vr.api_endpoint, text=message)
        result = self.vr.send()
        expect = {
            'code': 200,
            'endpoint': 'http://localhost',
            'http_verb': 'POST',
            'message': {'text': 'this is a test'}
        }
        self.assertDictEqual(result, expect)

    def test_sendRaisesVisaTimeoutErrorOnHTTP202(self, m):
        m.register_uri('POST', self.vr.api_endpoint, status_code=202)
        with self.assertRaises(VisaTimeoutError):
            self.vr.send()

    def test_sendRaisesVisaDuplicateTransactionErrorOnHTTP303(self, m):
        m.register_uri('POST', self.vr.api_endpoint, status_code=303)
        with self.assertRaises(VisaDuplicateTransactionError):
            self.vr.send()

    def test_sendRaisesVisaMessageValidationErrorOnHTTP400(self, m):
        m.register_uri('POST', self.vr.api_endpoint, status_code=400)
        with self.assertRaises(VisaMessageValidationError):
            self.vr.send()

    def test_sendRaisesVisaUnauthenticatedErrorOnHTTP401(self, m):
        m.register_uri('POST', self.vr.api_endpoint, status_code=401)
        with self.assertRaises(VisaUnauthenticatedError):
            self.vr.send()

    def test_sendRaisesVisaAccessDeniedErrorOnHTTP403(self, m):
        m.register_uri('POST', self.vr.api_endpoint, status_code=403)
        with self.assertRaises(VisaAccessDeniedError):
            self.vr.send()

    def test_sendRaisesVisaNotFoundErrorOnHTTP404(self, m):
        m.register_uri('POST', self.vr.api_endpoint, status_code=404)
        with self.assertRaises(VisaNotFoundError):
            self.vr.send()

    def test_sendRaisesVisaGeneralErrorOnHTTP500(self, m):
        m.register_uri('POST', self.vr.api_endpoint, status_code=500)
        with self.assertRaises(VisaGeneralError):
            self.vr.send()

    def test_getXPayTokenGeneratesToken(self, m):
        ts = str(int(time.time()))
        resource_path = self.vr.api + '/' + self.vr.version + '/' + self.vr.method
        message = ts + resource_path + self.vr.query_string + self.vr.data
        digest = hmac.new(str.encode(self.vr.shared_secret), msg=str.encode(message), digestmod=hashlib.sha256).hexdigest()
        token = "xv2:" + ts + ":" + digest

        self.assertEqual(token, self.vr._get_x_pay_token(), "x-pay-token does not match")

    def test_objToJsonSerializesObjectToJSON(self, m):
        obj = self.t
        json = jsonpickle.encode(obj, unpicklable=False)
        self.assertEqual(json, self.vr._obj_to_json(obj), 'json strings do not match')