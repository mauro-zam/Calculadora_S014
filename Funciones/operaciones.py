#Calculadora

memoria=[]

def suma(n):
    suma=0
    for i in range(n):
        num = int(input(f"Ingrese el número {i+1}: "))
        suma+= num 

   
    return suma

def resta(n1,n2):
    return



while True:
    print("---- Menú_CALCULADORA ----")
    print("1. Sumar")
    print("2. Resta")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sumar")
    op=input("\nDigite la opción del menú:")

    match op:
        case "1":
            res=suma(int(input("Ingrese cantidad de nros, a sumar: ")))
            memoria.append(res)
            print(memoria)

        case "2":
            print()
        case "3":
            print()
        case "4":
            print()
        case "5":
            print("Usted ha saludo del sistema!!!")
            break
        case _:
            print("Opción no valida")




