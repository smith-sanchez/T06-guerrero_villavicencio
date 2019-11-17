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

#VERIFICACDOR
pasajero_comprensible=(total>50)

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
print("¿el pasajero es comprensible?",pasajero_comprensible)

#condicion simple
#si el pasajero es comprensible se llevara un pasaje gratis
if( total>50 ):
    print("felicidades, ganaste un pasaje gratis")
#fin_if
