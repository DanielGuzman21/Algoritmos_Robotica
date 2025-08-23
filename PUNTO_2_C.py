import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, step

variable = ""
wn = float(input("Ingrese la frecuencia natural no amortiguada (ωn): "))
zeta = float(input("Ingrese el coeficiente de amortiguamiento (ζ): "))
K = float(input("Ingrese el coeficiente K: "))

if zeta < 1:
    print("El sistema es Subamortiguado")
    
    numerador = [K * wn**2]
    denominador = [1, 2*zeta*wn, wn**2]
    sistema = TransferFunction(numerador, denominador)

    # Generar el tiempo y la respuesta al escalón
    t, y = step(sistema)

    # Graficar la respuesta al escalón
    plt.plot(t, y)
    plt.title("Respuesta al Escalón unitario subamortiguado")
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.show()
    
elif zeta == 1:
    print("El sistema es críticamente amortiguado")
    
    numerador = [K * wn**2]
    denominador = [1, 2*zeta*wn, wn**2]
    sistema = TransferFunction(numerador, denominador)

    # Generar el tiempo y la respuesta al escalón
    t, y = step(sistema)

    # Graficar la respuesta al escalón
    plt.plot(t, y)
    plt.title("Respuesta al Escalón unitario críticamente amortiguado")
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.show()
    
else:
    print("El sistema es sobreamortiguado")
   
    numerador = [K * wn**2]
    denominador = [1, 2*zeta*wn, wn**2]
    sistema = TransferFunction(numerador, denominador)

    # Generar el tiempo y la respuesta al escalón
    t, y = step(sistema)

    # Graficar la respuesta al escalón
    plt.plot(t, y)
    plt.title("Respuesta al Escalón unitario sobre amortiguado")
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.show()

    


