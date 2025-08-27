import math


p_entrada = 40 # psi
p_salida = 50  # psi
d_cilindro = 300 # mm
l_cilindro = 90  # mm

#fuerza de avance
fuerza_avance = abs(p_entrada * (math.pi * (d_cilindro/2)**2))
print("Fuerza de avance:", fuerza_avance, "N")

#fuerza de retroceso
fuerza_retroceso = abs(p_salida * (math.pi * (d_cilindro/2)**2) - math.pi *(d_cilindro/2)**2)
print("Fuerza de retroceso:", fuerza_retroceso, "N")



