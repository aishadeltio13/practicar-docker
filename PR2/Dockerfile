# Practicar bind mounts para que cambios en el host se reflejen en el 
# contenedor.

# Usar la imagen base de Nginx (servidor web ligero)
FROM nginx:alpine

# Exponer el puerto 80 (por donde se servirá la página)
EXPOSE 80

# PASOS: 

# # Construir la imagen
# docker build -t servidor-bind .

# # Ejecutar el contenedor con bind mount
# # -v <host>:<contenedor> , importante usar la terminal powershell y las comillas (nuestra ruta tiene espacios)
# docker run -d -p 8080:80 -v "${PWD}\site:/usr/share/nginx/html" servidor-bind

# http://localhost:8080/index_volumen.html