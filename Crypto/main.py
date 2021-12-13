import requests

if __name__ == '__main__':
    freno = 0
    endpoint = 'https://criptoya.com/api/argenbtc'
    peticion = requests.get(endpoint)
    if peticion.status_code == 200:
        while freno==0:
            peticion = requests.get(endpoint)
            orden = input("¿Consultar cotización del bitcoin? [Y/N]").lower()
            if orden=='y':
                archivo_json = peticion.json()
                precio_compra_sin_comision = archivo_json['ask']
                precio_compra_final = archivo_json['totalAsk']
                precio_venta_sin_comision = archivo_json['bid']
                precio_venta_final = archivo_json['totalBid']
                timestamp = archivo_json['time']
                print(f"""El precio de compra final es de USD{precio_compra_final}.""")
            elif (orden != 'y') and (orden!='n'):
                print("Opción no válida.")
            else:
                freno=1
                print("Tenga un buen día =).")
    else:
        print("No hay conexión!!!") 