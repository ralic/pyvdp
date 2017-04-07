========================
VisaDirect FundsTransfer
========================

.. seealso::

    https://developer.visa.com/products/visa_direct/reference#visa_direct__funds_transfer

+++++
Usage
+++++

A collection of functional call for VisaDirect FundsTransfer APIs, including:

* PullFundsTransactions (GET, POST)
* MultiPullFundsTransactions (GET, POST)
* PushFundsTransactions (GET, POST)
* MultiPushFundsTransactions (GET, POST)
* ReverseFundsTransactions (GET, POST)
* MultiReverseFundsTransactions (GET, POST)

---------
PullFunds
---------

.. automodule:: pyvdp.visadirect.fundstransfer.pullfunds
   :members:

---------
PushFunds
---------

.. automodule:: pyvdp.visadirect.fundstransfer.pushfunds
   :members:

------------
ReverseFunds
------------

.. automodule:: pyvdp.visadirect.fundstransfer.reversefunds
   :members:

++++++++++++
Data objects
++++++++++++

..  _pull_funds_transaction:

-------------------------
PullFundsTransactionModel
-------------------------

.. autoclass:: pyvdp.visadirect.fundstransfer.PullFundsTransactionModel
   :members:

.. autoclass:: pyvdp.visadirect.fundstransfer.MultiPullFundsTransactionModel
   :members:

..  _push_funds_transaction:

-------------------------
PushFundsTransactionModel
-------------------------

.. autoclass:: pyvdp.visadirect.fundstransfer.PushFundsTransactionModel
   :members:

.. autoclass:: pyvdp.visadirect.fundstransfer.MultiPushFundsTransactionModel
   :members:

----------------------------
ReverseFundsTransactionModel
----------------------------

.. autoclass:: pyvdp.visadirect.fundstransfer.ReverseFundsTransactionModel
   :members:

.. autoclass:: pyvdp.visadirect.fundstransfer.MultiReverseFundsTransactionModel
   :members:
