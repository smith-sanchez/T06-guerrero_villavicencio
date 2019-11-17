import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
consumidores,cantidad,pt="",0,0.0

#INPUT
consumidores=os.sys.argv[1]
cantidad=int(os.sys.argv[2])
precio_tickets=float(os.sys.argv[3])

#PROCESSING
total=round(cantidad*precio_tickets)

#OUTPUT
print("######################")
print("# BOLETA DE VENTA")
print("######################")
print("#")
print("# consumidores     :",consumidores)
print("# cantidad         :",cantidad)
print("# precio unitario  :s/",precio_tickets)
print("total              :s/",total)
print("######################")

#condicion multiple
#si esta disponible la venta obtendra los tickets
if(total<10):
    print("lo sentimos, no tiene el dinero suficiente para obtener estos tickets")
#fin_if

#si supera el limite obtiene los tickets
if(total>10):
    print("usted ha ganado los tickets")
#fin_if

#agradecer al cliente por su compra
if(total>40):
    print("le damos las gracias por esta compra")
#fin_if
