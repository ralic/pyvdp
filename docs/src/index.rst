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
5. If something went wrong, exception is raised.


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


+++++++++++
Data Models
+++++++++++

Models are simple Python objects, representing data, submitted to VISA. Models attributes (properties) are matched to
actual attributes names, that are understood by VISA.

+++++++++++
Dispatchers
+++++++++++

Dispatcher are python classes, that implement logic, related to connection to various APIs, such as API enpoints,
authentication methods etc.

+++++++
Actions
+++++++

Actions are Python modules (essentially helpers) that implement one of the API methods, introduced by VDP.
E.g. :func:`pyvdp.visadirect.fundstransfer.pullfundstransactions.send()` submits POST request to Visa Direct
FundsTransfer API endpoint.

++++++++++
Exceptions
++++++++++

With any unexpected outcome, a corresponding exception is raised. Generally, any response code from VISA, except
**200 OK** raises corresponding exception, listed in :func:`pyvdp.exceptions` module. Names of such exceptions begin
with *Visa* (e.g. :func:`~pyvdp.exceptions.VisaMessageValidationError` that represents HTTP 400 code).
Internal PyVDP errors are also handled by exceptions. Names of such exceptions start with *Pyvdp*, e.g.
:func:`~pyvdp.configuration.PyvdpConfigurationError`.
