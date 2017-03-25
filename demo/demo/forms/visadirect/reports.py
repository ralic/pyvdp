from django import forms


class TransactionDataFormGet(forms.Form):
    from_date = forms.CharField(label='From', required=True)
    to_date = forms.CharField(label='To', required=True)
