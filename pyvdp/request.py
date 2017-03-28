import hashlib
import hmac
import jsonpickle
import os
import random
import requests
import string
import time

from pyvdp.exceptions import (VisaAccessDeniedError, VisaDuplicateTransactionError, VisaGeneralError,
                              VisaMessageValidationError, VisaNotFoundError, VisaTimeoutError, VisaUnauthenticatedError)

from pyvdp import configuration


class VisaRequest(object):
    """Constructs a request to Visa API to provided resource, method and http verb.

    After request is constructed, it shall be submitted with `send()` method, which returns a `requests.Response`
    object.

    This class is not assumed to be instantiated on its own (consider it abstract). Instead, every VISA API
    implementation must provide its own request class, inheriting from VisaRequest and providing a
    corresponding VISA API resource name as a `resource` argument value (see visa.visadirect.request as an example)

    :param str resource: **Required**. VISA API resource name
    :param str api: **Required**. VISA API api name
    :param str method: **Required**. VISA API endpoint method
    :param str http_verb: **Required**. VISA API HTTP verb (GET, POST, PUT)
    :param str query_string: **Conditional**. Query string to append to API endpoint
    :param object data: **Conditional**. Data payload for POST requests, VisaTransacton object
    :param str auth_method: **Conditional**. Authentication method. Possible values are:
            **ssl** - for certificate-based authentication (default) or **token** - for x-pay-token authentication
    :param dict headers: **Optional**. Additional headers.
    """

    # VDP HTTP codes mapped to exceptions
    # (kudos to http://codereview.stackexchange.com/questions/155350/pyvdp-python-library-for-visa-developer-program)
    ERROR_CODES = {
        202: VisaTimeoutError,
        303: VisaDuplicateTransactionError,
        400: VisaMessageValidationError,
        401: VisaUnauthenticatedError,
        403: VisaAccessDeniedError,
        404: VisaNotFoundError
    }

    def __init__(self,
                 resource,
                 api,
                 method,
                 http_verb,
                 query_string='',
                 data='',
                 auth_method='ssl',
                 headers=None,
                 config=None):

        if config:
            self._config = self._get_config_from_dict(config)
        else:
            config_path = os.getenv('PYVDP_CONFIG', os.path.join(os.path.dirname(__file__), 'configuration.ini'))
            self._config = configuration.get_config(config_path)

        # API path structure: https://domain/resource/api/version/method
        # eg https://sandbox.api.visa.com/cybersource/payments/v1/authorizations
        self.resource = resource
        self.api = api
        self.method = method
        self.api_endpoint = self._config['url'] \
                            + "/" \
                            + self.resource \
                            + "/" \
                            + self.api \
                            + "/" \
                            + self._config['version'] \
                            + "/" \
                            + self.method

        self.http_verb = http_verb

        if query_string:
            self.query_string = query_string
        else:
            self.query_string = ''

        if data:
            self.data = self._obj_to_json(data)
        else:
            self.data = ''

        # Headers setup
        # FIXME: Hardcoded request/response in json format
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Client-Transaction-ID': self._get_x_client_transaction_id()
        }
        if headers:
            self.headers.update(headers)

        # Session initialization
        self.session = requests.Session()

        # Authentication setup
        if auth_method == 'ssl':
            # certificate-based authentication
            self.session.cert = (self._config['cert'], self._config['key'])
        elif auth_method == 'token':
            # x-pay-token authentication
            x_pay_token = self._get_x_pay_token()
            token_header = {'X-PAY-TOKEN': x_pay_token}
            self.headers.update(token_header)
        else:
            raise AttributeError("auth_method argument value must be either 'ssl' or 'token' ('%s' passed)" % auth_method)

    def send(self):
        """Submits a data object or query string id to VISA using `self.api_endpoint` field and corresponding http verb.

        :return: result: Resulting dictionary.
        """

        url = self.api_endpoint + self.query_string

        # Using requests.Session and requests.PreparedRequest to construct request to VDP
        req = requests.Request(
            method=self.http_verb,
            url=url,
            data=self.data,
            auth=(self._config['username'], self._config['password']),
            headers=self.headers
        )
        prepped_req = req.prepare()
        result = self.session.send(prepped_req)

        return self._response(result)

    def _response(self, result):
        """Processes a response from Visa Direct API.

        Depending on HTTP code in response, either returns a result or raises corresponding app-level exception.

        :param requests.Response result: Required. Response from VISA
        :return: dict result: Resulting dictionary
        :raises: VisaTimeoutError, VisaDuplicateTransactionError, VisaMessageValidationError, VisaUnauthenticatedError,
                VisaAccessDeniedError, VisaNotFoundError, VisaGeneralError
        """

        code = result.status_code

        if not self._config['debug']:
            if code == 200:
                result = {
                    'code': code,
                    'endpoint': self.api_endpoint,
                    'http_verb': self.http_verb,
                    'message': result.json()
                }
            else:
                raise self.ERROR_CODES.get(code, VisaGeneralError)(result=result)
        else:
            if code == 202:
                message = result.content
            else:
                message = result.json()

            result = {
                'request': {
                    'endpoint': self.api_endpoint,
                    'http_verb': self.http_verb,
                    'data': self.data,
                },
                'response': {
                    'code': code,
                    'headers': result.headers,
                    'message': message,
                }
            }

        return result

    @staticmethod
    def _get_x_client_transaction_id():
        """Generates random 12-digits value used for X-Client-Transaction-ID header.

        :return: Value for X-Client-Transaction-ID header
        """
        return ''.join(random.choice(string.digits) for _ in range(12))

    def _get_x_pay_token(self):
        """Generates payload for X-PAY-TOKEN header (token-based authentication)
        https://developer.visa.com/guides/vdpguide#two_way_ssl

        :return: X-PAY-TOKEN value
        """
        ts = str(int(time.time()))
        key = self._config['shared_secret']
        resource_path = self.api + '/' + self._config['version'] + '/' + self.method
        message = ts + resource_path + self.query_string + self.data

        digest = hmac.new(str.encode(key), msg=str.encode(message), digestmod=hashlib.sha256).hexdigest()

        return "xv2:" + ts + ":" + digest

    @staticmethod
    def _obj_to_json(data):
        """Serializes Python object to json

        :param object data: Python object
        :return: JSON string
        """
        json = jsonpickle.encode(data, unpicklable=False)
        return json

    @staticmethod
    def _get_config_from_dict(config):
        return config
