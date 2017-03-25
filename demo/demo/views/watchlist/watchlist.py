from django.shortcuts import render

from pyvdp.visadirect.watchlist import watchlistinquiry
from pyvdp.visadirect.watchlist.data import WatchlistObject

from demo.forms.watchlist.watchlist import WlInquiryFormPost


def inquiry(request):
    if request.method == 'POST':
        form = WlInquiryFormPost(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            issuer_country_code = form.cleaned_data['issuer_country_code']

            data = WatchlistObject(name=name,
                                   city=city,
                                   issuer_country_code=issuer_country_code)

            result = watchlistinquiry.send(data)

            return render(request, template_name='success.html', context={'result': result})
    else:
        form_post = WlInquiryFormPost()
        return render(request, template_name='watchlist/wl_inquiry.html', context={'form_post': form_post})
