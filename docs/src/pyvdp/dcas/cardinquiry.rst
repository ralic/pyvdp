================
Card Inquiry API
================

..  seealso::

    https://developer.visa.com/products/dcas/reference

+++++
Usage
+++++

..  code-block:: python

        from pyvdp.dcas.cardinquiry.accounts import debitcardinquiry, CardInquiryModel

        cn_kwargs = {
            'first_name': 'John',
            'last_name': 'Doe'
        }

        cim_kwargs = {
            'direct_dan': '0987654321',
            'routing_number': '1234567890',
            'cardholder_name': CardInquiryModel.CardholderName(**cn_kwargs)
        }

        cim = CardInquiryModel(**cim_kwargs)
        result = debitcardinquiry.send(data=cim)
        print result['response']

++++++
Models
++++++

----------------
CardInquiryModel
----------------

..  autoclass:: pyvdp.dcas.cardinquiry.accounts.CardInquiryModel
    :members:
