from pyvdp.dispatcher import VisaDispatcher


class VisaDcasDispatcher(VisaDispatcher):

    def __init__(self, api, method, http_verb, query_string='', data=None, headers=None):
        super(VisaDcasDispatcher, self).__init__(resource='dcas',
                                                 api=api,
                                                 method=method,
                                                 http_verb=http_verb,
                                                 query_string=query_string,
                                                 data=data,
                                                 headers=headers)
