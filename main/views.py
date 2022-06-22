from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests


# Create your views here.
def index(request):
    my_date, my_agen = '', ''
    if request.method == 'GET':
        if request.GET.get('your_date'):
            my_date = request.GET['your_date']
            my_date = my_date.split('-')
            my_date = f'{my_date[0]}/{my_date[1]}/{my_date[2]}/'
        if request.GET.get('your_agen'):
            my_agen = request.GET['your_agen']
            my_agen = f'{my_agen}/'

    res = requests.get('http://127.0.0.1:8000/api/' + my_date + my_agen)

    try:
        cus_list = list(res.json()['customers'].values())
        agencies = res.json()['agencies']
    except:
        agencies = []
        keys = ('customerName', 'contactLastName', 'contactFirstName', 'lastOrderDate', 'numOrders', 'Agency', 'phone',
                'addressLine', 'city', 'country')
        cus_list = list(dict(zip(keys, 10*['connection error'])))
    page = request.GET.get('page', 1)
    paginator = Paginator(cus_list, 10)

    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    context = {'customers': customers,
               'agencies': agencies}

    return render(request, "index.html", {'context': context})
