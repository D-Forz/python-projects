# JSON: Javascript Object Notation

#https://pokeapi.co/api/v2/pokemon/charizard
#https://www.globalmentoring.com.mx/api/personas.json

# Leer archivo json
# json = JavaScript Object Notation
import urllib.request
import json

# Debido a cambios en la libreria ahora se deben pasar algunos cabeceros html
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/api/personas.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
    }
)
respuesta = urllib.request.urlopen(peticion)
print(respuesta)
cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)
# Procesamos la respuesta json
json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
print(json_respuesta)
# Imprimimos sólo los nombres de las personas
# json se convierte a listas y diccionarios de python
print('Nombres de las personas en el archivo json:')
for persona in json_respuesta['personas']:
    print(persona['nombre'], persona['edad'])
# Accedemos al total de personas de archivo
print(f'Total de personas: {json_respuesta["total"]}')
# Accedemos al mensaje del archivo
print(f'Mensaje: {json_respuesta["mensaje"]}')
