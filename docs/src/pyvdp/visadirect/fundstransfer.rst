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



.. automodule:: pyvdp.visadirect.fundstransfer.pull_funds
   :members:

---------
PushFunds
---------

.. automodule:: pyvdp.visadirect.fundstransfer.push_funds
   :members:

------------
ReverseFunds
------------

.. automodule:: pyvdp.visadirect.fundstransfer.reverse_funds
   :members:

++++++++++++
Data objects
++++++++++++

..  _pull_funds_transaction:

--------------------
PullFundsTransaction
--------------------

.. autoclass:: pyvdp.visadirect.fundstransfer.data.PullFundsTransaction
   :members:

.. autoclass:: pyvdp.visadirect.fundstransfer.data.MultiPullFundsTransaction
   :members:

..  _push_funds_transaction:

--------------------
PushFundsTransaction
--------------------

.. autoclass:: pyvdp.visadirect.fundstransfer.data.PushFundsTransaction
   :members:

.. autoclass:: pyvdp.visadirect.fundstransfer.data.MultiPushFundsTransaction
   :members:

-----------------------
ReverseFundsTransaction
-----------------------

.. autoclass:: pyvdp.visadirect.fundstransfer.data.ReverseFundsTransaction
   :members:

.. autoclass:: pyvdp.visadirect.fundstransfer.data.MultiReverseFundsTransaction
   :members:
