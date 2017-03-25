from django import forms


class WlInquiryFormPost(forms.Form):
    name = forms.CharField(label='Client name', max_length=255, required=True, initial="Mohammed Qasim")
    city = forms.CharField(label='Client city', max_length=25, required=True, initial="San Francisco")
    issuer_country_code = forms.CharField(label='Card issuer country code', max_length=3, required=True, initial="USA")