from datetime import datetime
from pyvdp.paai import PaymentAccountAttributesInquiry


class FundsTransferInquiry(PaymentAccountAttributesInquiry):
    """Funds Transfer Inquiry data object model.

    :param str pan: **Required**. Primary account number (PAN). 13-19 characters string.
    :param int stan: **Required**. Systems trace audit number.  6 digits integer.
    :param int acquiring_bin: **Optional**. BIN under which FundsTransfer app is registered. 6-11 digits integer.
    :param int acquirer_country_code: **Optional**. 3 digits acquirer country code.

    **Example:**
        ..  code-block:: json

            {
                "primaryAccountNumber": "4957030420210512",
                "retrievalReferenceNumber": "330000550000",
                "systemsTraceAuditNumber": "451006"
            }
    """
    ATTR_MAPPINGS = {
        'pan': 'primaryAccountNumber',
        'acquiring_bin': 'acquiringBin',
        'acquirer_country_code': 'acquirerCountryCode',
    }

    def __init__(self, stan, **kwargs):
        super(FundsTransferInquiry, self).__init__(stan, **kwargs)
        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)

        self.systemsTraceAuditNumber = stan

        try:
            self.retrievalReferenceNumber = kwargs['rrn']
        except KeyError:
            self.retrievalReferenceNumber = self._get_rrn()

    def _get_rrn(self):
        """Generates RRN (retrievalReferenceNumber).

        :return: str rrn: Last digit of current year + number of current day in the year + current hour + STAN
        """
        now = datetime.now()
        year_last_digit = now.strftime('%Y')[3]
        day_of_the_year = now.strftime('%j')
        current_hour = now.strftime('%H')
        return year_last_digit + day_of_the_year + current_hour + str(self.systemsTraceAuditNumber)
