

def read_file():    # La función se define con EL nombre: 'read_file'
    file = open("productos.txt", "r")    # abra el archivo stock (products.txt) en modo lectura.
    lines = file.readlines()
    L = []  # Asignar lista vacía con nombre 'L'
    for line in lines:
        L.append(line.replace("\n", "").split(","))
    file.close()
    print("Los siguientes productos están disponibles en nuestra tienda.")
    print("--------------------------------------------")
    print("PRODUCTO\tPRECIO\t\tCANTIDAD")
    print("--------------------------------------------")
    for i in range(len(L)):
        print(L[i][0], "\t\t", L[i][1], "\t\t", L[i][2])    # Imprime el producto disponible, precio y cantidad
    print("--------------------------------------------")
    return L
