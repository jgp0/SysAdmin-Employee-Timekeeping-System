import csv
import os
from datetime import datetime

# Definir los campos del archivo CSV
campos = ['Empleado', 'Fecha', 'Hora_Entrada', 'Hora_Salida']

# Crear un archivo CSV para almacenar los registros de horas
archivo_registros = 'data/registros_horas.csv'
if not os.path.exists(archivo_registros):
    with open(archivo_registros, 'w', newline='') as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()

def registrar_hora():
    empleado = input("Nombre del empleado: ")
    hora_entrada = input("Hora de entrada (HH:MM): ")
    hora_salida = input("Hora de salida (HH:MM): ")
    
    # Validar el formato de las horas ingresadas
    try:
        hora_entrada = datetime.strptime(hora_entrada, '%H:%M')
        hora_salida = datetime.strptime(hora_salida, '%H:%M')
    except ValueError:
        print("Formato de hora incorrecto. Utiliza HH:MM.")
        return

    # Registrar el registro de horas en el archivo CSV
    with open(archivo_registros, 'a', newline='') as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writerow({
            'Empleado': empleado,
            'Fecha': datetime.now().strftime('%Y-%m-%d'),
            'Hora_Entrada': hora_entrada.strftime('%H:%M'),
            'Hora_Salida': hora_salida.strftime('%H:%M')
        })

def generar_reporte():
    empleado = input("Nombre del empleado para el informe (dejar en blanco para todos los empleados): ")
    
    # Leer registros de horas desde el archivo CSV
    registros = []
    with open(archivo_registros, 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            if not empleado or fila['Empleado'] == empleado:
                registros.append(fila)

    if registros:
        print("\nRegistro de Horas:")
        for registro in registros:
            print(f"Empleado: {registro['Empleado']}, Fecha: {registro['Fecha']}, Entrada: {registro['Hora_Entrada']}, Salida: {registro['Hora_Salida']}")
    else:
        print("No se encontraron registros para el empleado especificado.")

if __name__ == '__main__':
    while True:
        print("\nSistema de Registro de Horas")
        print("1. Registrar Hora")
        print("2. Generar Informe")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            registrar_hora()
        elif opcion == '2':
            generar_reporte()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")