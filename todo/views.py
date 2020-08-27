from django.shortcuts import render,redirect
from .models import List
from django.contrib import messages
from .forms import ListForm

# Create your views here.

def home(request):
    if request.method =='POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request,('Item has been added to list'))
            return render(request,"home.html",{'all_items':all_items})

    else:
        all_items = List.objects.all()
        return render(request,"home.html",{'all_items':all_items})


def delete(request,list_id):
    item_todelete = List.objects.get(id=list_id)
    item_todelete.delete()
    messages.success(request,('item has been Deleted'))
    return redirect('home')


def cross_off(request,list_id):
    item_tocross = List.objects.get(id=list_id)
    item_tocross.completed = True
    item_tocross.save()
    return redirect('home')


def uncross(request,list_id):
    uncross = List.objects.get(id=list_id)
    uncross.completed = False
    uncross.save()
    return redirect('home')


def edit(request,list_id):
    if request.method == 'POST':
        item = List.objects.get(id=list_id)
        form = ListForm(request.POST or None,instance=item)
        if form.is_valid:
            form.save()
            item = List.objects.all()
            messages.success(request,'item has been edited')
            return redirect('home')

    else:
        item = List.objects.get(id=list_id)
        return render(request,'edit.html',{'item':item})
