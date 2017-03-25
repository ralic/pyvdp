from django.shortcuts import render

from demo.forms.visadirect.reports import TransactionDataFormGet

from pyvdp.visadirect.reports import transaction_data

def index(request):
    return render(request, template_name='visadirect/reports/index.html')

def transactiondata(request):
    if request.method == 'POST':
        form = TransactionDataFormGet(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']

            result = transaction_data.get(from_date=from_date, to_date=to_date)
            return render(request, template_name='success.html', context={'result': result})
    else:
        form_get = TransactionDataFormGet()
        return render(request, template_name='visadirect/reports/transactiondata.html', context={'form_get': form_get})
