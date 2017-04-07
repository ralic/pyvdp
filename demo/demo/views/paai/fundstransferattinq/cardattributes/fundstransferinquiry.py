from django.shortcuts import render

from pyvdp.paai.fundstransferattinq.cardattributes import fundstransferinquiry, FundsTransferInquiryModel

from demo.forms.paai.fundstransferattinq.cardattributes.fundstransferinquiry import FundsTransferInquiryPostForm


def funds_transfer_inquiry(request):
    if request.method == 'POST':
        form = FundsTransferInquiryPostForm(request.POST)
        if form.is_valid():
            pan = form.cleaned_data['pan']

            ftid_kwargs = {
                'systemsTraceAuditNumber': 123456,
                'primaryAccountNumber': pan,
            }

            data = FundsTransferInquiryModel(**ftid_kwargs)

            result = fundstransferinquiry.send(data=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = FundsTransferInquiryPostForm()
        return render(request,
                      template_name='paai/fundstransferattinq/cardattributes/fundstransferinquiry.html',
                      context={'form_post': form_post})
