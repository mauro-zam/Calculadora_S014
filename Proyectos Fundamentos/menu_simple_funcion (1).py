
def menu_principal():
    while True:
        print("=== Menu Principal ===")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                print("Has seleccionado la Opción 1")
                # Aquí puedes agregar la lógica para la Opción 1
            case "2":
                print("Has seleccionado la Opción 2")
                # Aquí puedes agregar la lógica para la Opción 2
            case "3":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción válida.")
