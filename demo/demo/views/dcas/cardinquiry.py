from django.shortcuts import render

from pyvdp.dcas.cardinquiry.accounts import debitcardinquiry, DebitCardInquiryModel

from demo.forms.dcas.cardinquiry import DebitCardInquiryFormPost


def debit_card_inquiry(request):
    if request.method == 'POST':
        form = DebitCardInquiryFormPost(request.POST)
        if form.is_valid():
            direct_dan = form.cleaned_data['direct_dan']
            routing_number = form.cleaned_data['routing_number']
            ch_first_name = form.cleaned_data['ch_first_name']
            ch_last_name = form.cleaned_data['ch_last_name']

            cn_kwargs = {
                'firstName': ch_first_name,
                'lastName': ch_last_name
            }

            cim_kwargs = {
                'directDebitAccountNumber': direct_dan,
                'routingNumber': routing_number,
                'cardholderName': DebitCardInquiryModel.CardholderName(**cn_kwargs)
            }

            data = DebitCardInquiryModel(**cim_kwargs)

            result = debitcardinquiry.send(data=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = DebitCardInquiryFormPost()

        return render(request, template_name='dcas/cardinquiry/debitcardinquiry.html', context={'form_post': form_post})
