import csv
import os

# Nombre del archivo CSV de la base de datos
NOMBRE_ARCHIVO = 'asistencia.csv'

def cargar_asistencia():
    """Carga los datos del archivo CSV."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        # Si el archivo no existe, lo crea con los encabezados
        with open(NOMBRE_ARCHIVO, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Alumno', 'Fecha', 'Asistencia'])
            writer.writeheader()
        return []

    with open(NOMBRE_ARCHIVO, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def guardar_asistencia(datos):
    """Guarda los datos en el archivo CSV."""
    with open(NOMBRE_ARCHIVO, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Alumno', 'Fecha', 'Asistencia'])
        writer.writeheader()
        writer.writerows(datos)

def mostrar_asistencia(datos):
    """Muestra la asistencia de todos los alumnos."""
    print("\n--- Lista de Asistencia ---")
    if not datos:
        print("No hay registros de asistencia.")
        return
    
    for i, registro in enumerate(datos):
        print(f"[{i+1}] Alumno: {registro['Alumno']}, Fecha: {registro['Fecha']}, Asistencia: {registro['Asistencia']}")

def registrar_asistencia(datos):
    """Permite registrar una nueva entrada de asistencia."""
    print("\n--- Registrar Nueva Asistencia ---")
    alumno = input("Nombre del Alumno: ")
    fecha = input("Fecha (YYYY-MM-DD): ")
    asistencia = input("Asistencia (Presente/Ausente): ")

    if asistencia.lower() not in ['presente', 'ausente']:
        print("Asistencia inválida. Por favor, escriba 'Presente' o 'Ausente'.")
        return

    nuevo_registro = {
        'Alumno': alumno.capitalize(),
        'Fecha': fecha,
        'Asistencia': asistencia.capitalize()
    }
    datos.append(nuevo_registro)
    guardar_asistencia(datos)
    print("Registro de asistencia guardado con éxito.")

def editar_asistencia(datos):
    """Permite editar un registro existente."""
    if not datos:
        print("No hay registros para editar.")
        return
    
    mostrar_asistencia(datos)
    
    try:
        indice = int(input("\nIngrese el número del registro que desea editar: ")) - 1
        if 0 <= indice < len(datos):
            print(f"Editando el registro: {datos[indice]}")
            
            nuevo_alumno = input(f"Nuevo nombre del Alumno (dejar en blanco para no cambiar): ")
            nueva_fecha = input(f"Nueva Fecha (YYYY-MM-DD, dejar en blanco para no cambiar): ")
            nueva_asistencia = input(f"Nueva Asistencia (Presente/Ausente, dejar en blanco para no cambiar): ")
            
            if nuevo_alumno:
                datos[indice]['Alumno'] = nuevo_alumno.capitalize()
            if nueva_fecha:
                datos[indice]['Fecha'] = nueva_fecha
            if nueva_asistencia:
                if nueva_asistencia.lower() in ['presente', 'ausente']:
                    datos[indice]['Asistencia'] = nueva_asistencia.capitalize()
                else:
                    print("Asistencia no válida. El registro no se ha modificado.")
            
            guardar_asistencia(datos)
            print("Registro actualizado con éxito.")
        else:
            print("Número de registro inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

def menu():
    """Función principal que muestra el menú interactivo."""
    datos_asistencia = cargar_asistencia()
    
    while True:
        print("\n--- Menú de Control de Asistencia ---")
        print("1. Ver Asistencia")
        print("2. Registrar Asistencia")
        print("3. Editar Asistencia")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_asistencia(datos_asistencia)
        elif opcion == '2':
            registrar_asistencia(datos_asistencia)
        elif opcion == '3':
            editar_asistencia(datos_asistencia)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()