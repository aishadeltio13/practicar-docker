# Entender la diferencia entre ENTRYPOINT y CMD y cómo docker run 
# puede sobreescribir comandos.

# Usar imagen base ligera de Alpine
FROM alpine:latest

# creamos y cambiamos al directorio /app dentro del contenedor
WORKDIR /app

# copiamos nuestro script dentro de /app
COPY . .

# Dar permisos de ejecución al script
RUN chmod +x script.sh

# ENTRYPOINT define el comando principal que siempre se ejecuta.
# le decimos a Docker que ejecute el script que está en el directorio actual (/app).
ENTRYPOINT ["./script.sh"]

# CMD define los argumentos por defecto (pueden ser sobreescritos)
CMD ["arg1", "arg2"]


# PASOS:

# docker build -t entrypoint-cmd .
# docker run entrypoint-cmd → ejecuta ./script.sh arg1 arg2
# docker run entrypoint-cmd hola mundo → ejecuta ./script.sh hola mundo
# docker run --entrypoint /bin/sh entrypoint-cmd -c "echo test" → reemplaza ENTRYPOINT por /bin/sh
