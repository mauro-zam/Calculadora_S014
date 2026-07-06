# ============================================
# 
'''
Ejercicio que desarrolla aspectos como:

variables;
decisiones;
ciclos;
excepciones;
diccionarios;
funciones;
GitHub;
estructura del programa

'''
# ============================================

# ESCENARIO

productos = [
    ["P001","Mouse"],
    ["P002","Teclado"],
    ["P003","Monitor"],
    ["P004","Parlantes"],
    ["P005","WebCam"]
]

# INVENTARIO

inventario = [
    ["P001",15,12990],
    ["P003",8,159990],
    ["P005",12,39990]
]

# ============================================
# FUNCIONES
# ============================================

def mostrar_menu():

    print("\n===== INVENTARIO =====")
    print("1. Consultar stock")
    print("2. Actualizar stock")
    print("3. Agregar inventario")
    print("4. Mostrar inventario")
    print("5. Salir")


def leer_opcion():

    while True:

        try:

            op=int(input("Seleccione opción: "))

            if 1<=op<=5:
                return op

            print("Opción inválida")

        except:

            print("Debe ingresar un número")


#--------------------------------------------

def buscar_catalogo(codigo):

    for producto in productos:

        if producto[0]==codigo:

            return producto

    return None


#--------------------------------------------

def buscar_inventario(codigo):

    for posicion in range(len(inventario)):

        if inventario[posicion][0]==codigo:

            return posicion

    return -1


#--------------------------------------------

def consultar_stock():

    codigo=input("Código: ").upper()

    pos=buscar_inventario(codigo)

    if pos==-1:

        print("Producto sin inventario")

        return

    producto=buscar_catalogo(codigo)

    print("---------------------")
    print("Producto :",producto[1])
    print("Stock    :",inventario[pos][1])
    print("Precio   :",inventario[pos][2])


#--------------------------------------------

def actualizar_stock():

    codigo=input("Código: ").upper()

    pos=buscar_inventario(codigo)

    if pos==-1:

        print("Producto no encontrado")

        return

    nuevo_stock=int(input("Nuevo stock: "))

    inventario[pos][1]=nuevo_stock

    print("Stock actualizado")


#--------------------------------------------

def agregar_inventario():

    codigo=input("Código: ").upper()

    if buscar_catalogo(codigo)==None:

        print("Código no existe en catálogo")

        return

    if buscar_inventario(codigo)!=-1:

        print("Producto ya existe en inventario")

        return

    stock=int(input("Stock: "))
    precio=int(input("Precio: "))

    inventario.append([codigo,stock,precio])

    print("Producto agregado")


#--------------------------------------------

def mostrar_inventario():

    print("\n====== INVENTARIO ======")

    for dato in inventario:

        producto=buscar_catalogo(dato[0])

        print("------------------------")
        print("Código :",dato[0])
        print("Nombre :",producto[1])
        print("Stock  :",dato[1])
        print("Precio :",dato[2])


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

while True:

    mostrar_menu()

    opcion=leer_opcion()

    if opcion==1:

        consultar_stock()

    elif opcion==2:

        actualizar_stock()

    elif opcion==3:

        agregar_inventario()

    elif opcion==4:

        mostrar_inventario()

    elif opcion==5:

        print("Programa finalizado")

        break