from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')


def visa_direct(request):
    return render(request, template_name='visadirect/index.html')


def pav(request):
    return render(request, template_name='pav/index.html')


def merchantsearch(request):
    return render(request, template_name='merchantsearch/index.html')


def watchlist(request):
    return render(request, template_name='watchlist/index.html')


def paai(request):
    return render(request, template_name='paai/index.html')
