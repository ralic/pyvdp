from pyvdp.dispatcher import VisaDispatcher


class VisaDirectDispatcher(VisaDispatcher):
    """Implements HTTP requests to Visa Direct APIs.

    :param data: **Required**. Instance of data model.
    :param str resource: **Required**. Resource name.
    :param str api: **Required**. API name.
    :param str method: **Required**. Method name.
    :param str http_verb: **Required**. HTTP Verb.
    :param str auth_method: **Required**. Authentication method. Possible values are: **ssl**, **token**.
    """

    def __init__(self, resource, api, method, version, http_verb, auth_method, url_params=None, data=None):

        super(VisaDirectDispatcher, self).__init__(resource=resource,
                                                   api=api,
                                                   version=version,
                                                   method=method,
                                                   http_verb=http_verb,
                                                   auth_method=auth_method,
                                                   url_params=url_params,
                                                   data=data)
