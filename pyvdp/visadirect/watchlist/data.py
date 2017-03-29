import string
import random


class WatchlistData(object):
    """VisaDirect WatchlistScreening WatchlistInquiry data object model.

    :param str name: **Required**. Name of the person, to receive WLM score. Max 255 characters latin string.
    :param WatchlistDataAddress address: **Required**. Instance of :func:`~pyvdp.visadirect.watchlist.WatchlistData.WatchlistDataAddress`.
    :param int acquiring_bin: **Conditional**.  This field is required if acquirerCountryCode field is provided. Bank
        Identification Number provided during enrollment. 6-11 digits integer.
    :param int acquirer_country_code: **Optional**. Acquirer ISO country code, provided during enrollment. 3 digits
        integer

    **Example:**
        ..  code-block:: json

            {
                "acquirerCountryCode": "840",
                "acquiringBin": "408999",
                "address": {
                    "cardIssuerCountryCode": "USA",
                    "city": "San Francisco"
                },
                "name": "Mohammed Qasim",
                "referenceNumber": "330000550000"
            }
    """
    ATTR_MAPPINGS = {
        'name': 'name',
        'address': 'address',
        'acquiring_bin': 'acquiringBin',
        'acquirer_country_code': 'acquirerCountryCode'
    }

    def __init__(self, **kwargs):

        self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)
        self.referenceNumber = self.__get_reference()
        try:
            self.address = self.WatchlistDataAddress(**kwargs['address'])
        except KeyError:
            # If address is missing, skip silently, errors will be handled by VDP
            pass

    @staticmethod
    def __get_reference():
        """Generates random 12-digit reference to tie together a WLM score request and WLM score response service calls.

        :return: reference
        """
        return ''.join(random.choice(string.digits) for _ in range(12))

    class WatchlistDataAddress(object):
        """Watchlist address object model, part of :func:`~visa.visadirect.watchlist.data.WatchlistObject`.
    
        :param str city: **Required**. Client city name.
        :param str issuer_country_code: **Required**. Card issuer 3 characters ISO country code.
        """
        ATTR_MAPPINGS = {
            'city': 'city',
            'issuer_country_code': 'cardIssuerCountryCode'
        }

        def __init__(self, **kwargs):
            self.__dict__.update((self.ATTR_MAPPINGS[k], v) for k, v in kwargs.items() if k in self.ATTR_MAPPINGS and v)
