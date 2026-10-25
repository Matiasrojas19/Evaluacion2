import requests
import urllib.parse

ruta_url = "https://graphhopper.com/api/1/route?"
clave = "TU_API_KEY"   # pega aquí tu API key de GraphHopper

SALIR = ("s", "salir")
VEHICULOS = {"auto": "car", "bici": "bike", "a pie": "foot"}


def geocodificar(lugar, clave):
    url = "https://graphhopper.com/api/1/geocode?" + urllib.parse.urlencode(
        {"q": lugar, "limit": "1", "key": clave})
    respuesta = requests.get(url)
    datos = respuesta.json()
    if respuesta.status_code == 200 and len(datos["hits"]) != 0:
        punto = datos["hits"][0]
        return punto["point"]["lat"], punto["point"]["lng"], punto["name"]
    return None


while True:
    print("\n=============================================")
    print("Medios de transporte disponibles: auto, bici, a pie")
    print("Escriba 's' o 'salir' en cualquier momento para terminar")
    print("=============================================")

    medio = input("Ingrese el medio de transporte: ").strip().lower()
    if medio in SALIR:
        print("Programa finalizado.")
        break
    if medio not in VEHICULOS:
        print("Medio no válido, se usará 'auto'.")
        medio = "auto"
    vehiculo = VEHICULOS[medio]

    origen = input("Ingrese el origen: ").strip()
    if origen.lower() in SALIR:
        print("Programa finalizado.")
        break

    destino = input("Ingrese el destino: ").strip()
    if destino.lower() in SALIR:
        print("Programa finalizado.")
        break

    punto_o = geocodificar(origen, clave)
    punto_d = geocodificar(destino, clave)
    if punto_o is None or punto_d is None:
        print("No se pudo encontrar el origen o el destino. Intente de nuevo.")
        continue

    parametros = urllib.parse.urlencode(
        {"key": clave, "vehicle": vehiculo, "locale": "es"})
    url = (ruta_url + parametros
           + "&point=" + f"{punto_o[0]},{punto_o[1]}"
           + "&point=" + f"{punto_d[0]},{punto_d[1]}")

    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        print("Error al consultar la ruta. Código:", respuesta.status_code)
        print(respuesta.text)
        continue

    camino = respuesta.json()["paths"][0]
    km = camino["distance"] / 1000
    millas = km / 1.61
    segundos = camino["time"] / 1000
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    seg = segundos % 60

    print("\n=============================================")
    print(f"Direcciones desde {punto_o[2]} hasta {punto_d[2]} en {medio}")
    print("=============================================")
    print(f"Distancia: {millas:.2f} millas / {km:.2f} km")
    print(f"Duración del viaje: {horas:02d}:{minutos:02d}:{seg:05.2f}")
    print("=============================================")
    for paso in camino["instructions"]:
        print(f"{paso['text']} ( {paso['distance'] / 1000:.2f} km )")
    print("=============================================")