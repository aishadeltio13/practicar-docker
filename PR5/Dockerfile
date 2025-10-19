# Construir una Imagen de Docker que contenga una
# aplicación Python que usa la librería Requests para
# obtener información de usuarios de GitHub.  
# Ejecutar la aplicación como un contenedor en tu máquina,
# demostrando que funciona correctamente sin necesidad de
# tener Python ni Requests instalados localmente.
# El contenedor pedirá un nombre de usuario de GitHub
# y mostrará información básica como nombre, repositorios
# públicos y URL del perfil.


# Imagen base de Python
FROM python:3.12-alpine

# Crear directorio de trabajo
WORKDIR /app

# Copiar el archivo de dependencias y la app al contenedor
COPY pip.txt .
COPY app.py .

# Instalar todas las librerías listadas en pip.txt
RUN pip install --no-cache-dir -r pip.txt

# Ejecutar la aplicación al iniciar el contenedor
CMD ["python", "app.py"]

# PASOS:
# docker build -t python-requests-app .
# docker run -it python-requests-app --> ejecutar el contenedor de forma interactiva


