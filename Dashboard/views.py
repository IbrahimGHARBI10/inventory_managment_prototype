from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from matplotlib.style import context
from .models import product,order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages



@login_required
def index(request):
    orders= order.objects.all()
    products=product.objects.all()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form=OrderForm()
    context={
        'orders':orders,
        'form':form,
        'products':products,
    }
    return render(request,'dashboard/index.html',context)

@login_required
def staff(request):
    workers= User.objects.all()
    workers_count= workers.count()
    context = {
        'workers': workers,
        'workers_count': workers_count
    }
    return render(request,'dashboard/staff.html',context)

@login_required
def staff_details(request,pk):
    workers = User.objects.get(id=pk)
    context={'workers' : workers,}
    return render(request, 'dashboard/staff_detail.html',context)


@login_required
def Product(request):
    items = product.objects.all()
    #items = product.objects.raw('SELECT * FROM dashboard_product')
    
    workers_count1=items.count()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
            
            return redirect('dashboard-product')
    else: 
        form=ProductForm()

    context={
        'items':items,
        'form':form, 
        'workers_count1':workers_count1,
    }
    return render(request,'dashboard/product.html',context)

@login_required
def product_delete(request,pk):
    item=product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request,pk):
    item=product.objects.get(id=pk)
    if request.method=="POST":
        form=ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form=ProductForm(instance=item)

    context={ 
        'form':form,

        }
    return render(request, 'dashboard/product_update.html',context)


@login_required
def Order(request):
    orders= order.objects.all()
    context={
        'orders':orders,
    }
    return render(request,'dashboard/order.html',context)