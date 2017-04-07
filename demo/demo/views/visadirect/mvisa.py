from django.shortcuts import render

from demo.forms.visadirect.mvisa import (CashinPushPaymentsFormPost, CashinPushPaymentsFormGet,
                                         CashoutPushPaymentsFormPost, CashoutPushPaymentsFormGet,
                                         MerchantPushPaymentsFormPost, MerchantPushPaymentsFormGet)

from pyvdp.visadirect.mvisa import (cashinpushpayments,
                                    cashoutpushpayments,
                                    merchantpushpayments)

from pyvdp.visadirect import CardAcceptorModel
from pyvdp.visadirect.mvisa import CashinPushPaymentTransactionModel
from pyvdp.visadirect.mvisa import CashoutPushPaymentTransactionModel
from pyvdp.visadirect.mvisa import MerchantPushPaymentTransactionModel
from pyvdp.visadirect.mvisa import PurchaseIdentifierModel


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
                    'terminalId': 'TID-9999',
                    'idCode': 'CA-IDCode-77765',
                    'address': {
                        'country': 'IND',
                        'city': 'Bangalore',
                    }
                }

                cippt_kwargs = {
                    'systemsTraceAuditNumber': 123456,
                    'acquiringBin': 400171,
                    'acquirerCountryCode': 643,
                    'businessApplicationId': 'CI',
                    'amount': amount,
                    'recipientPrimaryAccountNumber': recipient_pan,
                    'senderAccountNumber': sender_account_number,
                    'senderName': sender_name,
                    'transactionCurrencyCode': 'USD',
                    'cardAcceptor': CardAcceptorModel(**ca_kwargs)
                }

                cippt = CashinPushPaymentTransactionModel(**cippt_kwargs)

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
                    'terminalId': 'TID-9999',
                    'idCode': 'CA-IDCode-77765',
                    'address': {
                        'country': 'IND',
                        'city': 'Bangalore',
                    }
                }

                coppt_kwargs = {
                    'systemsTraceAuditNumber': 123456,
                    'acquiringBin': 400171,
                    'acquirerCountryCode': 643,
                    'businessApplicationId': 'CI',
                    'amount': amount,
                    'recipientPrimaryAccountNumber': recipient_pan,
                    'senderAccountNumber': sender_account_number,
                    'senderName': sender_name,
                    'transactionCurrencyCode': 'USD',
                    'cardAcceptor': CardAcceptorModel(**ca_kwargs)
                }

                coppt = CashoutPushPaymentTransactionModel(**coppt_kwargs)

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
                    'terminalId': 'TID-9999',
                    'idCode': 'CA-IDCode-77765',
                    'address': {
                        'country': 'IND',
                        'city': 'Bangalore',
                    }
                }

                pi_kwargs = {
                    'type': '0',
                    'referenceNumber': purchase_reference_number
                }

                mppt_kwargs = {
                    'systemsTraceAuditNumber': 123456,
                    'amount': amount,
                    'acquiringBin': 408972,
                    'acquirerCountryCode': 356,
                    'transactionCurrencyCode': 'USD',
                    'recipientPrimaryAccountNumber': recipient_pan,
                    'recipient_name': 'Jasper',
                    'senderName': sender_name,
                    'senderAccountNumber': sender_account_number,
                    'cardAcceptor': CardAcceptorModel(**ca_kwargs),
                    'purchaseIdentifier': PurchaseIdentifierModel(**pi_kwargs),
                    'businessApplicationId': 'MP'
                }

                mppt = MerchantPushPaymentTransactionModel(**mppt_kwargs)

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