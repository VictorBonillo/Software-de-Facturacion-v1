"""
Funcion de este archivo:
1) Interacción con el cliente sobre qué y cuánto quiere comprar.
2) verificar la interacción del usuario válida o no con manejo de excepciones.
3) calcular el producto de compra del cliente con descuento (si es descontable)
4) mostrar la última actualización del producto
5) escriba la factura para el cliente con un nombre único
"""


def compra(Lista):
    L = Lista  # asignar lista con nombre de variable 'L'.
    a_nombre = input("por favor, escriba su nombre: ")
    print(f"\nHola {a_nombre}! Bienvenido a nuestra tienda electrónica.\nSeleccione el producto según su elección.")
    q = {}  # asignar diccionario vacío con nombre de variable 'q'.
    flag = "Y"
    while flag.upper() == "Y":  # Verifique y continue si flag es 'Y' o 'y'.
        producto = input("\n¿Qué producto quieres comprar? ")
        nombre_del_producto = producto.upper()  # Cambie el valor de 'string' en mayúsculas.

        if nombre_del_producto == L[0][0].upper() \
                or nombre_del_producto == L[1][0].upper() \
                or nombre_del_producto == L[2][0].upper():  # Verifique el nombre del producto ingresado por el usuario con el stock de la tienda.
            p = True
            while p == True:
                try:
                    p_cantidad = int(input(f"Cuantos {producto} Quieres comprar: "))
                    p = False
                except:  # se ejecuta, si el cliente ingresó un valor inesperado.
                    print("\t\t¡¡¡Error!!!\n¡¡¡Por favor ingrese un valor entero!!! ")
            if nombre_del_producto == L[0][0].upper() and p_cantidad <= int(L[0][2]):
                q[nombre_del_producto] = p_cantidad
            elif nombre_del_producto == L[1][0].upper() and p_cantidad <= int(L[1][2]):
                q[nombre_del_producto] = p_cantidad
            elif nombre_del_producto == L[2][0].upper() and p_cantidad <= int(L[2][2]):
                q[nombre_del_producto] = p_cantidad
            else:
                print(
                    f"\n¡¡¡Lo siento {a_nombre}!!!, {producto} está agotado.\nAgregaremos stock de {producto} más adelante. \nEsperemos que obtenga este producto después de la próxima compra.\n")

            flag = (input(f"{a_nombre} ¿Quieres comprar más productos?(Y/N)"))
        else:
            print(f"Lo siento {producto} no está disponible en nuestra tienda.")
            print("\n¡Elija entre los siguientes productos, por favor!")
            print("--------------------------------------------")
            print("PRODUCTO\t\tPRECIO\t\tCANTIDAD")
            print("--------------------------------------------")
            for i in range(len(L)):
                print(L[i][0], "\t\t", L[i][1], "\t\t",
                      L[i][2])  # imprime el nombre del producto actualizado por última vez, cantidad y precio.
            print("--------------------------------------------")

    print("\nUsted eligió artículos y su cantidad respectivamente:\n", q, "\n")
    '''
        En la siguiente operación:
        1) cambie cada valor de string en mayúsculas.
        2) verificar cuál es el producto ingresado por el cliente.
        3) ejecuta la condición respectiva si el producto es un 'teléfono', una 'computadora portátil' o un 'disco duro' ingresado por el cliente.
    '''
    f_cantidad = 0  # Cantidad final.
    for cuenta in q.keys():
        if cuenta.upper() == L[0][0].upper():  # ejecuta esta operación si el producto ingresado por el cliente es teléfono.
            p_precio = int(L[0][1])
            p_num = int(q[cuenta])
            p_cantidad = (p_precio * p_num)
            f_cantidad += (p_precio * p_num)
            print("\nCosto total por movil: ", p_cantidad)
        elif cuenta.upper() == L[1][0].upper():  # ejecuta esta operación si el producto ingresado por el cliente es laptop.
            l_precio = int(L[1][1])
            l_num = int(q[cuenta])
            l_cantidad = (l_precio * l_num)
            f_cantidad += (l_precio * l_num)
            print("Costo total por laptop: ", l_cantidad)
        else:  # ejecuta esta operación si el producto ingresado por el cliente es hdd.
            h_precio = int(L[2][1])
            h_num = int(q[cuenta])
            h_cantidad = (h_precio * h_num)
            f_cantidad += (h_precio * h_num)
            print("Costo total por HDD: ", h_cantidad)
    print("\nSu monto total descontable es: ", f_cantidad)

    '''
        En la siguiente operación:
        1) solicite al cliente el % de descuento esperado en el monto total de la compra.
        2) verifique el monto total de la compra que el cliente espera descontable o no.
        3) verificar el monto total de la compra si es descontable básico o no.
    '''
    disc = float(input("Por favor ingrese su descuento esperado (Solo en numero, sin '%'): "))
    dis = 0.0
    if (f_cantidad >= 5000) and (f_cantidad < 10000):
        descuento = disc
        if descuento <= 5.0:
            dis = (descuento * f_cantidad) / 100
            total = float(f_cantidad - dis)
            print("Obtuviste el " + str(disc) + "% de descuento y el importe es: ", dis)
        else:
            descuento = 5.0
            dis = (descuento * f_cantidad) / 100
            total = float(f_cantidad - dis)
            print("No obtuviste el descuento esperado del " + str(
                disc) + "% \nPorque su compra total no cumple con los criterios mínimos para el descuento del " + str(
                disc) + "%.")
            print("Obtuviste un descuento básico del 5% y el monto descontado es:", dis)
    elif f_cantidad >= 10000:
        descuento = disc
        if descuento <= 10.0:
            dis = (descuento * f_cantidad) / 100
            total = float(f_cantidad - dis)
            print("Obtuviste el descuento esperado del " + str(disc) + "% y el monto es: ", dis)
        else:
            descuento = 10.0
            dis = (descuento * f_cantidad) / 100
            total = float(f_cantidad - dis)
            print("No obtuviste el descuento esperado del " + str(
                disc) + "% \nPorque su compra total no cumple con los criterios mínimos para obtener un " + str(
                disc) + "% de descuento.")
            print("Obtuviste un descuento básico del 10% y el monto descontado es:", dis)
    else:
        descuento = 0.0
        total = float(f_cantidad)
        print("No obtuviste el descuento esperado del " + str(
            disc) + "% \nPorque su compra total no cumple con los criterios mínimos para obtener un " + str(
            disc) + "% de descuento.")
    print("Su monto a pagar es: ", total)

    '''
        En la siguiente operación:
        1) escriba cada nombre de participación único que incluya también la fecha y hora actuales con el nombre del cliente.
        2) escriba el nombre del producto de compra y los detalles en el archivo (factura).
        3) escriba un monto descontado y el monto final a pagar en el archivo (factura).
    '''

    import datetime  # importar la fecha y hora del sistema para crear un nombre de factura único.
    dt = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
        datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
    factura = str(dt)  # factura unica
    t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day)  # Fecha
    d = str(t)  # Fecha
    u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
        datetime.datetime.now().second)  # Hora
    e = str(u)  # Hora

    file = open(factura + " (" + a_nombre + ").txt", "w")  # Genere un nombre de factura único y ábralo en modo escritura.
    file.write("=============================================================")
    file.write("\nVICTOR STORE\t\t\t\tFACTURA")
    file.write("\n\nFactura: " + factura + "\t\tFecha: " + d + "\n\t\t\t\t\tHora: " + e + "")
    file.write("\nNombre del cliente: " + str(a_nombre) + "")
    file.write("\n=============================================================")
    file.write("\nPARTICULAR\tCANTIDAD\tPRECIO POR UNIDAD\tTOTAL")
    file.write("\n-------------------------------------------------------------")

    for cuenta in q.keys():  # En este bucle, Se escribe un archivo solo aquellos productos que compra el usuario.
        if cuenta == "MOVIL":
            file.write(
                str("\n" + str(cuenta) + " \t\t " + str(q['MOVIL']) + "\t\t " + str(L[0][1]) + "\t\t\t " + str(p_cantidad)))
        elif cuenta == "LAPTOP":
            file.write(str(
                "\n" + str(cuenta) + " \t\t " + str(q['LAPTOP']) + "\t\t " + str(L[1][1]) + "\t\t\t " + str(l_cantidad)))
        else:
            file.write(
                str("\n" + str(cuenta) + " \t\t " + str(q['HDD']) + "\t\t " + str(L[2][1]) + "\t\t\t " + str(h_cantidad)))

    file.write("\n\n-------------------------------------------------------------")
    file.write("\n\t\t\tTu importe descontable: " + str(f_cantidad))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\t\t   Su monto con descuento del " + str(descuento) + "% es de: " + str(dis))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\t\t\t Su monto a pagar es: " + str(total))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\n\tMuchas gracias " + a_nombre + " por tus compras.\n\t\t¡Vuelva pronto!")
    file.write("\n=============================================================")
    file.close()
    return q
