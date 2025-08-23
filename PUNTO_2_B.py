import random
 
x=0   
x = int(input("Ingrese la cantidad de números aleatorios que desea: "))

inferior = int(input("Ingrese el valor mínimo del rango: "))
superior = int(input("Ingrese el valor máximo del rango: "))

aleatorios = [random.randint(inferior, superior) for _ in range(x)]

# Mostrar los números generados
print(f"Los {x} números aleatorios generados entre {inferior} y {superior} son: ")
print(aleatorios)
    

