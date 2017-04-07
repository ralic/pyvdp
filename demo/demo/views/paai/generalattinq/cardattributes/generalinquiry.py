from django.shortcuts import render

from pyvdp.paai.generalattinq.cardattributes import generalinquiry, GeneralInquiryModel

from demo.forms.paai.generalattinq.cardattributes.generalinquiry import GeneralInquiryPostForm


def general_inquiry(request):
    if request.method == 'POST':
        form = GeneralInquiryPostForm(request.POST)
        if form.is_valid():
            pan = form.cleaned_data['pan']

            gid_kwargs = {
                'primaryAccountNumber': pan
            }

            data = GeneralInquiryModel(**gid_kwargs)

            result = generalinquiry.send(data=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = GeneralInquiryPostForm()
        return render(request,
                      template_name='paai/generalattinq/cardattributes/generalinquiry.html',
                      context={'form_post': form_post})
