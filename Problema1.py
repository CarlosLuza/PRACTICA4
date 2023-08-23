import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  
        data = response.json()
        bitcoin_precio = data["bpi"]["USD"]["rate_float"]
        return bitcoin_precio
    except requests.RequestException as e:
        print("Error", e)
        return None
    except KeyError:
        print("Error")
        return None
def main():
    try:
        cant_bitcoins = float(input("Ingrese la cantidad de Bitcoins que posee: "))
        if cant_bitcoins < 0:
            print("La cantidad de Bitcoins debe ser mayor a 0.")
            return

        bitcoin_price = get_bitcoin_price()
        if bitcoin_price is not None:
            total_cost_usd = cant_bitcoins * bitcoin_price
            print(f"Costo actual de {cant_bitcoins:.8f} Bitcoins: ${total_cost_usd:,.4f}")
        else:
            print("No se pudo obtener el precio de Bitcoin.")

    except ValueError:
        print("Ingrese un numero valido: ")

if __name__ == "__main__":
    main()
