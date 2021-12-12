import json
import urllib.parse
import requests
import os

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "4M5DvMCiE9Br6fgGnv4xAUbKsouOV2T4"

while True:

    orig = input("Origen: ").lower()
    if orig == "s":
        break
    
    dest = input("Destino: ").lower()
    if orig == "s":
        break
    
    clear = lambda: os.system('cls')
    clear()

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + url)

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status== 0:
        print(f"Estatus de la API: {str(json_status)}. Se encontró la Ruta.\n")
        print(f'Instrucciones de {orig} a {dest}')
        print(f'Duración aproximada: {str(json_data["route"]["formattedTime"])}.')
        print(f'Kilómetros aproximados: {str(json_data["route"]["distance"]*1.61)} kms.')
        print(f'Combustible aproximado: {str(json_data["route"]["fuelUsed"]*3.78)}')
        print('================== INICIO DE INSTRUCCIONES DE LA RUTA ==============')
        contador = 1
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(f'Paso nº:{str(contador)}: {each["narrative"]} ({str(float(each["distance"])*1.61)} kms.)')
            contador += 1
        print('================== FIN DE INSTRUCCIONES DE LA RUTA =================')
    elif json_status == 402:
        print(f"No se encontró la ruta.")
    else:
        print("Releer la documentación.")