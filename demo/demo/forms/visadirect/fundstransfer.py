from django import forms


class PullFundsFormGet(forms.Form):
    status_id = forms.CharField(label='Status ID', required=True)


class PullFundsFormPost(forms.Form):
    sender_pan = forms.CharField(label='Sender card PAN', max_length=16, required=True, initial='4005520000011126')
    sender_expiry_date = forms.CharField(label='Sender card expiration', required=True, initial='2020-03')
    amount = forms.FloatField(label='Amount', required=True, initial=350.00)
    is_multi = forms.BooleanField(label='Multi?', required=False, initial=False)


class PushFundsFormGet(forms.Form):
    status_id = forms.CharField(label='Status ID', required=True)


class PushFundsFormPost(forms.Form):
    sender_pan = forms.CharField(label='Sender card PAN', max_length=16, required=True, initial='4957030420210454')
    recipient_pan = forms.CharField(label='Recipient card PAN', max_length=16, required=True, initial='4957030420210462')
    amount = forms.FloatField(label='Amount', required=True, initial=350.00)
    is_multi = forms.BooleanField(label='Multi?', required=False, initial=False)


class ReverseFundsFormGet(forms.Form):
    status_id = forms.CharField(label='Status ID', required=True)


class ReverseFundsFormPost(forms.Form):
    sender_pan = forms.CharField(label='Sender card PAN', max_length=16, required=True, initial='4895100000055127')
    sender_card_expiry_date = forms.CharField(label='Card expiration', required=True, initial='2015-10')
    transaction_identifier = forms.IntegerField(label='Transaction ID', required=True, initial='381228649430011')
    amount = forms.FloatField(label='Amount', required=True, initial=24.01)
    is_multi = forms.BooleanField(label='Multi?', required=False, initial=False)
