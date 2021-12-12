import requests

def lista():
    freno = 0
    args={'offset':0}
    contador = 1
    while freno == 0:
        opcion = input("Imprimimos pokemones? [Y/N]").lower()
        if opcion == 'y':
            url = 'https://pokeapi.co/api/v2/pokemon-form'
            args['offset'] += 20
            response = requests.get(url, params=args)
            if response.status_code == 200:
                payload = response.json()
                results = payload.get('results', [])
                if results:
                    for pokemon in results:
                        name = pokemon['name']
                        print(f"Pokemon nº {contador}: {name}")
                        contador += 1
        elif (opcion != 'y') and (opcion != 'n'):
            print("Ingrese una tecla válida.")
        else:
            freno = 1

if __name__ == '__main__':
    lista()
