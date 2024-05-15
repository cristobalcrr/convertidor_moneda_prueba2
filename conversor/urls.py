from django.urls import path
from .views import convertir_moneda_post, convertir_moneda_get

urlpatterns = [
    path('convertir-moneda/', convertir_moneda_post, name='convertir-moneda-post'),
    path('convertir-moneda/', convertir_moneda_get, name='convertir-moneda-get'),
]