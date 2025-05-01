import requests
import json

# Cargar datos desde archivo
with open('datos.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Obtener todos los documentos
lista_datos = data['docs']

# Nombre de la base de datos en CouchDB
base_datos = "personas006"
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar documentos uno por uno
for doc in lista_datos:
    response = requests.post(url, headers=headers, json=doc)
    nombre = doc.get('nombre', 'Desconocido')
    print(f"Insertando {nombre} | {response.status_code}")
