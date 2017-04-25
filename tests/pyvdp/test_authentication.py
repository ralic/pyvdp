import hashlib
import hmac
import jsonpickle
import time
import unittest

from pyvdp.authentication import TokenAuth
from pyvdp.visadirect import VisaDirectTransactionModel


class TestTokenAuth(unittest.TestCase):
    def setUp(self):
        kwargs = {
            'systemsTraceAuditNumber': 123456
        }
        self._config = {
            'api_key': 'api_key',
            'shared_secret': 'secret'
        }
        self._model = VisaDirectTransactionModel(**kwargs)
        self._url = 'http://localhost'
        self._api = 'testapi'
        self._version = 'v1'
        self._method = 'testmethod'
        self._query_string = "key1=val1&key2=val2"
        self._data = jsonpickle.encode(self._model, unpicklable=False)

    def test_x_pay_token(self):
        token_kwargs = {
            'url': self._url,
            'api': self._api,
            'version': self._version,
            'method': self._method,
            'data': self._data,
            'query_string': self._query_string
        }

        sample_token = self._get_sample_token()

        klass = TokenAuth(self._config, **token_kwargs)
        generated_token = klass._x_pay_token

        self.assertEqual(sample_token, generated_token, "sample token does not match generated token")

    def _get_sample_token(self):
        ts = str(int(time.time()))
        resource_path = "%s/%s/%s/%s" % (self._url, self._api, self._version, self._method)
        query_string = "?apikey=%s&%s" % (self._config['api_key'], self._query_string)

        message = "%s%s%s%s" % (ts, resource_path, query_string, self._data)
        digest = hmac.new(str.encode(self._config['shared_secret']),
                          msg=str.encode(message),
                          digestmod=hashlib.sha256).hexdigest()
        return "xv2:%s:%s" % (ts, digest)
