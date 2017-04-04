from pyvdp.visadirect import VisaDirectDispatcher


def send(data):
    """Submits a WatchlistInquiry request.

    :param WatchlistObject data: **Required**. Instance of :func:`~pyvdp.visadirect.watchlist.WatchlistObject`.
    :return: Dictionary with VDP API response
    """
    c = VisaDirectDispatcher(api='watchlistscreening', method='watchlistinquiry', http_verb='post', data=data)
    return c.send()
