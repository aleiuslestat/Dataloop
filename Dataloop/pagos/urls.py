from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_pago, name='home-pago'),
    path('aplicar_pago/', views.add_pago, name='aplicar-pago'),
    path('find_pagos/', views.find_pagos, name='find-pagos'),
    path('<int:pago_id>', views.pago_form, name='mod-pago'),
    path('del_propietario/<int:pago_id>', views.del_pago, name='del-pago'),  
]