import numpy as np

# Inicializa matrices
matriz_1 = np.array([[22, 12], [22, 11]])
matriz_2 = np.array([[34, 4], [12, 9]])

print("")
suma = matriz_1 + matriz_2
print("Suma:")
print(suma)

print("")
resta = matriz_1 - matriz_2
print("Resta:")
print(resta)

print("")
producto_punto = np.dot(matriz_1, matriz_2)
print("Producto punto:")
print(producto_punto)

print("")
producto_cruz = matriz_1 * matriz_2
print("Producto elemento a elemento:")
print(producto_cruz)

print("")
division = matriz_1 / matriz_2
print("División (elemento a elemento):")
print(division)
