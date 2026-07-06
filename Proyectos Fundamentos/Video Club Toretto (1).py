
peliculas = {
    "AV101": {"valor": 15000, "pelicula": "Avatar: The Way of Water", "año": 2022, "stock": 4},
    "TO102": {"valor": 14500, "pelicula": "Top Gun: Maverick", "año": 2022, "stock": 2},
    "OP103": {"valor": 14000, "pelicula": "Oppenheimer", "año": 2023, "stock": 5},
    "DU104": {"valor": 13500, "pelicula": "Dune", "año": 2021, "stock": 3},
    "BA105": {"valor": 13000, "pelicula": "Batman", "año": 2022, "stock": 1},
    "JO106": {"valor": 11000, "pelicula": "Joker", "año": 2019, "stock": 2},
    "IN107": {"valor": 10000, "pelicula": "Interstellar", "año": 2014, "stock": 4},
    "MA108": {"valor": 8500, "pelicula": "Matrix", "año": 1999, "stock": 3},
    "GL109": {"valor": 7000, "pelicula": "Gladiador", "año": 2000, "stock": 5},
    "TI110": {"valor": 5000, "pelicula": "Titanic", "año": 1997, "stock": 2}
}
clientes = {
    "17328459-4": {"nombre": "Mauricio Zamorano", "teléfono": "987654321"},
    "18273645-6": {"nombre": "María Gómez", "teléfono": "912345678"},
    "19283746-5": {"nombre": "Carlos Rodríguez", "teléfono": "923456789"},
    "18273645-7": {"nombre": "Ana Martínez", "teléfono": "934567890"},
    "19283746-8": {"nombre": "Luis Fernández", "teléfono": "945678901"},
    "15796775-4": {"nombre": "Dominique", "teléfono": "945678901"}
    }

arrendadas = {
    "AV101": [{"Rut": "17328459-4", "Nombre Cliente": "Mauricio Zamorano", "Pelicula": "Avatar: The Way of Water", "Fecha Arrendamiento": "2024-06-01"}],
    "TO102": [{"Rut": "18273645-6", "Nombre Cliente": "María Gómez", "Pelicula": "Top Gun: Maverick", "Fecha Arrendamiento": "2024-06-02"}],
    "OP103": [{"Rut": "19283746-5", "Nombre Cliente": "Carlos Rodríguez", "Pelicula": "Oppenheimer", "Fecha Arrendamiento": "2024-06-03"}],
    "DU104": [{"Rut": "18273645-7", "Nombre Cliente": "Ana Martínez", "Pelicula": "Dune", "Fecha Arrendamiento": "2024-06-04"}],
    "BA105": [{"Rut": "19283746-8", "Nombre Cliente": "Luis Fernández", "Pelicula": "Batman", "Fecha Arrendamiento": "2024-06-05"}]
}
cont1=0

while True: 
    try:
        print("\n<<<<<<<< VIDEO CLUB TORETTO >>>>>>>>>\n")
        
        print("\n Bienvenido al Video Club Toretto, donde encontrarás una amplia selección de películas.")
        
        print("\n ---- Menú de opciones ----")
        print("(1) Ver catálogo de películas disponibles")
        print("(2) ingresar nueva película al catálogo")
        print("(3) Ver listado de peliculas arrendadas")
        print("(4) Ingresar nuevo cliente al sistema")
        print("(5) Arrendar una película")
        print("(6) Devolver una película")
        print("(7) Salir")
        op = input("\nSeleccione una opción: ")
        if op == "1":
            print("\nCatálogo de películas disponibles:")
            print("-" * 80)
            if cont1!=0:
                cont1=0
            
            for sku, info in peliculas.items():
                print(f"SKU: {sku}, Precio: ${info["valor"]}, Stock: {info["stock"]}, Película: {info["pelicula"]}, Año: {info["año"]}")
                cont1+=1
                if cont1==25:
                    cont1=0
                    pausa=input("\n Presione cualquier tecla para continuar...")
            pausa=input("\n Presione cualquier tecla para continuar...")
        elif op == "2":
            print("\nIngreso de nueva película:")
            print("-" * 80)
            sku = input("Ingrese el SKU de la película (ejemplo: AV101): ").upper()
            if sku in peliculas:
                print()
                print("El SKU ya existe en el catálogo!")
                print(f"El SKU {sku} corresponde a la película: {peliculas[sku]["pelicula"]}, año: {peliculas[sku]["año"]}, precio: ${peliculas[sku]["valor"]}, cantidad disponible: {peliculas[sku]["stock"]}")
                res1=input("\n ¿Deseas sumar mas stock a esta película? (S/N): ").upper()
                if res1=="S":
                    cantidad = int(input("Ingrese la cantidad a sumar: "))
                    peliculas[sku]['stock'] += cantidad
                    print(f"Stock actualizado. Nueva cantidad disponible de {peliculas[sku]["pelicula"]}: {peliculas[sku]["stock"]}")
            else:
                pelicula = input("Ingrese el nombre de la película: ")
                valor = int(input("Ingrese el valor de la película: "))
                año = int(input("Ingrese el año de la película: "))
                cantidad = int(input("Ingrese la cantidad disponible: "))
                peliculas[sku] = {"valor": valor, "pelicula": pelicula, "año": año, "stock": cantidad}
                print("\nPelícula agregada al catálogo exitosamente.")
            input("\n Presione cualquier tecla para continuar...")
        
        elif op== "3":
            print("\nListado de películas arrendadas:")
            print("-" * 80)
            for sku, lista_arriendos in arrendadas.items():
                cont1+=1
                for arriendo in lista_arriendos:

                    print(
                        f"SKU: {sku} | "
                        f"RUT: {arriendo['Rut']} | "
                        f"Cliente: {arriendo['Nombre Cliente']} | "
                        f"Película: {arriendo['Pelicula']} | "
                        f"Fecha: {arriendo['Fecha Arrendamiento']}")
                    
            
            pausa=input("\n Presione cualquier tecla para continuar...")
        
        elif op == "4":
            while True:
                print("\n          MENU DE INGRESO DE CLIENTES          ")
                print("-" * 80)
                rut = input("Ingrese RUT de nuevo cliente (Ejemplo:12345678-9): ").upper()
                try:
                    cuerpo, dv = rut.split("-")
                    factor = 2
                    suma = 0

                    for n in reversed(cuerpo):
                        suma += int(n) * factor
                        factor = factor + 1 if factor < 7 else 2

                    dv_calc = 11 - (suma % 11)

                    if dv_calc == 11:
                        dv_calc = "0"
                    elif dv_calc == 10:
                        dv_calc = "K"
                    else:
                        dv_calc = str(dv_calc)

                    if dv == dv_calc:
                        break

                    print("RUT inválido")
                    

                except:
                    print("Formato incorrecto")
                    break
            
            if rut in clientes:
                print("\nEl RUT ya existe en el sistema!")
                print(f"El RUT {rut} corresponde al cliente: {clientes[rut]["nombre"]}, teléfono: {clientes[rut]["teléfono"]}")
            else:
                nombre = input("Ingrese el nombre del cliente: ")
                telefono = input("Ingrese el teléfono del cliente: ")
                clientes[rut] = {"nombre": nombre, "teléfono": telefono}
                print("\nCliente agregado al sistema exitosamente.")
            input("\n Presione cualquier tecla para continuar...")

        elif op == "5":
            print("\n          MENU DE ARRIENDAMIENTO DE PELÍCULAS          ")
            print("-" * 80)

            rut = input("Ingrese el RUT del cliente: ").upper()

            if rut in clientes:

                print(f"\nCliente encontrado: {clientes[rut]['nombre']}")
                print(f"Teléfono: {clientes[rut]['teléfono']}")

                sku = input("\nIngrese el SKU de la película que desea arrendar: ").upper()

                if sku in peliculas:

                    if peliculas[sku]["stock"] > 0:

                        print("\nPelícula seleccionada:")
                        print(f"Nombre : {peliculas[sku]['pelicula']}")
                        print(f"Año    : {peliculas[sku]['año']}")
                        print(f"Valor  : ${peliculas[sku]['valor']}")
                        print(f"Stock  : {peliculas[sku]['stock']}")

                        precio = peliculas[sku]["valor"]

                        while True:

                            try:
                                pago = int(input("\nIngrese el monto pagado: $"))

                                if pago >= precio:

                                    vuelto = pago - precio

                                    nuevo_arriendo = {
                                        "Rut": rut,
                                        "Nombre Cliente": clientes[rut]["nombre"],
                                        "Pelicula": peliculas[sku]["pelicula"],
                                        "Fecha Arrendamiento": "2026-06-07"
                                    }

                                    if sku not in arrendadas:
                                        arrendadas[sku] = []

                                    arrendadas[sku].append(nuevo_arriendo)

                                    peliculas[sku]["stock"] -= 1

                                    print("\nArriendo realizado exitosamente.")
                                    print(f"Vuelto: ${vuelto}")
                                    print(f"Stock restante: {peliculas[sku]['stock']}")

                                    break

                                else:
                                    print("Monto insuficiente.")

                            except ValueError:
                                print("Debe ingresar un valor numérico.")

                    else:
                        print("\nLa película no tiene stock disponible.")

                else:
                    print("\nEl SKU ingresado no existe.")

            else:
                print("\nNo existe un cliente con ese RUT.")

            input("\nPresione cualquier tecla para continuar...")







        elif op == "6":
            print("\n          MENU DE DEVOLUCIÓN DE PELÍCULAS          ")
            print("-" * 80)

            rut = input("Ingrese el RUT del cliente: ").upper()
            sku = input("Ingrese el SKU de la película: ").upper()

            if sku in arrendadas:

                encontrado = False

                for arriendo in arrendadas[sku]:

                    if arriendo["Rut"] == rut:

                        peliculas[sku]["stock"] += 1

                        print(f"\nPelícula '{arriendo['Pelicula']}' "f"devuelta exitosamente por "f"{arriendo['Nombre Cliente']}.")

                        arrendadas[sku].remove(arriendo)

                        if len(arrendadas[sku]) == 0:
                            del arrendadas[sku]

                        encontrado = True
                        break

                if not encontrado:
                    print("\nNo existe un arriendo para ese RUT y SKU.")

            else:
                print("\nEl SKU ingresado no tiene arriendos registrados.")

            input("\nPresione cualquier tecla para continuar...")



           

        elif op == "7":
            print("\nGracias por usar el Video Club Toretto. ¡Hasta luego!")
            break
    except:
        print("Opción no válida. Por favor, ingrese un número del 1 al 7.") 

