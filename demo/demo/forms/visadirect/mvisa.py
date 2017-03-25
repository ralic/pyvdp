from django import forms


class CashinPushPaymentsFormPost(forms.Form):
    recipient_pan = forms.CharField(label='Recipient card PAN', max_length=16, required=True, initial="4123640062698797")
    amount = forms.FloatField(label='Amount', required=True, initial=124.05)
    sender_name = forms.CharField(label='Sender name', max_length=30, required=True, initial="Mohammed Qasim")
    sender_account_number = forms.CharField(label='Sender account number', max_length=13, required=True, initial="4541237895236")


class CashinPushPaymentsFormGet(forms.Form):
    status_id = forms.CharField(label='Status ID', required=True)


class CashoutPushPaymentsFormPost(forms.Form):
    recipient_pan = forms.CharField(label='Recipient card PAN', max_length=16, required=True, initial="4123640062698797")
    amount = forms.FloatField(label='Amount', required=True, initial=124.05)
    sender_name = forms.CharField(label='Sender name', max_length=30, required=True, initial="Mohammed Qasim")
    sender_account_number = forms.CharField(label='Sender account number', max_length=13, required=True, initial="456789123456")


class CashoutPushPaymentsFormGet(forms.Form):
    status_id = forms.CharField(label='Status ID', required=True)


class MerchantPushPaymentsFormPost(forms.Form):
    recipient_pan = forms.CharField(label='Recipient card PAN', max_length=16, required=True, initial="4123640062698797")
    amount = forms.FloatField(label='Amount', required=True, initial=124.05)
    sender_name = forms.CharField(label='Sender name', max_length=30, required=True, initial="Jasper")
    sender_account_number = forms.CharField(label='Sender account number', max_length=13, required=True, initial="4027290077881587")
    purchase_reference_number = forms.CharField(label='Purchase reference', max_length=25, required=True, initial="REF_123456789123456789123")


class MerchantPushPaymentsFormGet(forms.Form):
    status_id = forms.CharField(label='Status ID', required=True)
