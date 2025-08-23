import numpy as np

# Inicializa dos vectores
vector1 = np.array([34, 22, 31])
vector2 = np.array([12, 12, 23])


suma = vector1 + vector2
print("Suma: ", suma)


resta = vector1 - vector2
print("Resta: ", resta)


producto_punto = np.dot(vector1, vector2)
print("Producto punto: ", producto_punto)


producto_cruz = np.cross(vector1, vector2)
print("Producto cruz: ", producto_cruz)


division = vector1 / vector2
print("División: ", division)
