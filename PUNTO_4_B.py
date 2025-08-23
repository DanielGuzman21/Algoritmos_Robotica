while True:
    
    print("Seleccione el tipo de robot del que desea obtener información:")
    print("")
    print("1). Robot Cilíndrico")
    print("2). Robot Cartesiano")
    print("3). Robot Esférico")
    print("")
    menu = int(input("Ingrese el número:"))

    if menu == 1:
        print("")
        print("Robot Cilíndrico: Tiene 3 articulaciones principales = una articulación lineal (Z), una rotacional (R), y otra lineal (prismática).")
        print("")
    elif menu == 2:
        print("Robot Cartesiano: Tiene 3 articulaciones lineales (X, Y, Z), todas en ángulos rectos entre sí.")

    elif menu == 3:
        print("")
        print("Robot Esférico: Tiene 3 articulaciones principales - dos rotacionales (R1, R2) y una lineal (prismática).")
        print("")
    else:
        print("")
        print("Error!, seleccione una opción entre 1 y 3.")
        print("")
