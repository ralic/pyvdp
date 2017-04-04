from django.shortcuts import render

from pyvdp.merchantsearch import search, MerchantSearchData

from demo.forms.merchantsearch.search import MerchantSearchFormPost


def merchant_search(request):
    if request.method == 'POST':
        form = MerchantSearchFormPost(request.POST)
        if form.is_valid():
            merchant_name = form.cleaned_data['merchant_name']

            msal_kwargs = {
                'merchant_name': merchant_name,
                "merchantStreetAddress": "802 industrial dr",
                "merchantCity": "Mount Pleasant",
                "merchantState": "MI",
                "merchantPostalCode": "48858",
                "merchantCountryCode": "840",
                "merchantPhoneNumber": "19897747123",
                "merchantUrl": "http://www.emc.cmich.edu",
                "businessRegistrationId": "386004447",
                "acquirerCardAcceptorId": "424295031886",
                "acquiringBin": "476197",
            }

            mso_kwargs = {
                "maxRecords": "5",
                "matchIndicators": "true",
                "matchScore": "true",
                "proximity": [
                    "merchantName"
                ],
                "wildCard": [
                    "merchantName"
                ]
            }

            ms_kwargs = {
                'header': MerchantSearchData.MerchantSearchHeader(),
                'search_attr_list': MerchantSearchData.MerchantSearchAttrList(**msal_kwargs),
                'response_attr_list': ["GNSTANDARD"],
                'options': MerchantSearchData.MerchantSearchOptions(**mso_kwargs)
            }

            data = MerchantSearchData(**ms_kwargs)

            result = search.send(data=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = MerchantSearchFormPost()

        return render(request, template_name='merchantsearch/search.html', context={'form_post': form_post})
