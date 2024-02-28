import os
import MTO

def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def main():
    # Solicitar al usuario que elija entre encriptar o desencriptar
    opcion = input("¿Desea encriptar (E) o desencriptar (D) un mensaje? ").upper()

    # Validar la opción ingresada
    if opcion not in ["E", "D"]:
        print("Opción no válida. Por favor, ingrese 'E' para encriptar o 'D' para desencriptar.")
        exit()

    # Realizar la operación seleccionada por el usuario
    if opcion == "E":
        mensaje = input("Ingrese el mensaje: ")
        clave = obtener_entero("Ingrese la clave (número entero): ")
        mi_motor = MTO.MotorEncriptacion(clave)
        mensaje_encriptado = mi_motor.encriptar(mensaje)
        print("Mensaje encriptado:", mensaje_encriptado)
        
        with open("mensaje_encriptado.txt", "w", encoding="utf-8") as archivo:
            archivo.write(f"Mensaje encriptado: {mensaje_encriptado}\n")
            archivo.write(f"Clave: {clave}\n")
        
        print("Mensaje encriptado y clave guardados en 'mensaje_encriptado.txt'.")
        
    elif opcion == "D":
        clave_ingresada = obtener_entero("Ingrese la clave para desencriptar (número entero): ")
        
        try:
            with open("mensaje_encriptado.txt", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                clave_almacenada = int(lineas[1].split(":")[1].strip())
        except FileNotFoundError:
            print("No se encontró el archivo 'mensaje_encriptado.txt'.")
            exit()
        except (ValueError, IndexError):
            print("Error al leer la clave almacenada.")
            exit()

        if clave_ingresada == clave_almacenada:
            mensaje_encriptado = lineas[0].split(":")[1].strip()
            mi_motor = MTO.MotorEncriptacion(clave_almacenada)
            mensaje_desencriptado = mi_motor.desencriptar(mensaje_encriptado)
            print("Mensaje desencriptado:", mensaje_desencriptado)
        else:
            print("La clave ingresada no coincide con la almacenada.")

if __name__ == "__main__":
    main()
