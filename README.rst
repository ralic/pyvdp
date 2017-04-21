====================================
PyVDP: VISA APIs. Wrapped in Python.
====================================

..  image:: https://travis-ci.org/ppokrovsky/pyvdp.svg?branch=master
    :target: https://travis-ci.org/ppokrovsky/pyvdp

..  image:: https://lima.codeclimate.com/github/ppokrovsky/pyvdp/badges/gpa.svg
    :target: https://lima.codeclimate.com/github/ppokrovsky/pyvdp

..  image:: https://api.codacy.com/project/badge/Grade/5a119e1aafb9480c87736df4d0ab2a24
    :target: https://www.codacy.com/app/ppokrovsky/pyvdp


..  contents::

++++++++
Features
++++++++

* Easy calls to VDP APIs, implemented through functions, named to reflect structure of actual VDP APIs..
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
    * Visa Global AT Locator
    * Merchant Measurement
    * Payment Account Attibutes Inquiry
    * Foreign Exchange Rates
    * Digital Card and Account Services
  * Risk and Fraud
    * Mobile Location Confirmation
    * Payment Account Validation

++++++++++++
Installation
++++++++++++

..  code:: bash

    $ pip install pyvdp

+++++++++++++
Configuration
+++++++++++++

See **Configuration** section in documentation.

+++++++++++
Basic Usage
+++++++++++

Here's an example snippet for Payment Account Validation call:

..  code:: python

    from pyvdp.visadirect import CardAcceptorModel
    from pyvdp.pav import cardvalidation, CardValidationModel

    ca_address_kwargs = {
        "city": "fostr city",
        "country": "PAKISTAN",
        "county": "CA",
        "state": "CA",
        "zipCode": "94404"
    }

    ca_kwargs = {
        "address": CardAcceptorModel.CardAcceptorAddress(**ca_address_kwargs),
        "idCode": "111111",
        "name": "rohan",
        "terminalId": "123"
    }

    avr_kwargs = {
        "postalCode": "T4B 3G5",
        "street": "2881 Main Street Sw"
    }

    data_kwargs = {
        "addressVerificationResults": CardValidationModel.AddressVerificationResults(**avr_kwargs),
        "cardAcceptor": CardAcceptorModel(**ca_kwargs),
        "cardCvv2Value": "672",
        "cardExpiryDate": "2018-06",
        "primaryAccountNumber": "4957030000313108",
        "retrievalReferenceNumber": "015221743720",
        "systemsTraceAuditNumber": "743720"
    }

    data = CardValidationModel(**data_kwargs)
    result = cardvalidation.send(data)
    print(result)

The implementation is straightforward:

1. Build a data object
2. Submit this object to :func:`send` function

Under the hood, data object will be serialized to JSON and submitted to corresponding API endpoint. If returning
HTTP code equals 200, response will contain a JSON string with headers and payload, otherwise an exception will be
raised depending on returned HTTP code value.

+++++++++++++
Documentation
+++++++++++++

A thorough documentation is located in docs/

+++++++++
Questions
+++++++++

Please use the issue tracker to ask questions.

+++++++
License
+++++++

Copyright &copy; 2017 Pavel Pokrovskiy.

MIT licensed.
