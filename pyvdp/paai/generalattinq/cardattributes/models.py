class GeneralInquiryModel(object):
    """General Card Attributes Inquiry data object model.

    :param str primaryAccountNumber: **Required**. Primary account number (PAN). 13-19 characters string.

    **Example:**
        ..  code-block:: json

            {
                "primaryAccountNumber": "4465390000029077"
            }
    """
    ATTRS = [
        'primaryAccountNumber'
    ]

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in self.ATTRS and value:
                self.__setattr__(attr, value)
