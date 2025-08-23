def pt100(temperatura):
    # Constantes
    R0 = 100  #°C
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12  

    if temperatura >= 0:
        r  = R0 * (1 + A * temperatura + B * temperatura**2)
    else:
        r = R0 * (1 + A * temperatura + B * temperatura**2 + C * (temperatura - 100) * temperatura**3)
    
    return r

temperatura = 100
r = pt100(temperatura)
print("Resistencia: ", r)
print("Temperatura: ", temperatura)
