import requests

def precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    return data

def guardar_txt(data):
    with open("preciobitcoin.txt", "w") as archivo:
        archivo.write(str(data))

def guardar_csv(data):
    with open("preciobitcoin.csv", "w", newline="") as archivo:
        archivo.write("Moneda,Precio\n")
        
        for moneda, info in data["bpi"].items():
            archivo.write(f"{moneda},{info['rate']}\n")

def main():
    data = precio_bitcoin()

    guardar_txt(data)
    print("Datos guardados en precio_bitcoin.txt")

    guardar_csv(data)
    print("Datos guardados en precio_bitcoin.csv")

if __name__ == "__main__":
    main()
