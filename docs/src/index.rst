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
Introduction
++++++++++++

PyVDP is a collection of wrappers for Visa Developer Program, that implements various APIs for payment card processing.
The library implements following major components:
* Models
* Dispatchers
* Actions

General interaction with VDP is implemented with following flow:
1. User instantiates a data object (Model), that will be submitted to VISA
2. Model is passed to Dispatcher, that instantaites a connection to VISA
3. Send action is called on Dispatcher, that submits data to VISA.
4. Result is returned to user.

------
Models
------

Models are simple Python objects, representing data, submitted to VISA. Models attributes (properties) are matched to
actual attributes names, that are understood by VISA.

-----------
Dispatchers
-----------

Dispatcher are python classes, that implement logic, related to connection to various APIs, such as API enpoints,
authentication methods etc.

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
    loglevel = DEBUG
    logfile = pyvdp.log


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
* *loglevel* - **Optional**. Loglevel. See `Logging`_ section below
* *logfile* - **Optional**. Path and name of the logfile. See `Logging`_ section below.

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

+++++++
Logging
+++++++

PyVDP provides some logging capabilities, that may be used to log errors or debug operations. Logging is implemented
via standard Python `logging` library and is configured in **[VISA]** section of configuration file.

..  code-block:: ini

    loglevel = DEBUG
    logfile = pyvdp.log

..  glossary::

    loglevel
        Logging level. Possible values: DEBUG, INFO, WARNING, ERROR, CRITICAL. Default is **ERROR**.

    logfile
        Logfile path and name. Path is relative to directory, where config file is stored. Default is **pyvdp.log**
        located in the same directory, where configuration file resides.

In order to provide consistency between requests and replies, every session with VDP is identified in logfile with UUID.
This way you can easily correlate records and trace requests flow for information or debug.

Default loglevel is **ERROR**. With this loglevel, exceptions will be logged, including request method + url and
response HTTP code. **INFO** loglevel will log the same but for successful requests. Finally, **DEBUG** level will
log everything, including request and response headers and payloads.

..  warning::

    **DEBUG** should not be used in production environment because logs may (and will) contain sensitive data, such
    as VDP authentication credentials and card details.

