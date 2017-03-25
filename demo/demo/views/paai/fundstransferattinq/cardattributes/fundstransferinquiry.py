from django.shortcuts import render

from pyvdp.paai.fundstransferattinq.cardattributes.data import FundsTransferInquiryData
from pyvdp.paai.fundstransferattinq.cardattributes import fundstransferinquiry

from demo.forms.paai.fundstransferattinq.cardattributes.fundstransferinquiry import FundsTransferInquiryPostForm


def funds_transfer_inquiry(request):
    if request.method == 'POST':
        form = FundsTransferInquiryPostForm(request.POST)
        if form.is_valid():
            pan = form.cleaned_data['pan']

            data = FundsTransferInquiryData(stan=123456,
                                            pan=pan)

            result = fundstransferinquiry.send(data=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = FundsTransferInquiryPostForm()
        return render(request,
                      template_name='paai/fundstransferattinq/cardattributes/fundstransferinquiry.html',
                      context={'form_post': form_post})
