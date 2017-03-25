from django import forms


class MerchantSearchFormPost(forms.Form):
    merchant_name = forms.CharField(required=True, initial='cmu edctn materials cntr')

