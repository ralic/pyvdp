from django.shortcuts import render

from demo.forms.visadirect.fundstransfer import (PullFundsFormGet, PullFundsFormPost, PushFundsFormGet,
                                                 PushFundsFormPost, ReverseFundsFormGet, ReverseFundsFormPost)

from pyvdp.visadirect import CardAcceptor, OriginalDataElements

from pyvdp.visadirect.fundstransfer import PullFundsTransaction, MultiPullFundsTransaction
from pyvdp.visadirect.fundstransfer import PushFundsTransaction, MultiPushFundsTransaction
from pyvdp.visadirect.fundstransfer import ReverseFundsTransaction, MultiReverseFundsTransaction

from pyvdp.visadirect.fundstransfer import pushfunds, pullfunds, reversefunds


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
                        'zip_code': '12345',
                        'state': 'CA'
                    },
                    'terminal_id': 'TID-9999',
                    'id_code': 'CA-IDCode-77765'
                }

                pft_kwargs = {
                    'stan': 123456,
                    'amount': amount,
                    'sender_pan': sender_pan,
                    'sender_expiration': sender_expiry_date,
                    'card_acceptor': CardAcceptor(**ca_kwargs),
                    'sender_currency_code': 'USD',
                    'acquiring_bin': 408999,
                    'acquirer_country_code': 840,
                    'business_application_id': 'AA'
                }

                pft = PullFundsTransaction(**pft_kwargs)

                if is_multi:
                    pft_kwargs = {
                        'stan': 123456,
                        'amount': amount,
                        'sender_pan': sender_pan,
                        'sender_expiration': sender_expiry_date,
                        'card_acceptor': CardAcceptor(**ca_kwargs),
                        'sender_currency_code': 'USD',
                    }

                    mpft_kwargs = {
                        'acquiring_bin': 408999,
                        'acquirer_country_code': 840,
                        'business_application_id': 'AA',
                        'request': [
                            PullFundsTransaction(**pft_kwargs)
                        ]
                    }

                    mpft = MultiPullFundsTransaction(**mpft_kwargs)
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
                'terminal_id': 'TID-9999',
                'id_code': 'CA-IDCode-77765',
                'address': {
                    'country': 'USA',
                    'zip_code': '12345',
                    'state': 'CA'
                }
            }

            pft_kwargs = {
                'stan': 123456,
                'acquiring_bin': 408999,
                'acquirer_country_code': 840,
                'business_application_id': 'AA',
                'amount': amount,
                'card_acceptor': CardAcceptor(**ca_kwargs),
                'sender_account_number': sender_pan,
                'recipient_pan': recipient_pan,
                'recipient_name': 'Doe John',
                'transaction_currency_code': 'USD'
            }

            data = PushFundsTransaction(**pft_kwargs)

            if is_multi:

                pft_kwargs = {
                    'stan': 123456,
                    'amount': amount,
                    'card_acceptor': CardAcceptor(**ca_kwargs),
                    'sender_account_number': sender_pan,
                    'sender_name': 'Doe Jane',
                    'sender_address': 'Home',
                    'sender_city': 'San Francisco',
                    'sender_country_code': 'USA',
                    'sender_state_code': 'CA',
                    'recipient_pan': recipient_pan,
                    'recipient_name': 'Doe John',
                    'transaction_currency_code': 'USD'
                }

                mpft_kwargs = {
                    'acquiring_bin': 408999,
                    'acquirer_country_code': 840,
                    'business_application_id': 'AA',
                    'request': [
                        PushFundsTransaction(**pft_kwargs)
                    ]
                }

                mpft = MultiPushFundsTransaction(**mpft_kwargs)
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
                'terminal_id': 'TID-9999',
                'id_code': 'CA-IDCode-77765',
                'address': {
                    'country': 'USA',
                    'zip_code': '12345',
                    'state': 'CA'
                }
            }

            ode_kwargs = {
                'stan': 123456,
                'acquiring_bin': 408999,
                'approval_code': '20304B',
                'transmission_datetime': '2017-02-16T12:59:23'
            }

            rft_kwargs = {
                'stan': 123456,
                'acquiring_bin': 408999,
                'acquirer_country_code': 608,
                'ode': OriginalDataElements(**ode_kwargs),
                'card_acceptor': CardAcceptor(**ca_kwargs),
                'sender_pan': sender_pan,
                'sender_currency_code': 'USD',
                'amount': amount,
                'sender_expiration': sender_card_expiry_date,
                'transaction_identifier': transaction_identifier
            }

            rft = ReverseFundsTransaction(**rft_kwargs)

            if is_multi:

                rft_kwargs = {
                    'stan': 123456,
                    'ode': OriginalDataElements(**ode_kwargs),
                    'card_acceptor': CardAcceptor(**ca_kwargs),
                    'sender_pan': sender_pan,
                    'sender_currency_code': 'USD',
                    'amount': amount,
                    'sender_expiration': sender_card_expiry_date,
                    'transaction_identifier': transaction_identifier
                }

                mrft_kwargs = {
                    'acquiring_bin': 408999,
                    'acquirer_country_code': 608,
                    'request': [
                        ReverseFundsTransaction(**rft_kwargs)
                    ]
                }

                mrft = MultiReverseFundsTransaction(**mrft_kwargs)

                result = reversefunds.send(data=mrft, multi=True)

            else:
                result = reversefunds.send(data=rft)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = ReverseFundsFormPost()
        form_get = ReverseFundsFormGet()
        return render(request,
                      template_name='visadirect/fundstransfer/reversefunds.html',
                      context={'form_post': form_post, 'form_get': form_get})
