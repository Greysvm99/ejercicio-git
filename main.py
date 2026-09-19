# importar libreria
import requests

# Crear la funcion
def consultar_api(url):
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos

#Api Publica
url = "https://jsonplaceholder.typicode.com/todos/1"

resultado = consultar_api(url)

print(resultado)

#Comrpobar que es un diccionario
print(type(resultado))