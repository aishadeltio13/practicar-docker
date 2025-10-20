import numpy as np      # Librería para operaciones numéricas con arrays
import pandas as pd     # Librería para manipulación de datos
import matplotlib.pyplot as plt  # Librería para gráficos
import os               # Para leer variables de entorno

# Función que crea un array de números enteros aleatorios entre 0 y un máximo
def crear_array(tamano, max_val):
    return np.random.randint(0, max_val + 1, tamano)
# El tamaño se lo preguntamos al usuario 'n' y el max_val esta definido en enviroment (es una variable de entorno)

if __name__ == "__main__":
    # Leer tamaño del array desde input del usuario
    try:
        n = int(input("👉 Ingresa el tamaño de los arrays: "))
    except ValueError:
        print("❌ Por favor ingresa un número entero válido.")
        exit(1)

    # Leer variable de entorno ARRAY_MAX, con valor por defecto 100. Si no se indica en enviroment, se queda en 100.
    max_val = int(os.getenv("ARRAY_MAX", 100))
    # Leer variable de entorno USER_NAME, con valor por defecto Usuario. Si no se indica en enviroment, se queda en Usuario.
    user_name = os.getenv("USER_NAME", "Usuario") 

    # Crear arrays usando numpy
    arr1 = crear_array(n, max_val)
    arr2 = crear_array(n, max_val)
    suma = arr1 + arr2

    # Convertir los arrays a un DataFrame de pandas para mostrar datos de forma ordenada
    df = pd.DataFrame({"Array1": arr1, "Array2": arr2, "Suma": suma})
    print(f"\n=== RESULTADOS para {user_name} ===")
    print(df)

    # Graficar la suma 
    plt.bar(range(n), suma)
    plt.title(f"Suma de Array1 + Array2 para {user_name}")
    plt.show()
