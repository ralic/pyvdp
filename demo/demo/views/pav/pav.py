from django.shortcuts import render

from pyvdp.pav import cardvalidation, PaymentAccountValidationModel
from pyvdp.visadirect import CardAcceptorModel

from demo.forms.pav.pav import CardValidationFormPost


def card_validation(request):
    if request.method == 'POST':
        form = CardValidationFormPost(request.POST)
        if form.is_valid():
            pan = form.cleaned_data['pan']
            expiry_date = form.cleaned_data['expiry_date']
            cvv2 = form.cleaned_data['cvv2']

            avr_kwargs = {
                "postalCode": "T4B 3G5",
                "street": "2881 Main Street Sw"
            }

            ca_kwargs = {
                "address": {
                    "city": "fostr city",
                    "country": "PAKISTAN",
                    "county": "CA",
                    "state": "CA",
                    "zipCode": "94404"
                },
                "idCode": "111111",
                "name": "rohan",
                "terminalId": "123"
            }

            pav_kwargs = {
                'primaryAccountNumber': pan,
                'cardExpiryDate': expiry_date,
                'cardCvv2Value': cvv2,
                'cardAcceptor': CardAcceptorModel(**ca_kwargs),
                'addressVerificationResults': PaymentAccountValidationModel.AddressVerificationResults(**avr_kwargs)
            }

            data = PaymentAccountValidationModel(**pav_kwargs)

            result = cardvalidation.send(data=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = CardValidationFormPost()
        return render(request, template_name='pav/card_validation.html', context={'form_post': form_post})
