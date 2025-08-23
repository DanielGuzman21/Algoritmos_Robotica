import numpy as np
import matplotlib.pyplot as plt

# Constantes del PT100 (IEC 60751)
R0 = 100  # Resistencia a 0°C
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

# Rango de temperatura
T = np.arange(-20, 20, 1)

# Cálculo de resistencia con ecuación polinómica
R = np.where(
    T >= 0,
    R0 * (1 + A*T + B*T**2),  # Para T >= 0°C
    R0 * (1 + A*T + B*T**2 + C*(T-100)*T**3)  # Para T < 0°C
)

#///////// PLOTEO ///////////
plt.figure(figsize=(10, 5))
plt.plot(T, R, label="PT100 (IEC 60751)", color="red", linewidth=2.5)
plt.title("Curva Real de una PT100")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ω)")
plt.grid(True)
plt.legend()
plt.show()
