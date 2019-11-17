import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
producto,costo,rebaja="",0.0,0.0

#INPUT
producto=os.sys.argv[1]
costo=float(os.sys.argv[2])
rebaja=float(os.sys.argv[3])

#PROCESSING
precio_total=round(costo-rebaja)

#OUTPUT
print("###############################")
print("# BOLETA DE VENTA ")
print("###############################")
print("#")
print("#NOMBRE DEL PRODUCTO :",producto)
print("# PRECIO PRODUCTO    :",costo)
print("REBAJA               :",rebaja)
print("costo total s/.      :",precio_total)
print("###############################")

#condicion multiple
#si el producto es de calidad
if(precio_total==250):
    print("por realizar esta compra se descuenta 10 soles")
#fin_if

#si la compra es mayor a 300 se le hara un descuento
if(precio_total>300):
    print("por realizar esta compra se descuenta 20 soles")
#fin_if

#si la compra es menor a 200 solo agradecer
if(precio_total<200):
    print("gracias")
#fin_if
