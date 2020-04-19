from django.shortcuts import render
from .models import Tracs

# Create your views here.

def post_list(request):
    tracs = Tracs.objects.order_by('amount')
    ryopay = 0
    maepay = 0
    for trac in tracs:
        if trac.payer == "ryosuke":
            ryopay = ryopay + trac.amount
        else:
            maepay = maepay + trac.amount

    if maepay > ryopay:
        paying = "ryosuke"
        amount = (maepay - ryopay)/2
    else:
        paying = "mae"
        amount = (ryopay - maepay)/2

    return render(request, 'warikan/post_list.html', {'paying':paying, 'amount':amount})

def detail(request):
    tracs = Tracs.objects.order_by('date')
    return render(request, 'warikan/detail.html', {'tracs':tracs})
