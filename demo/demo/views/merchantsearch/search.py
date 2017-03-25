from django.shortcuts import render

from pyvdp.merchantsearch.data import MerchantSearchData
from pyvdp.merchantsearch import search

from demo.forms.merchantsearch.search import MerchantSearchFormPost


def merchant_search(request):
    if request.method == 'POST':
        form = MerchantSearchFormPost(request.POST)
        if form.is_valid():
            merchant_name = form.cleaned_data['merchant_name']

            search_attrs = {
                'merchant_name': merchant_name,
                'merchant_street_address': '802 industrial dr',
                'merchant_city': 'Mount Pleasant',
                'merchant_state': 'MI',
                'merchant_postal_code': '48858',
                'merchant_country_code': 840,
                'merchant_phone_number': '19897747123',
                'merchant_url': 'http://www.emc.cmich.edu/',
                'business_registration_id': '386004447',
                'acquirer_card_acceptor_id': '424295031886',
                'acquiring_bin': '476197'
            }

            response_attrs = [
                'GNBANKA'
            ]

            options = {
                'max_records': 5,
                'match_indicators': True,
                'match_score': True,
                'proximity': [merchant_name],
                'wildcards': [merchant_name]
            }

            header = {
                'message_id': 'Request_001',
            }

            data = MerchantSearchData(header=header,
                                      search_attrs=search_attrs,
                                      response_attrs=response_attrs,
                                      options=options)

            result = search.send(data=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = MerchantSearchFormPost()

        return render(request, template_name='merchantsearch/search.html', context={'form_post': form_post})
