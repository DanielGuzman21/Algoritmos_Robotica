import math

while True:
    print(" ")
    print("Seleccione el sólido del que desea calcular el volumen:")
    print("1). Prisma")
    print("2). Pirámide")
    print("3). Cono truncado")
    print("4). Cilindro")
    print(" ")
    
    menu = int(input("Ingrese el número: "))
    
    if menu == 1:
        print("")
        base = float(input("Ingresa el área de la base del prisma: "))
        altura = float(input("Ingresa la altura del prisma: "))
        volumen = base * altura
        print("")
        print("El volumen del prisma es:",volumen)
        print("")
    
    elif menu == 2:
        print("")
        base = float(input("Ingresa el área de la base de la pirámide: "))
        altura = float(input("Ingresa la altura de la pirámide: "))
        volumen = (base * altura) / 3
        print("")
        print("El volumen de la pirámide es:",volumen)
        print("")
    
    elif menu == 3:
        print("")
        radio_menor = float(input("Ingresa el radio menor del cono truncado: "))
        radio_mayor = float(input("Ingresa el radio mayor del cono truncado: "))
        altura = float(input("Ingresa la altura del cono truncado: "))
        print("")
        volumen = (1/3) * math.pi * altura * (radio_mayor**2 + radio_menor**2 + radio_mayor * radio_menor)
        print("El volumen del cono truncado es: ", volumen)
        print("")
    
    elif menu == 4:
        print("")
        radio = float(input("Ingresa el radio de la base del cilindro: "))
        altura = float(input("Ingresa la altura del cilindro: "))
        volumen =math.pi * radio**2 * altura
        print("")
        print("El volumen del cilindro es: ",volumen)
        print("")
    
    else:
        print("")
        print("Error! seleccione una opción entre 1 y 4.")
        print("")
