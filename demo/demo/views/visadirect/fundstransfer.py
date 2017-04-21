from django.shortcuts import render

from demo.forms.visadirect.fundstransfer import (PullFundsFormGet, PullFundsFormPost, PushFundsFormGet,
                                                 PushFundsFormPost, ReverseFundsFormGet, ReverseFundsFormPost)

from pyvdp.visadirect import CardAcceptorModel, OriginalDataElementsModel

from pyvdp.visadirect.fundstransfer import PullFundsTransactionsModel, MultiPullFundsTransactionsModel
from pyvdp.visadirect.fundstransfer import PushFundsTransactionsModel, MultiPushFundsTransactionsModel
from pyvdp.visadirect.fundstransfer import ReverseFundsTransactionsModel, MultiReverseFundsTransactionsModel

from pyvdp.visadirect.fundstransfer import pushfunds, pullfunds, reversefundstransactions


def index(request):
    return render(request, template_name='visadirect/fundstransfer/index.html')


def pull(request):
    if request.method == 'POST':
        result = {}
        if request.POST['action'] == 'post':
            form = PullFundsFormPost(request.POST)
            if form.is_valid():
                sender_pan = form.cleaned_data['sender_pan']
                sender_expiry_date = form.cleaned_data['sender_expiry_date']
                amount = form.cleaned_data['amount']
                is_multi = form.cleaned_data['is_multi']

                ca_kwargs = {
                    'name': 'Acceptor 1',
                    'address': {
                        'country': 'USA',
                        'zipCode': '12345',
                        'state': 'CA'
                    },
                    'terminalId': 'TID-9999',
                    'idCode': 'CA-IDCode-77765'
                }

                pft_kwargs = {
                    'systemsTraceAuditNumber': 123456,
                    'amount': amount,
                    'senderPrimaryAccountNumber': sender_pan,
                    'senderCardExpiryDate': sender_expiry_date,
                    'cardAcceptor': CardAcceptorModel(**ca_kwargs),
                    'senderCurrencyCode': 'USD',
                    'acquiringBin': 408999,
                    'acquirerCountryCode': 840,
                    'businessApplicationId': 'AA'
                }

                pft = PullFundsTransactionsModel(**pft_kwargs)

                if is_multi:
                    pft_kwargs = {
                        'stan': 123456,
                        'amount': amount,
                        'senderPrimaryAccountNumber': sender_pan,
                        'senderCardExpiryDate': sender_expiry_date,
                        'cardAcceptor': CardAcceptorModel(**ca_kwargs),
                        'senderCurrencyCode': 'USD',
                    }

                    mpft_kwargs = {
                        'acquiringBin': 408999,
                        'acquirerCountryCode': 840,
                        'businessApplicationId': 'AA',
                        'request': [
                            PullFundsTransactionsModel(**pft_kwargs)
                        ]
                    }

                    mpft = MultiPullFundsTransactionsModel(**mpft_kwargs)
                    result = pullfunds.send(data=mpft, multi=True)
                else:
                    result = pullfunds.send(data=pft)
        else:
                form = PullFundsFormGet(request.POST)
                if form.is_valid():
                    status_id = form.cleaned_data['status_id']
                    result = pullfunds.get(query=status_id, multi=True)

        return render(request, template_name='success.html', context={'result': result})

    else:
        form_post = PullFundsFormPost()
        form_get = PullFundsFormGet()
        return render(request,
                      template_name='visadirect/fundstransfer/pullfunds.html',
                      context={'form_get': form_get, 'form_post': form_post})


def push(request):
    if request.method == 'POST':
        form = PushFundsFormPost(request.POST)
        if form.is_valid():
            sender_pan = form.cleaned_data['sender_pan']
            recipient_pan = form.cleaned_data['recipient_pan']
            amount = form.cleaned_data['amount']
            is_multi = form.cleaned_data['is_multi']

            ca_kwargs = {
                'name': 'Acceptor 1',
                'terminalId': 'TID-9999',
                'idCode': 'CA-IDCode-77765',
                'address': {
                    'country': 'USA',
                    'zipCode': '12345',
                    'state': 'CA'
                }
            }

            pft_kwargs = {
                'systemsTraceAuditNumber': 123456,
                'acquiringBin': 408999,
                'acquirerCountryCode': 840,
                'businessApplicationId': 'AA',
                'amount': amount,
                'cardAcceptor': CardAcceptorModel(**ca_kwargs),
                'senderAccountNumber': sender_pan,
                'recipientPrimaryAccountNumber': recipient_pan,
                'recipientName': 'Doe John',
                'transactionCurrencyCode': 'USD'
            }

            data = PushFundsTransactionsModel(**pft_kwargs)

            if is_multi:

                pft_kwargs = {
                    'systemsTraceAuditNumber': 123456,
                    'amount': amount,
                    'cardAcceptor': CardAcceptorModel(**ca_kwargs),
                    'senderAccountNumber': sender_pan,
                    'senderName': 'Doe Jane',
                    'senderAddress': 'Home',
                    'senderCity': 'San Francisco',
                    'senderCountryCode': 'USA',
                    'senderStateCode': 'CA',
                    'recipientPrimaryAccountNumber': recipient_pan,
                    'recipientName': 'Doe John',
                    'transactionCurrencyCode': 'USD'
                }

                mpft_kwargs = {
                    'acquiringBin': 408999,
                    'acquirerCountryCode': 840,
                    'businessApplicationId': 'AA',
                    'request': [
                        PushFundsTransactionsModel(**pft_kwargs)
                    ]
                }

                mpft = MultiPushFundsTransactionsModel(**mpft_kwargs)
                result = pushfunds.send(data=mpft, multi=True)
            else:
                result = pushfunds.send(data=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = PushFundsFormPost()
        form_get = PushFundsFormGet()
        return render(request,
                      template_name='visadirect/fundstransfer/pushfunds.html',
                      context={'form_post': form_post, 'form_get': form_get})


def reverse(request):
    if request.method == 'POST':
        form = ReverseFundsFormPost(request.POST)
        if form.is_valid():
            sender_pan = form.cleaned_data['sender_pan']
            sender_card_expiry_date = form.cleaned_data['sender_card_expiry_date']
            transaction_identifier = form.cleaned_data['transaction_identifier']
            amount = form.cleaned_data['amount']
            is_multi = form.cleaned_data['is_multi']

            ca_kwargs = {
                'name': 'Acceptor 1',
                'terminalId': 'TID-9999',
                'idCode': 'CA-IDCode-77765',
                'address': {
                    'country': 'USA',
                    'zipCode': '12345',
                    'state': 'CA'
                }
            }

            ode_kwargs = {
                'systemsTraceAuditNumber': 123456,
                'acquiringBin': 408999,
                'approvalCode': '20304B',
                'transmissionDateTime': '2017-02-16T12:59:23'
            }

            rft_kwargs = {
                'systemsTraceAuditNumber': 123456,
                'acquiringBin': 408999,
                'acquirerCountryCode': 608,
                'originalDataElements': OriginalDataElementsModel(**ode_kwargs),
                'cardAcceptor': CardAcceptorModel(**ca_kwargs),
                'senderPrimaryAccountNumber': sender_pan,
                'senderCurrencyCode': 'USD',
                'amount': amount,
                'senderCardExpiryDate': sender_card_expiry_date,
                'transactionIdentifier': transaction_identifier
            }

            rft = ReverseFundsTransactionsModel(**rft_kwargs)

            if is_multi:

                rft_kwargs = {
                    'systemsTraceAuditNumber': 123456,
                    'originalDataElements': OriginalDataElementsModel(**ode_kwargs),
                    'cardAcceptor': CardAcceptorModel(**ca_kwargs),
                    'sender_pan': sender_pan,
                    'senderPrimaryAccountNumber': 'USD',
                    'amount': amount,
                    'senderCardExpiryDate': sender_card_expiry_date,
                    'transactionIdentifier': transaction_identifier
                }

                mrft_kwargs = {
                    'acquiringBin': 408999,
                    'acquirerCountryCode': 608,
                    'request': [
                        ReverseFundsTransactionsModel(**rft_kwargs)
                    ]
                }

                mrft = MultiReverseFundsTransactionsModel(**mrft_kwargs)

                result = reversefundstransactions.send(data=mrft, multi=True)

            else:
                result = reversefundstransactions.send(data=rft)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = ReverseFundsFormPost()
        form_get = ReverseFundsFormGet()
        return render(request,
                      template_name='visadirect/fundstransfer/reversefunds.html',
                      context={'form_post': form_post, 'form_get': form_get})
