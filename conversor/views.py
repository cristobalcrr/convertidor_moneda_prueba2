import json
from django.http import JsonResponse
import bcchapi

def convertir_moneda(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        monto = float(request.POST['monto'])
        moneda_origen = request.POST['moneda_origen']
        moneda_destino = request.POST['moneda_destino']
        
        # Verificar si la moneda origen es CLP y la destino es USD
        if moneda_origen == 'CLP' and moneda_destino == 'USD':
            # Crear el objeto JSON con las credenciales
            credenciales = {
                "usuario": "ccarrasco.1810@gmail.com",
                "contrasena": "Cristobal123lal@"
            }
            credenciales_json = json.dumps(credenciales)
            
            # Crear el objeto bcchapi.Siete con las credenciales
            siete = bcchapi.Siete(file=credenciales_json)
            
            # Obtener el tipo de cambio CLP a USD
            tipo_cambio_clp_usd = siete.ultimo_valor("dolar", "peso", "dolar")
            
            # Calcular el monto en USD
            monto_usd = monto / tipo_cambio_clp_usd
            
            # Retornar el resultado como JSON
            return JsonResponse({"resultado": monto_usd})
        else:
            return JsonResponse({"error": "Conversión no soportada"}, status=400)
    else:
        # Si el método de solicitud no es POST, retornar un error
        return JsonResponse({"error": "Método no permitido"}, status=405)
