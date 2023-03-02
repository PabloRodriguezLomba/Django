from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cli'),
    path('cliente/new', views.cliente_new, name='cliente_new'),
    path('Productos',views.productos,name='Productos'),
    path('cliente/baja',views.cliente_baja,name='cliente_baja'),
    path('Pedidos',views.Pedidos,name='Pedidos'),
    path('Clientes',views.clientes_list,name='clientes_list'),
    path('About',views.About,name='About'),
    path('Productos/details',views.product_detail,name='product_detail')

]

