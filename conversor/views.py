import json
from django.http import JsonResponse
import bcchapi

# Vista para manejar la solicitud POST
def convertir_moneda_post(request):
    if request.method == 'POST':
        # Obtener los datos del formulario POST
        monto_clp = float(request.POST.get('monto_clp', 0))

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
        monto_usd = monto_clp / tipo_cambio_clp_usd
        
        # Almacenar el resultado en la sesión
        request.session['resultado'] = monto_usd
        
        # Retornar el resultado como JSON
        return JsonResponse({"resultado": monto_usd})
    else:
        # Si el método de solicitud no es POST, retornar un error
        return JsonResponse({"error": "Método no permitido"}, status=405)

# Vista para manejar la solicitud GET
def convertir_moneda_get(request):
    if request.method == 'GET':
        # Obtener el resultado de la conversión almacenado en la sesión
        resultado = request.session.get('resultado', None)
        
        # Verificar si hay un resultado almacenado
        if resultado is not None:
            # Retornar el resultado como JSON
            return JsonResponse({"resultado": resultado})
        else:
            return JsonResponse({"error": "No hay resultado disponible"}, status=400)
    else:
        # Si el método de solicitud no es GET, retornar un error
        return JsonResponse({"error": "Método no permitido"}, status=405)
