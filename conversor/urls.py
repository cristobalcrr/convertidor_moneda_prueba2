from django.urls import path
from .views import convertir_moneda

urlpatterns = [
    path('convertir-moneda/', convertir_moneda, name='convertir-moneda'),
]