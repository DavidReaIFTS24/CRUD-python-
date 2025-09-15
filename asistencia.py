# Importa los módulos necesarios
import csv  # Para leer y escribir archivos CSV
import os   # Para verificar si el archivo existe en el sistema

# Define el nombre del archivo CSV que almacena los registros de asistencia
NOMBRE_ARCHIVO = 'asistencia.csv'

# Función para cargar los datos desde el archivo CSV
def cargar_asistencia():
    """Carga los datos del archivo CSV."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        # Si el archivo no existe, lo crea con los encabezados
        with open(NOMBRE_ARCHIVO, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Alumno', 'Fecha', 'Asistencia'])
            writer.writeheader()  # Escribe los encabezados
        return []  # Devuelve una lista vacía

    # Si el archivo existe, lo abre y carga los registros como una lista de diccionarios
    with open(NOMBRE_ARCHIVO, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Función para guardar los datos actualizados en el archivo CSV
def guardar_asistencia(datos):
    """Guarda los datos en el archivo CSV."""
    with open(NOMBRE_ARCHIVO, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Alumno', 'Fecha', 'Asistencia'])
        writer.writeheader()      # Escribe los encabezados
        writer.writerows(datos)   # Escribe todas las filas de datos

# Función para mostrar todos los registros de asistencia
def mostrar_asistencia(datos):
    """Muestra la asistencia de todos los alumnos."""
    print("\n--- Lista de Asistencia ---")
    if not datos:
        print("No hay registros de asistencia.")
        return
    
    # Recorre cada registro y lo muestra con su número de índice
    for i, registro in enumerate(datos):
        print(f"[{i+1}] Alumno: {registro['Alumno']}, Fecha: {registro['Fecha']}, Asistencia: {registro['Asistencia']}")

# Función para registrar una nueva entrada de asistencia
def registrar_asistencia(datos):
    """Permite registrar una nueva entrada de asistencia."""
    print("\n--- Registrar Nueva Asistencia ---")
    alumno = input("Nombre del Alumno: ")  # Solicita el nombre del alumno
    fecha = input("Fecha (YYYY-MM-DD): ")  # Solicita la fecha
    asistencia = input("Asistencia (Presente/Ausente): ")  # Solicita el estado de asistencia

    # Valida que el estado de asistencia sea correcto
    if asistencia.lower() not in ['presente', 'ausente']:
        print("Asistencia inválida. Por favor, escriba 'Presente' o 'Ausente'.")
        return

    # Crea un nuevo registro con los datos ingresados
    nuevo_registro = {
        'Alumno': alumno.capitalize(),
        'Fecha': fecha,
        'Asistencia': asistencia.capitalize()
    }

    datos.append(nuevo_registro)  # Agrega el nuevo registro a la lista
    guardar_asistencia(datos)    # Guarda los datos actualizados
    print("Registro de asistencia guardado con éxito.")

# Función para editar un registro existente
def editar_asistencia(datos):
    """Permite editar un registro existente."""
    if not datos:
        print("No hay registros para editar.")
        return
    
    mostrar_asistencia(datos)  # Muestra los registros actuales
    
    try:
        # Solicita el número del registro a editar
        indice = int(input("\nIngrese el número del registro que desea editar: ")) - 1
        if 0 <= indice < len(datos):
            print(f"Editando el registro: {datos[indice]}")
            
            # Solicita nuevos valores, permitiendo dejar en blanco para no cambiar
            nuevo_alumno = input("Nuevo nombre del Alumno (dejar en blanco para no cambiar): ")
            nueva_fecha = input("Nueva Fecha (YYYY-MM-DD, dejar en blanco para no cambiar): ")
            nueva_asistencia = input("Nueva Asistencia (Presente/Ausente, dejar en blanco para no cambiar): ")
            
            # Actualiza los campos si se ingresaron nuevos valores
            if nuevo_alumno:
                datos[indice]['Alumno'] = nuevo_alumno.capitalize()
            if nueva_fecha:
                datos[indice]['Fecha'] = nueva_fecha
            if nueva_asistencia:
                if nueva_asistencia.lower() in ['presente', 'ausente']:
                    datos[indice]['Asistencia'] = nueva_asistencia.capitalize()
                else:
                    print("Asistencia no válida. El registro no se ha modificado.")
            
            guardar_asistencia(datos)  # Guarda los cambios
            print("Registro actualizado con éxito.")
        else:
            print("Número de registro inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

# Función para eliminar un registro de asistencia
def eliminar_asistencia(datos):
    """Permite eliminar un registro existente."""
    if not datos:
        print("No hay registros para eliminar.")
        return

    mostrar_asistencia(datos)  # Muestra los registros actuales

    try:
        # Solicita el número del registro a eliminar
        indice = int(input("\nIngrese el número del registro que desea eliminar: ")) - 1
        if 0 <= indice < len(datos):
            # Confirma la eliminación
            confirmacion = input(f"¿Está seguro que desea eliminar el registro de {datos[indice]['Alumno']}? (s/n): ")
            if confirmacion.lower() == 's':
                datos.pop(indice)         # Elimina el registro de la lista
                guardar_asistencia(datos)  # Guarda los datos actualizados
                print("Registro eliminado con éxito.")
            else:
                print("Operación cancelada.")
        else:
            print("Número de registro inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

# Función principal que muestra el menú interactivo
def menu():
    """Función principal que muestra el menú interactivo."""
    datos_asistencia = cargar_asistencia()  # Carga los datos al iniciar
    
    while True:
        # Muestra las opciones del menú
        print("\n--- Menú de Control de Asistencia ---")
        print("1. Ver Asistencia")
        print("2. Registrar Asistencia")
        print("3. Editar Asistencia")
        print("4. Eliminar Asistencia")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")  # Solicita la opción del usuario
        
        # Ejecuta la función correspondiente según la opción elegida
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

# Ejecuta el menú si el script se corre directamente
if __name__ == "__main__":
    menu()
