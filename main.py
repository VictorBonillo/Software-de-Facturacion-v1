# Aqui empieza el programa.
import read
import purchase
import write

bienvenido = "Y"
while bienvenido.upper() == "Y":
    datos_del_archivo = read.read_file()
    funcion_compra = purchase.compra(datos_del_archivo)
    write.over_write(datos_del_archivo, funcion_compra)
    bienvenido = input("\n¿Eres un nuevo cliente esperando un producto? (y/n) ")
print("\n¡Gracias por su compra en nuestra tienda!")
print("Consulte su factura para conocer los detalles de su compra, \nque hemos creado en formato de archivo .txt")