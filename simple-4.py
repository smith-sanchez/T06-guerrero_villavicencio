import  os
#BOLETA DE VENTA
#DECLARAR VARIABLES
consumidor,articulo1,precio1,articulo2,precio2="","",0.0,"",0.0

#INPUT
consumidor=os.sys.argv[1]
articulo1=os.sys.argv[2]
precio1=float(os.sys.argv[3])
articulo2=os.sys.argv[4]
precio2=float(os.sys.argv[5])

#PROCESSING
precio_total=round(precio1+precio2)

#VERIFICADOR
consumidor_rendible=(precio_total>500)

#OUTPUT
print("##############################")
print("# BOLETA DE VENTA")
print("##############################")
print("#")
print("# consumidor   :",consumidor)
print("# articulo 1   :",articulo1,    "precio: s/",precio1)
print("# articulo 2   :",articulo2,    "precio: s/",precio2)
print("total          :s/",precio_total)
print("##############################")
print("¿el consumidor es rendible?",consumidor_rendible)

#condicion simple
#si el consumidor es rendible
if(precio_total==700):
    print("esta de suerte, tiene la opcion de elegir como regalo cualquier cosa de la tienda")
#fin_if
