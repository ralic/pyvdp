from django import forms


class DebitCardInquiryFormPost(forms.Form):
    direct_dan = forms.CharField(required=True, initial='1234567890')
    routing_number = forms.CharField(required=True, initial='0987655321')
    ch_first_name = forms.CharField(required=True, initial='John')
    ch_last_name = forms.CharField(required=True, initial='Doe')
