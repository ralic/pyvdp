from django.shortcuts import render

from demo.forms.visadirect.mvisa import (CashinPushPaymentsFormPost, CashinPushPaymentsFormGet,
                                         CashoutPushPaymentsFormPost, CashoutPushPaymentsFormGet,
                                         MerchantPushPaymentsFormPost, MerchantPushPaymentsFormGet)

from pyvdp.visadirect.mvisa import (cashinpushpayments,
                                    cashoutpushpayments,
                                    merchantpushpayments)

from pyvdp.visadirect import CardAcceptor
from pyvdp.visadirect.mvisa import CashinPushPaymentTransaction
from pyvdp.visadirect.mvisa import CashoutPushPaymentTransaction
from pyvdp.visadirect.mvisa import MerchantPushPaymentTransaction
from pyvdp.visadirect.mvisa import PurchaseIdentifier


def index(request):
    return render(request, template_name='visadirect/mvisa/index.html')


def cipp(request):
    if request.method == 'POST':
        result = {}
        if request.POST['action'] == 'post':
            form = CashinPushPaymentsFormPost(request.POST)
            if form.is_valid():
                recipient_pan = form.cleaned_data['recipient_pan']
                amount = form.cleaned_data['amount']
                sender_name = form.cleaned_data['sender_name']
                sender_account_number = form.cleaned_data['sender_account_number']

                ca_kwargs = {
                    'name': 'Acceptor 1',
                    'terminal_id': 'TID-9999',
                    'id_code': 'CA-IDCode-77765',
                    'address': {
                        'country': 'IND',
                        'city': 'Bangalore',
                    }
                }

                cippt_kwargs = {
                    'stan': 123456,
                    'acquiring_bin': 400171,
                    'acquirer_country_code': 643,
                    'business_application_id': 'CI',
                    'amount': amount,
                    'recipient_pan': recipient_pan,
                    'sender_account_number': sender_account_number,
                    'sender_name': sender_name,
                    'transaction_currency_code': 'USD',
                    'card_acceptor': CardAcceptor(**ca_kwargs)
                }

                cippt = CashinPushPaymentTransaction(**cippt_kwargs)

                result = cashinpushpayments.send(data=cippt)
        else:
            form = CashinPushPaymentsFormGet(request.POST)
            if form.is_valid():
                status_id = form.cleaned_data['status_id']
                result = cashinpushpayments.get(query=status_id)

        return render(request, template_name='success.html',  context={'result': result})

    else:
        form_get = CashinPushPaymentsFormGet()
        form_post = CashinPushPaymentsFormPost()

        return render(request,
                      template_name='visadirect/mvisa/cipp.html',
                      context={'form_get': form_get, 'form_post': form_post})


def copp(request):
    if request.method == 'POST':
        result = {}
        if request.POST['action'] == 'post':
            form = CashoutPushPaymentsFormPost(request.POST)
            if form.is_valid():
                recipient_pan = form.cleaned_data['recipient_pan']
                amount = form.cleaned_data['amount']
                sender_name = form.cleaned_data['sender_name']
                sender_account_number = form.cleaned_data['sender_account_number']

                ca_kwargs = {
                    'name': 'Acceptor 1',
                    'terminal_id': 'TID-9999',
                    'id_code': 'CA-IDCode-77765',
                    'address': {
                        'country': 'IND',
                        'city': 'Bangalore',
                    }
                }

                coppt_kwargs = {
                    'stan': 123456,
                    'acquiring_bin': 400171,
                    'acquirer_country_code': 643,
                    'business_application_id': 'CI',
                    'amount': amount,
                    'recipient_pan': recipient_pan,
                    'sender_account_number': sender_account_number,
                    'sender_name': sender_name,
                    'transaction_currency_code': 'USD',
                    'card_acceptor': CardAcceptor(**ca_kwargs)
                }

                coppt = CashoutPushPaymentTransaction(**coppt_kwargs)

                result = cashoutpushpayments.send(data=coppt)
        else:
                form = CashoutPushPaymentsFormGet(request.POST)
                if form.is_valid():
                    status_id = form.cleaned_data['status_id']
                    result = cashoutpushpayments.get(query=status_id)

        return render(request, template_name='success.html', context={'result': result})
    else:
        form_get = CashoutPushPaymentsFormGet()
        form_post = CashoutPushPaymentsFormPost()
        return render(request,
                      template_name='visadirect/mvisa/copp.html',
                      context={'form_get': form_get, 'form_post': form_post})


def mpp(request):
    if request.method == 'POST':
        result = {}
        if request.POST['action'] == 'post':
            form = MerchantPushPaymentsFormPost(request.POST)
            if form.is_valid():
                recipient_pan = form.cleaned_data['recipient_pan']
                amount = form.cleaned_data['amount']
                sender_name = form.cleaned_data['sender_name']
                sender_account_number = form.cleaned_data['sender_account_number']
                purchase_reference_number = form.cleaned_data['purchase_reference_number']

                ca_kwargs = {
                    'name': 'Acceptor 1',
                    'terminal_id': 'TID-9999',
                    'id_code': 'CA-IDCode-77765',
                    'address': {
                        'country': 'IND',
                        'city': 'Bangalore',
                    }
                }

                pi_kwargs = {
                    'type': '0',
                    'reference_number': purchase_reference_number
                }

                mppt_kwargs = {
                    'stan': 123456,
                    'amount': amount,
                    'acquiring_bin': 408972,
                    'acquirer_country_code': 356,
                    'transaction_currency_code': 'USD',
                    'recipient_pan': recipient_pan,
                    'recipient_name': 'Jasper',
                    'sender_name': sender_name,
                    'sender_account_number': sender_account_number,
                    'card_acceptor': CardAcceptor(**ca_kwargs),
                    'purchase_id': PurchaseIdentifier(**pi_kwargs),
                    'business_application_id': 'MP'
                }

                mppt = MerchantPushPaymentTransaction(**mppt_kwargs)

                result = merchantpushpayments.send(data=mppt)
        else:
            form = MerchantPushPaymentsFormGet(request.POST)
            if form.is_valid():
                status_id = form.cleaned_data['status_id']
                result = merchantpushpayments.get(query=status_id)

        return render(request, template_name='success.html', context={'result': result})
    else:
        form_get = MerchantPushPaymentsFormGet()
        form_post = MerchantPushPaymentsFormPost()
        return render(request, template_name='visadirect/mvisa/mpp.html',
                      context={'form_get': form_get, 'form_post': form_post})