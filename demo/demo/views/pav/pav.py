from django.shortcuts import render

from pyvdp.pav import PavData
from pyvdp.visadirect import CardAcceptor
from pyvdp.pav import cardvalidation

from demo.forms.pav.pav import CardValidationFormPost


def card_validation(request):
    if request.method == 'POST':
        form = CardValidationFormPost(request.POST)
        if form.is_valid():
            pan = form.cleaned_data['pan']
            expiry_date = form.cleaned_data['expiry_date']
            cvv2 = form.cleaned_data['cvv2']

            avr_kwargs = {
                "postal_code": "T4B 3G5",
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
                "id_code": "111111",
                "name": "rohan",
                "terminal_id": "123"
            }

            pav_kwargs = {
                'pan': pan,
                'card_expiry_date': expiry_date,
                'cvv2': cvv2,
                'card_acceptor': CardAcceptor(**ca_kwargs),
                'avr': PavData.AddressVerificationResults(**avr_kwargs)
            }

            data = PavData(**pav_kwargs)

            result = cardvalidation.send(data=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = CardValidationFormPost()
        return render(request, template_name='pav/card_validation.html', context={'form_post': form_post})
