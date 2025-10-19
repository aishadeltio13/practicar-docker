# app.py: pedir un usuario de GitHub y mostrar info usando Requests
import requests

# Pedir al usuario un nombre de usuario de GitHub
usuario = input("Introduce un nombre de usuario de GitHub: ")

url = f"https://api.github.com/users/{usuario}"

try:
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        print(f"\nNombre: {datos.get('name')}")
        print(f"Repositorios públicos: {datos.get('public_repos')}")
        print(f"URL del perfil: {datos.get('html_url')}")
    else:
        print(f"Usuario no encontrado. Código HTTP: {respuesta.status_code}")
except Exception as e:
    print(f"Error al conectarse: {e}")
