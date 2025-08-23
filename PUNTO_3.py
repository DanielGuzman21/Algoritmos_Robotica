import math

# Coordenadas rectangulares
x = 23
y = 44
z = 45


r_cilindrica = math.sqrt(x**2 + y**2)
theta_cilindrica = math.atan2(y, x)
z_cilindrica = z

print("Coordenadas cilíndricas: ")
print(" R = ", r_cilindrica)
print(" theta = ", theta_cilindrica)
print(" z = ", z_cilindrica)


r_esferica = math.sqrt(x**2 + y**2 + z**2)
theta_esferica = math.acos(z / r_esferica)
phi_esferica = math.atan2(y, x)

print("Coordenadas Esfericas: ")
print(" R = ", r_esferica)
print(" theta = ", theta_esferica)
print(" z = ", phi_esferica)
