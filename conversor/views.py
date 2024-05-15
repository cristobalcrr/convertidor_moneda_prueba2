import json
from django.http import JsonResponse
import bcchapi

def convertir_moneda(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        monto = float(request.POST['monto'])
        moneda_origen = request.POST['moneda_origen']
        moneda_destino = request.POST['moneda_destino']
        
        # Crear el objeto JSON con las credenciales
        credenciales = {
            "usuario": "ccarrasco.1810@gmail.com",
            "contrasena": "Cristobal123lal@"
        }
        credenciales_json = json.dumps(credenciales)
        
        # Crear el objeto bcchapi.Siete con las credenciales
        siete = bcchapi.Siete(file=credenciales_json)
        
        # Realizar la conversión de moneda
        resultado = siete.conversor(moneda_origen, moneda_destino, monto)
        
        # Retornar el resultado como JSON
        return JsonResponse({"resultado": resultado})
    else:
        # Si el método de solicitud no es POST, retornar un error
        return JsonResponse({"error": "Método no permitido"}, status=405)