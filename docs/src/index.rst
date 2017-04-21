:github_url: https://www.github.com/ppokrovsky/pyvdp

======================================
PyVDP: VISA APIs. Wrapped with Python.
======================================

..  note::

    https://www.github.com/ppokrovsky/pyvdp

..  toctree::
    :maxdepth: 2
    :caption: Contents

    intro
    data_and_analytics/index
    payment_methods/index
    risk_and_fraud/index
    glossary

+++++
About
+++++

**PyVDP** is a collection of Python wrappers for `Visa Developer APIs <https://developer.visa.com>`_ which simplifies
interaction with APIs through provision of straightforward OO-interface for VISA APIs.

**Features:**

* Easy calls to VDP APIs, implemented through functions, named to reflect structure of actual VDP APIs.
* Errors are handled as standard exceptions with meaningful messages.
* OO-interface, data objects are simple Python classes.
* Can be used with any web framework.
* Includes demo Django application, demonstrating basic principles.
* Full support for following APIs:

  * Payment Methods:

    * VisaDirect

  * Data and Analytics:

    * Merchant Search
    * Merchant Locator
    * Visa Global ATM Locator
    * Merchant Measurement
    * Payment Account Attibutes Inquiry
    * Foreign Exchange Rates
    * Digital Card and Account Services

  * Risk and Fraud:

    * Mobile Location Confirmation
    * Payment Account Validation

++++++++++++
Installation
++++++++++++

..  code-block:: bash

    $ pip install pyvdp

+++++++++++++
Configuration
+++++++++++++

..  warning::

    Since configuration file contains sensitive data, such as user credentials, the configuration file itself and
    corresponding certificate/keyfiles should be kept safely and ignored by version control.

..  automodule:: pyvdp.configuration

+++++++
Logging
+++++++

..  warning::

    **DEBUG** should not be used in production environment because logs may (and will) contain sensitive data, such
    as VDP authentication credentials and card details.

..  automodule:: pyvdp.logger
