import csv  # Para leer y escribir archivos CSV
import os   # Para limpiar pantalla y verificar existencia de archivos
from datetime import datetime  # Para convertir formatos de fecha

NOMBRE_ARCHIVO = 'asistencia.csv'  # Nombre del archivo CSV

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')  # 'cls' para Windows, 'clear' para Unix/Linux/Mac

def cargar_asistencia():
    """Carga los registros desde el archivo CSV."""
    if not os.path.exists(NOMBRE_ARCHIVO):  # Si el archivo no existe
        with open(NOMBRE_ARCHIVO, 'w', newline='') as file:  # Lo crea
            writer = csv.DictWriter(file, fieldnames=['Alumno', 'Fecha', 'Asistencia'])  # Define encabezados
            writer.writeheader()  # Escribe encabezados
        return []  # Devuelve lista vacía
    with open(NOMBRE_ARCHIVO, 'r', newline='') as file:  # Si existe, lo abre
        reader = csv.DictReader(file)  # Lee como diccionario
        return list(reader)  # Devuelve lista de registros

def guardar_asistencia(datos):
    """Guarda los datos en el archivo CSV."""
    with open(NOMBRE_ARCHIVO, 'w', newline='') as file:  # Abre archivo en modo escritura
        writer = csv.DictWriter(file, fieldnames=['Alumno', 'Fecha', 'Asistencia'])  # Define campos
        writer.writeheader()  # Escribe encabezados
        writer.writerows(datos)  # Escribe registros

def mostrar_asistencia(datos):
    """Muestra la asistencia de todos los alumnos."""
    print("\n--- Lista de Asistencia ---")  # Título
    if not datos:  # Si no hay datos
        print("No hay registros de asistencia.")  # Mensaje vacío
    else:
        for i, registro in enumerate(datos):  # Recorre registros
            print(f"[{i+1}] Alumno: {registro['Alumno']}, Fecha: {registro['Fecha']}, Asistencia: {registro['Asistencia']}")  # Muestra cada uno
    input("\nPresione Enter para continuar...")  # Pausa
    limpiar_pantalla()  # Limpia pantalla

def registrar_asistencia(datos):
    """Permite registrar una nueva entrada de asistencia."""
    print("\n--- Registrar Nueva Asistencia ---")  # Título
    alumno = input("Nombre del Alumno (o escriba 'volver' para regresar): ")  # Solicita nombre
    if alumno.lower() == 'volver':  # Opción para volver
        limpiar_pantalla()
        return

    fecha = input("Fecha (YYYY-MM-DD): ")  # Solicita fecha
    if fecha.lower() == 'volver':
        limpiar_pantalla()
        return

    try:
        fecha_formateada = datetime.strptime(fecha, "%Y-%m-%d").strftime("%d/%m/%Y")  # Convierte a DD/MM/YYYY
    except ValueError:
        print("Formato de fecha inválido. Use YYYY-MM-DD.")
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()
        return

    asistencia = input("Asistencia (Presente/Ausente): ")  # Solicita estado
    if asistencia.lower() == 'volver':
        limpiar_pantalla()
        return

    if asistencia.lower() not in ['presente', 'ausente']:  # Valida asistencia
        print("Asistencia inválida. Por favor, escriba 'Presente' o 'Ausente'.")
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()
        return

    nuevo_registro = {
        'Alumno': alumno.capitalize(),
        'Fecha': fecha_formateada,
        'Asistencia': asistencia.capitalize()
    }

    datos.append(nuevo_registro)
    guardar_asistencia(datos)
    print("Registro de asistencia guardado con éxito.")
    input("\nPresione Enter para continuar...")
    limpiar_pantalla()

def editar_asistencia(datos):
    """Permite editar un registro existente."""
    if not datos:
        print("No hay registros para editar.")
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()
        return

    while True:
        mostrar_asistencia(datos)

        entrada = input("\nIngrese el número del registro que desea editar (o escriba 'volver'): ")
        if entrada.lower() == 'volver':
            limpiar_pantalla()
            return

        try:
            indice = int(entrada) - 1
            if 0 <= indice < len(datos):
                print(f"Editando el registro: {datos[indice]}")

                nuevo_alumno = input("Nuevo nombre del Alumno (dejar en blanco para no cambiar, o 'volver'): ")
                if nuevo_alumno.lower() == 'volver':
                    limpiar_pantalla()
                    return

                nueva_fecha = input("Nueva Fecha (YYYY-MM-DD, dejar en blanco para no cambiar, o 'volver'): ")
                if nueva_fecha.lower() == 'volver':
                    limpiar_pantalla()
                    return

                nueva_asistencia = input("Nueva Asistencia (Presente/Ausente, dejar en blanco para no cambiar, o 'volver'): ")
                if nueva_asistencia.lower() == 'volver':
                    limpiar_pantalla()
                    return

                if nuevo_alumno:
                    datos[indice]['Alumno'] = nuevo_alumno.capitalize()
                if nueva_fecha:
                    try:
                        datos[indice]['Fecha'] = datetime.strptime(nueva_fecha, "%Y-%m-%d").strftime("%d/%m/%Y")
                    except ValueError:
                        print("Formato de fecha inválido. No se modificó.")
                if nueva_asistencia:
                    if nueva_asistencia.lower() in ['presente', 'ausente']:
                        datos[indice]['Asistencia'] = nueva_asistencia.capitalize()
                    else:
                        print("Asistencia no válida. El registro no se ha modificado.")

                guardar_asistencia(datos)
                print("Registro actualizado con éxito.")
                break
            else:
                print("Elija un número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    input("\nPresione Enter para continuar...")
    limpiar_pantalla()

def eliminar_asistencia(datos):
    """Permite eliminar un registro existente."""
    if not datos:
        print("No hay registros para eliminar.")
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()
        return

    while True:
        mostrar_asistencia(datos)

        entrada = input("\nIngrese el número del registro que desea eliminar (o escriba 'volver'): ")
        if entrada.lower() == 'volver':
            limpiar_pantalla()
            return

        try:
            indice = int(entrada) - 1
            if 0 <= indice < len(datos):
                confirmacion = input(f"¿Está seguro que desea eliminar el registro de {datos[indice]['Alumno']}? (s/n): ")
                if confirmacion.lower() == 's':
                    datos.pop(indice)
                    guardar_asistencia(datos)
                    print("Registro eliminado con éxito.")
                else:
                    print("Operación cancelada.")
                break
            else:
                print("Elija un número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    input("\nPresione Enter para continuar...")
    limpiar_pantalla()

def menu():
    """Muestra el menú principal y gestiona las opciones."""
    datos_asistencia = cargar_asistencia()

    while True:
        print("\n--- Menú de Control de Asistencia ---")
        print("1. Ver Asistencia")
        print("2. Registrar Asistencia")
        print("3. Editar Asistencia")
        print("4. Eliminar Asistencia")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_asistencia(datos_asistencia)
        elif opcion == '2':
            registrar_asistencia(datos_asistencia)
        elif opcion == '3':
            editar_asistencia(datos_asistencia)
        elif opcion == '4':
            eliminar_asistencia(datos_asistencia)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

if __name__ == "__main__":
    limpiar_pantalla()
    menu()
