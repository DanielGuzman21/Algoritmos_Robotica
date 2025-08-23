import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
3
# Ingresar las coordenadas del vector
x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Vector Inicial
vector = [0, 0, 0]

ax.quiver(vector[0], vector[1], vector[2], x, y, z, color='Red')

# Configurar los límites de los ejes
ax.set_xlim([min(0, x)-1, max(0, x)+1])
ax.set_ylim([min(0, y)-1, max(0, y)+1])
ax.set_zlim([min(0, z)-1, max(0, z)+1])

# Label de cada uno de los ejes.
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')


ax.set_title('Grafica de un vector en un sistema coordenado 3D')

#plotear
plt.show()



    

