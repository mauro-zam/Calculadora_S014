op='0'
suma=0
promedio=0
t_notas=0
while op !="3":
    print("===== MENÚ =====")
    print("1. Ingresar Notas")
    print("2. Mostrar Promedio")
    print("3. Salir")
    print()
    op = input("Seleccione una opción: ")
    if op=="1":
        try:
            while True:
                can=int(input("Ingrese la cantidad de notas (1-5): "))
                if 1 <= can <= 5:
                    for i in range(can):
                        while True:
                            try:
                                nota=float(input(f"Ingrese nota {i+1}: "))
                                if 1 <= nota <= 7:
                                    suma+=nota
                                    t_notas+=1
                                    break
                                else:
                                    print("ERROR: La nota debe ser entre 1 y 7")
                            except ValueError:
                                print("Dato no VALIDO")
                    break 
                    pausa=input("Notas ingresadas correctamente. Presione Enter para continuar...")  
                else:
                    print("ERROR: La cantidad de notas debe ser entre 1 y 5")
        except ValueError:
            print("Dato no VALIDO")    
    elif op=="2":
        if t_notas > 0:
            promedio=suma/t_notas
            print(f"El promedio es: {promedio}")
            pausa=input("Presione Enter para continuar...")
        else:
            print("ERROR: Debe ingresar al menos una nota para calcular el promedio.")
    elif op=="3":
        print("Saliendo del programa. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
                



