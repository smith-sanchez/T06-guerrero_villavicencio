import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
pasajero,na,va="",0,0.0

#INPUT
pasajero=os.sys.argv[1]
na=int(os.sys.argv[2])
va=float(os.sys.argv[3])

#PROCESSING
total=round(na*va)

#OUTPUT
print("########################")
print("# BOLETA DE VENTA")
print("########################")
print("#")
print("# pasajero              :",pasajero)
print("# numero de asientos    :",na)
print("# valor de cada asiento :s/",va)
print("# total                 :s/",total)
print("########################")

#condicion multiple
#si el pasajero es comprensible
if(total>50):
    print("felicidades, ganaste un pasaje gratis")
#fin_if

#si la compra es menor que 50 hacerle saber al cliente de la promocion
if(total<50):
    print("si compras otro dos pasajes automaticamente te llevas uno gratis")
#fin_if

#agredecer al cliente y decirle que gano un pasaje
if(total==80):
    print("muchas gracias,gano un pasaje gratis")
