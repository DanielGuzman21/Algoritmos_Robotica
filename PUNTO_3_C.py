import numpy as np
import matplotlib.pyplot as plt


V = float(input("Ingrese el voltaje (V): "))
R = float(input("Ingrese la la resistencia (Ω): "))
C = float(input("Ingrese la capacitancia (uF): "))

#Todo en microfaradios
C = C * 1e-6

#tao
t = np.linspace(0, 5*R*C, 1000)


V_carga = V * (1 - np.exp(-t / (R * C)))
V_descarga = V * np.exp(-t / (R * C))

# Graficar
plt.figure(figsize=(10,9))

######## Carga ############
plt.subplot(2, 1, 1)
plt.plot(t, V_carga, label="Carga del capacitor", color="Purple")
plt.title("Grafica de carga y descarga de un condensador de un circuito RC")
plt.ylabel("Voltaje (V)")
plt.grid(True)
plt.legend()

######### Descarga ############
plt.subplot(2, 1, 2)
plt.plot(t, V_descarga, label="Descarga del capacitor", color="Orange")
plt.xlabel("Tiempo (S)")
plt.ylabel("Voltaje (V)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()



