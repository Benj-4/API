import requests
import json
import urllib.parse


main_url = "https://www.mapquestapi.com/directions/v2/route"
key = "GDtO0mvcEdVXkmVp3uOJFb9CjjCyP05S"

while True:
    start = input("Ingrese la ciudad de inicio ('S' para salir): ").upper()
    if start == 'S':
        break
    final = input("Ingrese la ciudad de destino: ")
    params = {
        'key': key,
        'from': start,
        'to': final,
        'locale': 'es_ES'
    }
    query_string = urllib.parse.urlencode(params)
    url = f"{main_url}?{query_string}"
    json_data = requests.get(url).json()
    km = json_data['route']['distance'] * 1.60934
    segundos = json_data['route']['time']
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60

    print(f'Distancia: {km:.1f} km')
    print(f'Duración del viaje: {horas:.0f} horas, {minutos:.0f} minutos, {segundos:.0f} segundos')

    # Salida con la narrativa del viaje en español
    print("Narrativa del viaje:")
    for leg in json_data['route']['legs']:
        for maneuver in leg['maneuvers']:
            narrative = maneuver.get('narrative', '')
            direction = maneuver.get('direction', '')
            streets = maneuver.get('streets', [])
            street = streets[0] if len(streets) > 0 else ''
            print(f"{narrative} (Siga {direction} hacia {street})")
