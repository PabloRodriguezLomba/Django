from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ClienteForm
from .models import Cliente
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
