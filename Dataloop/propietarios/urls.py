from django.urls import path
from . import views

urlpatterns = [
    path('', views.Propietarios, name='propietarios'),
    path('add_propietario/', views.add_propietario, name='add-propietario'),
    path('consulta_propietario/', views.list_propietario, name='list-propietario'),
    path('det_propietario/<vivienda_id>', views.det_propietario, name='det-propietario'),
    path('busca_propietario/', views.list_propietario, name='find-propietario'),
    path('<int:vivienda_id>', views.Propietario_form, name='mod-propietario'),
    path('del_propietario/<int:vivienda_id>', views.del_propietario, name='del-propietario'),        
]