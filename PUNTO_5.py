import numpy as np

theta = np.pi  

def x(theta):
    matriz = np.array([
        [1,             0,             0 ],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]])
    return matriz

def y(angulo):
    matriz = np.array([
        [np.cos(theta),  0, np.sin(theta)],
        [0,              1,             0],
        [-np.sin(theta), 0, np.cos(theta)]])
    return matriz

def z(angulo):
    matriz = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,          0,                 1]])
    return matriz

m_x = x(theta)
m_y = y(theta)
m_z = z(theta)


print("Matriz de rotación en X:")
print("")
print(m_x)
print("")

print("Matriz de rotación en Y:")
print("")
print(m_y)
print("")

print("Matriz de rotación en Z:")
print("")
print(m_z)
print("")
