from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')


def visa_direct(request):
    return render(request, template_name='visadirect/index.html')


def pav(request):
    return render(request, template_name='pav/index.html')


def merchantsearch(request):
    return render(request, template_name='merchantsearch/index.html')


def paai(request):
    return render(request, template_name='paai/index.html')


def dcas(request):
    return render(request, template_name='dcas/index.html')