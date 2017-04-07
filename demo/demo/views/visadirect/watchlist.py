from django.shortcuts import render

from pyvdp.visadirect.watchlist import watchlistinquiry, WatchlistDataModel

from demo.forms.watchlist.watchlist import WlInquiryFormPost


def index(request):
    return render(request, template_name='visadirect/watchlist/index.html')


def inquiry(request):
    if request.method == 'POST':
        form = WlInquiryFormPost(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            issuer_country_code = form.cleaned_data['issuer_country_code']

            wda_kwargs = {
                'issuerCountryCode': issuer_country_code,
                'city': city
            }

            wd_kwargs = {
                'name': name,
                'acquirerCountryCode': 840,
                'acquiringBin': 408999,
                'address': wda_kwargs
            }

            data = WatchlistDataModel(**wd_kwargs)

            result = watchlistinquiry.send(data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = WlInquiryFormPost()
        return render(request, template_name='visadirect/watchlist/wl_inquiry.html', context={'form_post': form_post})
