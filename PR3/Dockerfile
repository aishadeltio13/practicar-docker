# Ejecutar un contenedor que termina con error, inspeccionar docker ps-a, 
# docker logs, y forzar eliminación

# FORMA 1:
# # Usar la imagen oficial de Python
# FROM python:3.12-alpine

# # Copiar el script al contenedor
# # Toma el archivo crash.py que está en el mismo directorio que tu Dockerfile.
# # Lo copia directamente a la raíz del contenedor como /crash.py.
# COPY crash.py /crash.py

# # Ejecutar el script al iniciar el contenedor
# CMD ["python", "/crash.py"]

# FORMA 2:
FROM python:3.12-alpine
# todo lo que copio va a /app
WORKDIR /app 
COPY . .
# Ejecutar crash.py desde /app
CMD ["python", "crash.py"]


# PASOS:

# # Construir la imagen
# docker build -t contenedor-crash .

# # Ejecutar el contenedor (fallará)
# docker run --name crash contenedor-crash

# # Ver contenedores (incluidos los que terminaron)
# docker ps -a

# # Ver logs para ver el error
# docker logs crash

# # Eliminar el contenedor forzadamente
# docker rm -f crash

