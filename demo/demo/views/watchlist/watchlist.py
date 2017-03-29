from django.shortcuts import render

from pyvdp.visadirect.watchlist import watchlistinquiry
from pyvdp.visadirect.watchlist import WatchlistData

from demo.forms.watchlist.watchlist import WlInquiryFormPost


def inquiry(request):
    if request.method == 'POST':
        form = WlInquiryFormPost(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            issuer_country_code = form.cleaned_data['issuer_country_code']

            wda_kwargs = {
                'issuer_country_code': issuer_country_code,
                'city': city
            }

            wd_kwargs = {
                'name': name,
                'acquirer_country_code': 840,
                'acquiring_bin': 408999,
                'address': wda_kwargs
            }

            data = WatchlistData(**wd_kwargs)

            result = watchlistinquiry.send(data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = WlInquiryFormPost()
        return render(request, template_name='watchlist/wl_inquiry.html', context={'form_post': form_post})
