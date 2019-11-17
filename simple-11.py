import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
consumidor,precio_moto,precio_auto="",0.0,0.0

#INPUT
consumidor=os.sys.argv[1]
precio_moto=float(os.sys.argv[2])
precio_auto=float(os.sys.argv[3])

#PROCESSING
total=round(precio_moto+precio_auto)

#VERIFICADOR
buena_compra=(total>50000)

#OUTPUT
print("################################")
print("# BOLETA DE VENTA")
print("################################")
print("#")
print("# consumidor         :",consumidor)
print("# precio de la moto  :s/",precio_moto)
print("# precio del auto    :s/",precio_auto)
print("total                :s/",total)
print("################################")
print("¿se da una buena compra?",buena_compra )

#condicion simple
#si consumidor realiza una buena compra participara del sorteo
if(total==60000):
    print("felicidades participara del sorteo, llene sus datos")
#fin_if
