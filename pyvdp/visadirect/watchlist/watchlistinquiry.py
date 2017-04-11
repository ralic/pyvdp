from pyvdp.visadirect import VisaDirectDispatcher


def send(data):
    """Submits a WatchlistInquiry request.

    :param WatchListInquiryModel data: **Required**. 
        Instance of :func:`~pyvdp.visadirect.watchlist.WatchListInquiryModel`.
    :return: Dictionary with VDP API response.
    
    **Usage:**
    
    ..  code-block:: python

        from pyvdp.visadirect.watchlist import watchlistinquiry, WatchListInquiryModel
        
        wli_address_kwargs = {
            "cardIssuerCountryCode": "USA",
            "city": "San Francisco"        
        }
        
        wli_kwargs = {
            "acquirerCountryCode": "840",
            "acquiringBin": "408999",
            "address": WatchListInquiryModel.WatchListInquiryAddress(**wli_address_kwargs),
            "name": "Mohammed Qasim",
            "referenceNumber": "330000550000"            
        }
        
        data = WatchListInquiryModel(**wli_kwargs)
        
        result = watchlistinquiry.send(data=data)
        print(result)
    """
    c = VisaDirectDispatcher(api='watchlistscreening', method='watchlistinquiry', http_verb='post', data=data)
    return c.send()
