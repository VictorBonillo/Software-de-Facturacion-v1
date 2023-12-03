def over_write(List, Dictionary):   # Una función de sobrescritura
    L = List    # asignar lista con nombre de variable 'L'
    d = Dictionary    # asignar diccionario con nombre de variable 'd'
    """
    Actualice la cantidad de producto después de que el cliente haya comprado cierta cantidad de cualquier producto.
    E imprima los productos restantes en stock.
    """
    for keys in d.keys():
        if keys == "MOVIL":
            L[0][2] = str(int(L[0][2])-d['MOVIL'])
        elif keys == "LAPTOP":
            L[1][2] = str(int(L[1][2])-d['LAPTOP'])
        else:
            L[2][2] = str(int(L[2][2])-d['HDD'])
    print("\nProductos en stock restantes:\n",L)
        
    files = open("productos.txt", "w")  # Abre el archivo de stocks (productos.txt) en modo de escritura.
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return
