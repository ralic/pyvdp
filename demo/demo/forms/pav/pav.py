from django import forms


class CardValidationFormPost(forms.Form):
    pan = forms.CharField(label='Card PAN', max_length=16, required=True, initial="4957030000313108")
    expiry_date = forms.CharField(label='Card expiration', required=True, initial="2018-06")
    cvv2 = forms.CharField(label='Card CVV2', max_length=3, required=True, initial="672 ")