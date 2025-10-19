# Crear una imagen que sirva una página estática y mantener el 
# contenedor en ejecución mapeando puertos

# Usar la imagen base de Nginx (servidor web ligero)
FROM nginx:alpine

# Copiar el archivo HTML al directorio que Nginx sirve por defecto
COPY . /usr/share/nginx/html

# Exponer el puerto 80 (por donde se servirá la página)
EXPOSE 80


# PASOS: 

# # Construir la imagen (nombre: mi-servidor)
# docker build -t mi-servidor .

# # Ejecutar el contenedor en segundo plano (-d) mapeando el puerto 8080 del host al 80 del contenedor
# docker run -d -p 8080:80 mi-servidor

# http://localhost:8080/index_estatico.html
