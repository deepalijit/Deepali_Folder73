from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProdcutModelForm


# Create your views here.
@login_required(login_url='signin')
def addProductView(request):
    form = ProdcutModelForm()
    if request.method == 'POST':
        form = ProdcutModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-products')
    template_name = 'InventoryManagement/addProduct.html'
    context = {'form':form}
    return render(request,template_name,context)

def showProductsView(request):
    products=Product.objects.all()
    template_name = 'InventoryManagement/showProduct.html'
    context={'products':products}
    return render(request,template_name,context)

def updateProductView(request,id):
    obj = Product.objects.get(id=id)
    form = ProdcutModelForm(instance=obj)
    if request.method == 'POST':
        form = ProdcutModelForm(request.POST,instance=obj)
        form.save()
        return redirect('show-products')
    template_name='InventoryManagement/addProduct.html'
    context = {'form':form }
    return render(request, template_name, context)

def deleteProductView(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('show-products')