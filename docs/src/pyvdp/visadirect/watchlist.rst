==============================
VisaDirect Watchlist Screening
==============================

.. seealso::

    https://developer.visa.com/products/visa_direct/reference#visa_direct__ws

+++++
Usage
+++++

The Watch List Screening API provides an OFAC score value used for evaluation on how closely an individual's name,
city, and country input fields match against entries on the OFAC SDN lists. The Watch List Screening API also provides
an OFAC status value which represents how VisaNet would process the individual's information if used in a cross-border
OCT transaction.

----------------
WatchlistInquiry
----------------

.. automodule:: pyvdp.visadirect.watchlist.watchlistinquiry
   :members:

++++++++++++
Data Objects
++++++++++++

---------------
WatchlistObject
---------------

.. autoclass:: pyvdp.visadirect.watchlist.WatchlistData
   :members:
