import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente,precio_polo,precio_pantalon="",0.0,0.0

#INPUT
cliente=os.sys.argv[1]
precio_polo=float(os.sys.argv[2])
precio_pantalon=float(os.sys.argv[3])

#PROCESSING
total=round(precio_polo+precio_pantalon)

#VERIFICADOR
cliente_favorable=(total>400)

#OUTPUT
print("###################################")
print("# BOLETA DE VENTA")
print("###################################")
print("#")
print("# nombre del cliente        :",cliente)
print("# precio del polo           :",precio_polo)
print("# precio del  pantalon      :s/",precio_pantalon)
print("#total                      :s/",total)
print("###################################")
print("¿cliente es rendible?",cliente_favorable)

#condicion doble
#si el cliente es favorable se le pagara al taxi de regreso a su casa
if(total>=450):
    print("como supero los 450 le pagaremos el taxi")
#fin_if

#si el cliente tiene la disposicion de la oferta se le pagar el taxi
else:
    print("si lleva un cambio de ropa mas le pagaremos el taxi")
