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

#VERIFICADOR
disponibilidad_de_los_consumidores=(total<30)

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
print("¿la venta esta disponible?",disponibilidad_de_los_consumidores)

#condicion doble
#si esta disponible la venta obtendra los tickets
if(total<10):
    print("lo sentimos, no tiene el dinero suficiente para obtener estos tickets")
#fin_if

#si supera el limite obtiene los tickets
else:
    print("usted ha ganado los tickets")
