import os
import stat

user = os.getenv("USER", "usuario")
print(f"\nHola {user}, este contenedor se ejecuta con tus permisos actuales.\n")

# Función para mostrar permisos de un archivo o directorio
def mostrar_permisos(path):
    st = os.stat(path)
    permisos = stat.filemode(st.st_mode)
    propietario = st.st_uid
    grupo = st.st_gid
    print(f"{path}: {permisos} (UID:{propietario}, GID:{grupo})")

# Mostrar permisos de los archivos principales del proyecto
archivos = ["main.py", "docker-compose.yaml", "users.txt"]
for archivo in archivos:
    if os.path.exists(archivo):
        mostrar_permisos(archivo)
    else:
        print(f"{archivo}: no existe todavía")

