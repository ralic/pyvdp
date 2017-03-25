from django import forms


class GeneralInquiryPostForm(forms.Form):
    pan = forms.CharField(label='Card PAN', max_length=19, required=True, initial='4957030420210512')
