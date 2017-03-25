======================================================
PyVDP - Visa Developer Program APIs, wrapped in Python
======================================================

..  note::

    https://www.github.com/ppokrovsky/pyvdp

..  toctree::
    :maxdepth: 1
    :caption: Contents:

    api
    glossary

+++++++++++++
Configuration
+++++++++++++

Configuration parameters are set in configuration.ini file, located within visa package.

----
VISA
----

..  glossary::

    url
        Visa API Endpoint URL

    username
        VDP application username

    password
        VDP application password

    version
        API version (may be overridden)

    cert
        Relative path to certificate file

    key
        Relative path to keyfile

    enable_exceptions
        If False, a response will be returned as dictionary (see below), otherwise an exception will be raised if
        HTTP response code is other than 200 (Success)

        **Response example:**
            ..  code-block:: python

                    result = {
                        'request': {
                            'endpoint': self.api_endpoint,
                            'http_verb': self.http_verb,
                            'data': self.data,
                        },
                        'response': {
                            'code': code,
                            'message': result.json(),
                        }
                    }

--------
ACQUIRER
--------

..  glossary::

    acquiring_bin
        BIN of Acquirer

    acquirer_country_code
        Acquirer country code

-------------
FUNDSTRANSFER
-------------

..  glossary::

    business_application_id
        Business Application Identifier for FundsTransfer methods (AA)

-----
MVISA
-----

..  glossary::

    cashin_business_application_id
        Business application identifier for CashIn methods (CI)

    cashout_business_application_id
        Business application identifier for CashOut methods (CO)

    mp_business_application_id
        Business application identifier for MerchatnPurchase methods (MP)

+++++++++++++++++++++++++
configuration.ini example
+++++++++++++++++++++++++

    ..  code-block:: ini

        [VISA]
        url = https://sandbox.api.visa.com/
        username = somerandomstring
        password = somerandompassword
        version = v1
        cert = private/cert.pem
        key = private/key.pem
        enable_exceptions = True

        [ACQUIRER]
        acquiring_bin = 400171
        acquirer_country_code = 643

        # Resource-specific configuration

        [FUNDSTRANSFER]
        # FundsTransfer BAI
        business_application_id = AA

        [MVISA]
        # mVISA cashin methods
        cashin_business_application_id = CI
        # mVISA cashout methods
        cashout_business_application_id = CO
        # mVISA merchant purchase methods
        mp_business_application_id = MP
