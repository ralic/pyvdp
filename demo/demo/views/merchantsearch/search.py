from django.shortcuts import render

from pyvdp.merchantsearch import search, SearchModel

from demo.forms.merchantsearch.search import MerchantSearchFormPost


def merchant_search(request):
    if request.method == 'POST':
        form = MerchantSearchFormPost(request.POST)
        if form.is_valid():
            merchant_name = form.cleaned_data['merchant_name']

            msal_kwargs = {
                'merchantName': merchant_name,
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
                'header': SearchModel.MerchantSearchHeader(),
                'searchAttrList': SearchModel.MerchantSearchAttrList(**msal_kwargs),
                'responseAttrList': ["GNSTANDARD"],
                'searchOptions': SearchModel.MerchantSearchOptions(**mso_kwargs)
            }

            data = SearchModel(**ms_kwargs)

            result = search.send(data=data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = MerchantSearchFormPost()

        return render(request, template_name='merchantsearch/search.html', context={'form_post': form_post})
