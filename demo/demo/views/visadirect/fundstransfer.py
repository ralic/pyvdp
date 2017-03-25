from django.shortcuts import render

from demo.forms.visadirect.fundstransfer import (PullFundsFormGet, PullFundsFormPost, PushFundsFormGet,
                                                 PushFundsFormPost, ReverseFundsFormGet, ReverseFundsFormPost)

from pyvdp.visadirect.data import CardAcceptor
from pyvdp.visadirect.data import OriginalDataElements

from pyvdp.visadirect.fundstransfer.data import PullFundsTransaction, MultiPullFundsTransaction
from pyvdp.visadirect.fundstransfer.data import PushFundsTransaction, MultiPushFundsTransaction
from pyvdp.visadirect.fundstransfer.data import ReverseFundsTransaction, MultiReverseFundsTransaction

from pyvdp.visadirect.fundstransfer import push_funds, pull_funds, reverse_funds

def index(request):
    return render(request, template_name='visadirect/fundstransfer/index.html')

def pullfunds(request):
    if request.method == 'POST':
        result = {}
        if request.POST['action'] == 'post':
            form = PullFundsFormPost(request.POST)
            if form.is_valid():
                sender_pan = form.cleaned_data['sender_pan']
                sender_expiry_date = form.cleaned_data['sender_expiry_date']
                amount = form.cleaned_data['amount']
                is_multi = form.cleaned_data['is_multi']

                card_acceptor = CardAcceptor(name='Acceptor 1',
                                             address={
                                                 'country': 'USA',
                                                 'zip_code': '12345',
                                                 'state': 'CA'
                                             },
                                             terminal_id='TID-9999',
                                             id_code='CA-IDCode-77765')

                data = PullFundsTransaction(stan=123456,
                                            amount=amount,
                                            sender_pan=sender_pan,
                                            sender_card_expiry_date=sender_expiry_date,
                                            sender_currency_code='USD',
                                            card_acceptor=card_acceptor)

                if is_multi:
                    # FIXME multi should not be an argument for PFT
                    data = PullFundsTransaction(multi=True,
                                                stan=123456,
                                                amount=amount,
                                                sender_pan=sender_pan,
                                                sender_card_expiry_date=sender_expiry_date,
                                                sender_currency_code='USD',
                                                card_acceptor=card_acceptor)

                    pfts = [data]
                    mpft = MultiPullFundsTransaction(transactions=pfts)
                    result = pull_funds.send(transaction=mpft, multi=True)
                else:
                    result = pull_funds.send(transaction=data)
        else:
                form = PullFundsFormGet(request.POST)
                if form.is_valid():
                    status_id = form.cleaned_data['status_id']
                    result = pull_funds.get(status_id=status_id, multi=True)

        return render(request, template_name='success.html', context={'result': result})

    else:
        form_post = PullFundsFormPost()
        form_get = PullFundsFormGet()
        return render(request,
                      template_name='visadirect/fundstransfer/pullfunds.html',
                      context={'form_get': form_get, 'form_post': form_post})

def pushfunds(request):
    if request.method == 'POST':
        form = PushFundsFormPost(request.POST)
        if form.is_valid():
            sender_pan = form.cleaned_data['sender_pan']
            recipient_pan = form.cleaned_data['recipient_pan']
            amount = form.cleaned_data['amount']
            is_multi = form.cleaned_data['is_multi']

            card_acceptor = CardAcceptor(name='Acceptor 1',
                                         terminal_id='TID-9999',
                                         address={
                                             'country': 'USA',
                                             'zip_code': '12345',
                                             'state': 'CA'
                                         },
                                         id_code='CA-IDCode-77765')

            data = PushFundsTransaction(stan=123456,
                                        amount=amount,
                                        transaction_currency_code='USD',
                                        card_acceptor=card_acceptor,
                                        sender_pan=sender_pan,
                                        recipient_pan=recipient_pan,
                                        recipient_name='Test')

            if is_multi:
                data = PushFundsTransaction(multi=True,
                                            stan=123456,
                                            amount=amount,
                                            transaction_currency_code='USD',
                                            card_acceptor=card_acceptor,
                                            sender_pan=sender_pan,
                                            sender_name='John',
                                            sender_address='Home',
                                            sender_city='San Francisco',
                                            sender_country_code='USA',
                                            sender_state_code='CA',
                                            recipient_pan=recipient_pan,
                                            recipient_name='Test')
                pfts = [data]
                mpft = MultiPushFundsTransaction(transactions=pfts)
                result = push_funds.send(transaction=mpft, multi=True)
            else:
                result = push_funds.send(transaction=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = PushFundsFormPost()
        form_get = PushFundsFormGet()
        return render(request,
                      template_name='visadirect/fundstransfer/pushfunds.html',
                      context={'form_post': form_post, 'form_get': form_get})

def reversefunds(request):
    if request.method == 'POST':
        form = ReverseFundsFormPost(request.POST)
        if form.is_valid():
            sender_pan = form.cleaned_data['sender_pan']
            sender_card_expiry_date = form.cleaned_data['sender_card_expiry_date']
            transaction_identifier = form.cleaned_data['transaction_identifier']
            amount = form.cleaned_data['amount']
            is_multi = form.cleaned_data['is_multi']

            card_acceptor = CardAcceptor(name='Acceptor 1',
                                         terminal_id='TID-9999',
                                         id_code='CA-IDCode-77765',
                                         address={
                                             'country': 'USA',
                                             'zip_code': '12345',
                                             'state': 'CA'
                                         })

            ode = OriginalDataElements(stan=123456,
                                       approval_code='20304B',
                                       transmission_datetime='2017-02-16T12:59:26')

            data = ReverseFundsTransaction(stan=123456,
                                           ode=ode,
                                           sender_pan=sender_pan,
                                           sender_currency_code='USD',
                                           amount=amount,
                                           sender_card_expiry_date=sender_card_expiry_date,
                                           transaction_identifier=transaction_identifier,
                                           card_acceptor=card_acceptor)

            if is_multi:
                data = ReverseFundsTransaction(multi=True,
                                               stan=123456,
                                               ode=ode,
                                               sender_pan=sender_pan,
                                               sender_currency_code='USD',
                                               amount=amount,
                                               sender_card_expiry_date=sender_card_expiry_date,
                                               transaction_identifier=transaction_identifier,
                                               card_acceptor=card_acceptor)
                rfts = [data]
                mrft = MultiReverseFundsTransaction(transactions=rfts)
                result = reverse_funds.send(transaction=mrft, multi=True)
            else:
                result = reverse_funds.send(transaction=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = ReverseFundsFormPost()
        form_get = ReverseFundsFormGet()
        return render(request,
                      template_name='visadirect/fundstransfer/reversefunds.html',
                      context={'form_post': form_post, 'form_get': form_get})
