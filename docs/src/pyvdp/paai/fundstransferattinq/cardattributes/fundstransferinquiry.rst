======================
Funds Transfer Inquiry
======================

..  seealso::

    https://developer.visa.com/products/paai/reference#paai__paai

The Funds Transfer Attributes Inquiry API is often used with a funds transfer to/from a Visa payment account to
determine key characteristics of a recipient card before initiating the transfer like country, card-type, block status,
etc. The API has been enhanced to query :ref:`pull_funds_transaction` and :ref:`push_funds_transaction` eligibility
(both domestic and cross-border) for multiple U.S. debit networks.

Funds Transfer Inquiry API retrieves the attributes, which determine the key characteristics of a recipient payment
account before initiating a funds transfer, by providing the Primary Account Number (PAN)

+++++
Usage
+++++

..  automodule:: pyvdp.paai.fundstransferattinq.cardattributes.fundstransferinquiry
    :members:

++++++++++++
Data Objects
++++++++++++

--------------------
FundsTransferInquiry
--------------------

..  autoclass:: pyvdp.paai.fundstransferattinq.cardattributes.FundsTransferInquiry
    :members:

..  _PullFundsTransactions (AFT):

