import os
import stat
import getpass

# Leer usuario y contraseña admin desde variables de entorno
admin_user = os.getenv("ADMIN_USER", "admin")
admin_pass = os.getenv("ADMIN_PASS", "admin123")

# Pedir usuario
current_user = input("Usuario: ")

# Comprobar si es admin
if current_user != admin_user:
    print(f"❌ Acceso denegado para usuario {current_user}. Solo admin puede entrar.")
    exit(1)

# Si es admin, pedir contraseña
password = getpass.getpass("Contraseña: ")
if password != admin_pass:
    print("❌ Contraseña incorrecta")
    exit(1)

print(f"✅ Bienvenido {current_user}, tienes permisos completos.\n")

# Función para mostrar permisos
def mostrar_permisos(path):
    try:
        st = os.stat(path)
        permisos = stat.filemode(st.st_mode)
        propietario = st.st_uid
        grupo = st.st_gid
        print(f"{path}: {permisos} (UID:{st.st_uid}, GID:{st.st_gid})")
    except FileNotFoundError:
        print(f"{path}: no existe")

# Archivos a inspeccionar
archivos = ["main.py"]
for archivo in archivos:
    mostrar_permisos(archivo)
