tareas = []

def agregar_tarea():
    try:
        descripcion = input("Ingrese la descripción de la tarea: ")
        if descripcion.strip() == "" or descripcion ==" ":
            print("La descripción no puede estar vacía.")
            return
        
        prioridad = int(input("Ingrese la prioridad de la tarea (1 a 10): "))
        if prioridad < 1 or prioridad > 10:
            print("La prioridad debe ser un número entre 1 y 10.")
            return
        
        tiempo = float(input("Ingrese el tiempo estimado para completar la tarea (en horas): "))
        if tiempo <= 0:
            print("El tiempo estimado debe ser un número positivo.")
            return
        
        tarea = {
            "descripcion": descripcion,
            "prioridad": prioridad,
            "tiempo": tiempo,
            "completada": False
        }
        tareas.append(tarea)
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar correctamente")
        return

    print("Tarea agregada exitosamente.")

def Actualizar_estado(tareas):
    if not tareas:
        print("No hay tareas para actualizar.")
        return

    print("Lista de tareas:")
    for tarea in tareas:
        if tarea["prioridad"] >= 5:
            tarea["completada"] = True
            print(f"Tarea '{tarea['descripcion']}' actualizada a completada.")
    

while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar tarea")
    print("2. --------------------")
    print("3. --------------------")
    print("4. Actualizar estado")
    print("5. --------------------")
    print("6. Salir")
    print("=====================================")
    opcion = int(input("Seleccione una opción: "))
    match opcion:
        case 1:
            agregar_tarea()


        case 2:
            print("Opción 2")
        case 3:
            print("Opción 3")   
        case 4:
            Actualizar_estado(tareas)



            
        case 5:
            print("Opción 5")
        case 6:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")








