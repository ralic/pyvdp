from django.shortcuts import render

from demo.forms.visadirect.mvisa import (CashinPushPaymentsFormPost, CashinPushPaymentsFormGet,
                                         CashoutPushPaymentsFormPost, CashoutPushPaymentsFormGet,
                                         MerchantPushPaymentsFormPost, MerchantPushPaymentsFormGet)

from pyvdp.visadirect.mvisa import (cashin_push_payments,
                                    cashout_push_payments,
                                    merchant_push_payments)

from pyvdp.visadirect.data import CardAcceptor
from pyvdp.visadirect.mvisa.data import CashinPushPaymentTransaction
from pyvdp.visadirect.mvisa.data import CashoutPushPaymentTransaction
from pyvdp.visadirect.mvisa.data import MerchantPushPaymentTransaction
from pyvdp.visadirect.mvisa.data import PurchaseIdentifier

def index(request):
    return render(request, template_name='visadirect/mvisa/index.html')

def cashinpushpayments(request):
    if request.method == 'POST':
        result = {}
        if request.POST['action'] == 'post':
            form = CashinPushPaymentsFormPost(request.POST)
            if form.is_valid():
                recipient_pan = form.cleaned_data['recipient_pan']
                amount = form.cleaned_data['amount']
                sender_name = form.cleaned_data['sender_name']
                sender_account_number = form.cleaned_data['sender_account_number']

                card_acceptor = CardAcceptor(name='Acceptor 1',
                                             terminal_id='TID-9999',
                                             id_code='CA-IDCode-77765',
                                             address={
                                                 'country': 'USA',
                                                 'city': 'SFO',
                                                 'zip_code': '12345',
                                                 'state': 'CA'
                                             })

                transaction = CashinPushPaymentTransaction(stan=123456,
                                                           amount=amount,
                                                           transaction_currency_code='USD',
                                                           card_acceptor=card_acceptor,
                                                           recipient_pan=recipient_pan,
                                                           sender_name=sender_name,
                                                           sender_account_number=sender_account_number)

                result = cashin_push_payments.send(transaction)
        else:
            form = CashinPushPaymentsFormGet(request.POST)
            if form.is_valid():
                status_id = form.cleaned_data['status_id']
                result = cashin_push_payments.get(status_id=status_id)

        return render(request, template_name='success.html',  context={'result': result})

    else:
        form_get = CashinPushPaymentsFormGet()
        form_post = CashinPushPaymentsFormPost()

        return render(request,
                      template_name='visadirect/mvisa/cipp.html',
                      context={'form_get': form_get, 'form_post': form_post})

def cashoutpushpayments(request):
    if request.method == 'POST':
        result = {}
        if request.POST['action'] == 'post':
            form = CashoutPushPaymentsFormPost(request.POST)
            if form.is_valid():
                recipient_pan = form.cleaned_data['recipient_pan']
                amount = form.cleaned_data['amount']
                sender_name = form.cleaned_data['sender_name']
                sender_account_number = form.cleaned_data['sender_account_number']

                card_acceptor = CardAcceptor(name='Acceptor 1',
                                             terminal_id='TID-9999',
                                             id_code='CA-IDCode-77765',
                                             address={
                                                 'country': 'USA',
                                                 'city': 'SFO',
                                                 'zip_code': '12345',
                                                 'state': 'CA'
                                             })

                transaction = CashoutPushPaymentTransaction(stan=123456,
                                                            amount=amount,
                                                            transaction_currency_code='USD',
                                                            card_acceptor=card_acceptor,
                                                            recipient_pan=recipient_pan,
                                                            sender_name=sender_name,
                                                            sender_account_number=sender_account_number)

                result = cashout_push_payments.send(transaction)
        else:
                form = CashoutPushPaymentsFormGet(request.POST)
                if form.is_valid():
                    status_id = form.cleaned_data['status_id']
                    result = cashin_push_payments.get(status_id=status_id)

        return render(request, template_name='success.html', context={'result': result})
    else:
        form_get = CashoutPushPaymentsFormGet()
        form_post = CashoutPushPaymentsFormPost()
        return render(request,
                      template_name='visadirect/mvisa/copp.html',
                      context={'form_get': form_get, 'form_post': form_post})

def merchantpushpayments(request):
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

                card_acceptor = CardAcceptor(name='Acceptor 1',
                                             terminal_id='TID-9999',
                                             id_code='CA-IDCode-77765',
                                             address={
                                                 'country': 'USA',
                                                 'city': 'SFO',
                                                 'zip_code': '12345',
                                                 'state': 'CA'
                                             })

                purchase_identifier = PurchaseIdentifier(reference_number=purchase_reference_number, type='0')

                transaction = MerchantPushPaymentTransaction(stan=123456,
                                                             amount=amount,
                                                             transaction_currency_code='USD',
                                                             card_acceptor=card_acceptor,
                                                             recipient_pan=recipient_pan,
                                                             sender_name=sender_name,
                                                             purchase_identifier=purchase_identifier,
                                                             sender_account_number=sender_account_number)

                result = merchant_push_payments.send(transaction)
        else:
            form = MerchantPushPaymentsFormGet(request.POST)
            if form.is_valid():
                status_id = form.cleaned_data['status_id']
                result = merchant_push_payments.get(status_id=status_id)

        return render(request, template_name='success.html', context={'result': result})
    else:
        form_get = MerchantPushPaymentsFormGet()
        form_post = MerchantPushPaymentsFormPost()
        return render(request, template_name='visadirect/mvisa/mpp.html',
                      context={'form_get': form_get, 'form_post': form_post})