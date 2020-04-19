from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Tracs
from .forms import TracsForm
from django.shortcuts import redirect

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

def post_new(request):
    if request.method == "POST":
        form = TracsForm(request.POST)
        if form.is_valid():
            trac = form.save(commit=False)
            if trac.payer == "ryosuke" or trac.payer == "mae":
                if trac.payer == "ryosuke":
                    trac.nonpayer = "mae"
                else:
                    trac.nonpayer = "ryosuke"
                trac.date = timezone.now()
                trac.save()
                return redirect('detail')
            else:
                return redirect('post_new')
    else:
        form = TracsForm()
    return render(request, 'warikan/post_edit.html', {'form': form})

def post_edit(request, pk):
    trac = get_object_or_404(Tracs, pk=pk)
    if request.method == "POST":
        form = TracsForm(request.POST, instance=trac)
        if form.is_valid():
            trac = form.save(commit=False)
            if trac.payer == "ryosuke" or trac.payer == "mae":
                if trac.payer == "ryosuke":
                    trac.nonpayer = "mae"
                else:
                    trac.nonpayer = "ryosuke"
                trac.date = timezone.now()
                trac.save()
                return redirect('detail')
            else:
                return redirect('post_new')
    else:
        form = TracsForm(instance=trac)
    return render(request, 'warikan/post_edit.html', {'form': form})
