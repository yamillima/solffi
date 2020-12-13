from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inversionistas/', views.inversionistas, name='inversionistas'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
]
