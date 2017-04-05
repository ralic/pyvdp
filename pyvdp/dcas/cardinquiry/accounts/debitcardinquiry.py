from pyvdp.dcas.dispatcher import VisaDcasDispatcher

API = 'cardinquiry'
METHOD = 'accounts/debitcardinquiry'


def send(data):
    c = VisaDcasDispatcher(api=API, method=METHOD, http_verb='POST', data=data)
    return c.send()
