from django.shortcuts import render,redirect,get_object_or_404
from.models import Product
from .forms import ProductForm
from django.db import models
# Create your views here.

def home(request):
    return render(request,'products/product.html')

def product_list(request):
    products=Product.objects.all()

    search = request.GET.get('search', '')
    stock_filter = request.GET.get('stock', '')

    if search:
     products = products.filter(name__icontains=search)
    

    if stock_filter == 'low':
        products = products.filter(
            quantity__lte=models.F('low_stock_threshold')
        )

    return render(request, 'products/product.html', {
        'products': products,
        'search': search,
        'stock_filter': stock_filter,
    })
    

def product_create(request):
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form .is_valid():
            form.save()
            return redirect("product_list")
    else:
        form=ProductForm()
    return render(request,'products/product_form.html',{"form":form})


def product_update(request,id):
    product=get_object_or_404(Product,id=id)
    if request.method=="POST":
                form=ProductForm(request.POST,instance=product)
                if form .is_valid():
                    form.save()
                    return redirect("product_list")
    else:
                form=ProductForm(instance=product)
    return render(request,'products/product_form.html',{"form":form,
    'product':product                                                    })


def product_delete(request,id):
       product=get_object_or_404(Product,id=id)
       if request.method=="POST":
             product.delete()
             return redirect('product_list')
       return render (request,'products/product_delete.html',{'product':product})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, 'products/product_detail.html', {
        'product': product
    })



