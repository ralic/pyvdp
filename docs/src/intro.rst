============
Introduction
============

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
