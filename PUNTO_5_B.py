while True:
    x = input("¿Desea continuar? (Si/No): ").strip().lower()
    
    if x == "no":
        print("Finalizar.")
        break
    elif x == "si":
        print("continuar")
    else:
        print("Error digite: 'Si' o 'No'.")