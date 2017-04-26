from pyvdp.dispatcher import VisaDispatcher


class VisaDcasDispatcher(VisaDispatcher):
    """Implements HTTP requests to Visa Digital Card and Accounts APIs.

    :param data: **Required**. Instance of data model. 
    :param str resource: **Required**. Resource name.
    :param str api: **Required**. API name.
    :param str version: **Required**. API version.
    :param str method: **Required**. Method name.
    :param str http_verb: **Required**. HTTP Verb.
    :param str auth_method: **Required**. Authentication method. Possible values are: **ssl** for ssl-based
        authentication, **token** for token-based authentication.    
    """
    def __init__(self, resource, api, version, method, http_verb, auth_method, data):
        super(VisaDcasDispatcher, self).__init__(resource=resource,
                                                 api=api,
                                                 version=version,
                                                 method=method,
                                                 http_verb=http_verb,
                                                 auth_method=auth_method,
                                                 data=data)
