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

#condicion multiple
#si el cliente supera los 200 de compra obtendra los mejores asientos
if(total>200):
    print("por su compra obtendra los mejores asientos")
#fin_if

#si el cliente no supera los 200 no otendra los mejores asientos
if(total<200):
    print("lo sentimos, no pudo obtener los mejores asientos")
#fin_if

#si la compra realizada es igual a 550 se le agradecera
if(total==550):
    print("buena compra, muchas gracias")
#fin_if
