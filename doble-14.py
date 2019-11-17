import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
clientes,ne,pe="",0,0.0

#INPUT
clientes=os.sys.argv[1]
ne=int(os.sys.argv[2])
pe=float(os.sys.argv[3])

#PROCESSING
total=round(ne*pe)

#VERIFICADOR
clientes_buenos=(total>200)

#OUTPUT
print("##################################")
print("# BOLETA DE VENTA")
print("##################################")
print("#")
print("# cliente              :",clientes)
print("# cantidad de entradas :",ne)
print("# precio unitario      :s/",pe)
print("total                  :s/",total)
print("##################################")
print("¿son buenos clientes?",clientes_buenos)

#condicion doble
#si el cliente supera los 200 de compra obtendra los mejores asientos
if(total>200):
    print("por su compra obtendra los mejores asientos")
#fin_if

#si el cliente no supera los 200 de compra solo se le agaradece
else:
    print("gracias por su compra,disfrute su viaje")
