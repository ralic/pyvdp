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

++++++++++++
Installation
++++++++++++

..  code-block:: bash

    $ pip install pyvdp

+++++++++++++
Configuration
+++++++++++++

PyVDP is configured through INI-file. The location of INI-file is defined with environment variable **PYVDP_CONFIG**.
In case **PYVDP_CONFIG** variable is not set, then PyVDP will attempt to search for **configuration.ini** file in module
folder (which is usually located in site-packages/pyvdp).

..  warning::

    Since configuration file contains sensitive data, such as user credentials, the configuration file itself and
    corresponding certificate/keyfiles should be kept safely and ignored by version control.

Here's an example of configuration file:

..  code-block:: ini

    [VISA]
    url = https://sandbox.api.visa.com
    username = myapplicationusername
    password = myapplicationpassword
    version = v1
    cert = cert.pem
    key = key.pem
    shared_secret = secret
    api_key = 12345678ABCDEF
    debug = false

**[VISA]** is a mandatory section, under which configuration parameters are defined.

* *url* - **Required**. API endpoint with or without trailing slash.
* *username* - **Conditional**. Username for authentication. It is generated automatically when you add a
  corresponding API to your app.
* *password* - **Conditional**. Password for authentication. It is generated automatically when you add a
  corresponding API to your app.
* *version* - **Conditional**. Version of API. It may be overridden during Request instantiation.
* *cert* - **Conditional**. Full path to certificate file, relative to a directory, where configuration file is
  located.
* *key* - **Conditional**. Full path to keyfile, relative to a directory, where configuration file is located.
* *shared_secret* - **Conditional**. A shared secret string for token-based APIs.
* *api_key* - **Conditional**. API key for token-based APIs.
* *debug* - **Optional**. true or false. When enabled, returns a response dictionary. When disabled, only 200 codes
  will be returned as a dictionary. Other codes will raise corresponding exceptions. Default false.

++++++++++++++
Authentication
++++++++++++++

VDP supports two methods of authentication:

1. SSL-based
2. Token-based

The actual type of authentication depends on the API. E.g. VisaDirect APIs support SSL-based authentication, while
Microtransactions require token-based authentication.

If your app uses only SSL-based APIs, then you need to provide username,password and certificate/keyfile config
parameters. Correspondingly, if you built something with token-based API, then you need to provide shared_secret and
api_key parameters.

More details regarding VDP authentication are available at VDP portal (see link below).

..  seealso::

    https://developer.visa.com/guides/vdpguide#two_way_ssl
