from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ClienteForm, BajaForm
from .models import Cliente, Product
from django.utils import timezone
# Create your views here.
def clientes_list(request):
    clientes = Cliente.objects.filter(alta__lte=timezone.now()).order_by('alta')

    return render(request, 'misitio/clientes_list.html', {'clientes': clientes})
def cliente_new(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
    else:
        form = ClienteForm()
    return render(request, 'misitio/clientes_edit.html', {'form': form})
def productos(request):
    return render(request,'misitio/Productos.html')
def Pedidos(request):
    return render(request,'misitio/Productos.html')
def cliente_baja(request):
    if request.method == 'POST':
        form = BajaForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
    else:
        form = BajaForm()
    return render(request,'misitio/clientes_baja.html',{'form': form})

def home(request):
    return render(request,'misitio/home.html')

def About(request):
    return render(request,'misitio/About.html')

def product_detail(request):
    print(request.GET.get("producto"))
    producto = Product.objects.filter(nombre=request.GET.get("producto"))

    return render(request,'misitio/ProductDetail.html',{'producto':producto})

def purchase(cuantity,name):
    producto = Product.objects.filter(nombre=name).update(stock=cuantity+1)

def Sale(cuantity,name):
    producto = Product.objects.filter(nombre=name).update(stock=cuantity-1)






