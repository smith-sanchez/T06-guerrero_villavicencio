import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
nombre,producto1,precio_p1,producto2,precio_p2="","",0.0,"",0.0

#INPUT
nombre=os.sys.argv[1]
producto1=os.sys.argv[2]
precio_p1=float(os.sys.argv[3])
producto2=os.sys.argv[4]
precio_p2=float(os.sys.argv[5])

#PROCESSING
total=round(precio_p1+precio_p2)

#VEREFICADOR
total_suficiente=(total>200)

#OUTPUT
print("############################")
print("# BOLETA DE VENTA")
print("############################")
print("#")
print("# el nombre el ciente es:       :",nombre)
print("# producto 1 :",precio_p1," precio:",precio_p1)
print("# producto 2 :",precio_p2," precio:",precio_p2)
print("total                 :s/",total)
print("############################")
print("el total del precio es suficiente?",total_suficiente)

#condicion simple
#si gasta lo suficiente tendra premio sorpresa
if(total>250):
    print("que suerte', tendra un premio sorpresa este fin de semana")
#fin_if
