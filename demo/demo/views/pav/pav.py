from django.shortcuts import render

from pyvdp.pav.data import PavTransaction
from pyvdp.pav import cardvalidation

from demo.forms.pav.pav import CardValidationFormPost


def card_validation(request):
    if request.method == 'POST':
        form = CardValidationFormPost(request.POST)
        if form.is_valid():
            pan = form.cleaned_data['pan']
            expiry_date = form.cleaned_data['expiry_date']
            cvv2 = form.cleaned_data['cvv2']

            data = PavTransaction(stan=123456,
                                  pan=pan,
                                  expiry_date=expiry_date,
                                  cvv2=cvv2)

            result = cardvalidation.send(data=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = CardValidationFormPost()
        return render(request, template_name='pav/card_validation.html', context={'form_post': form_post})
