
# Si no escribe ninguna palabra devuelve None
def primera_letra(palabra):
    """Devuelve la primera letra de una palabra"""
    return palabra[0] if palabra else None 

# Solo ejecuta este bloque si este archivo se está ejecutando directamente, no si se importa como módulo en otro archivo.
if __name__ == "__main__":   
    palabra = input("👉 Escribe una palabra: ")
    if palabra:
        print(f"La primera letra de '{palabra}' es: {primera_letra(palabra)}")
    else:
        print("❗ No escribiste ninguna palabra.")
