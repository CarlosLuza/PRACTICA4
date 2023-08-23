import requests
import sqlite3


url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
respuesta = requests.get(url)
datos = respuesta.json()
precios_bitcoin = datos['bpi']


precio_usd = precios_bitcoin['USD']['rate']
precio_gbp = precios_bitcoin['GBP']['rate']
precio_eur = precios_bitcoin['EUR']['rate']

fecha_estatica = '2023-08-23 12:00:00'

info_bitcoin = (precio_usd, precio_gbp, precio_eur, fecha_estatica)


with sqlite3.connect('cryptos.db') as conexion:
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bitcoin (
            id INTEGER PRIMARY KEY,
            precio_usd TEXT,
            precio_gbp TEXT,
            precio_eur TEXT,
            fecha DATETIME
        )
    ''')

 
    cursor.execute('INSERT INTO bitcoin (precio_usd, precio_gbp, precio_eur, fecha) VALUES (?, ?, ?, ?)', info_bitcoin)

 
    conexion.commit()

print("Los precios de Bitcoin se han almacenado en la base de datos 'cryptos.db'.")
