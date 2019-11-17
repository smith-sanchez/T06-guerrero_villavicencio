import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente,cantidad,pu="",0,0.0

#INPUT
cliente=os.sys.argv[1]
cantidad=int(os.sys.argv[2])
pu=float(os.sys.argv[3])

#PROCESSING
total=round(cantidad*pu)

#VERIFICADOR
buena_ganancia=(total>120)

#OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# cliente         :",cliente)
print("# cantidad        :",cantidad)
print("# precio unitario :s/",pu)
print("total             :s/",total)
print("#######################")
print("se obtiene buena ganancia?",buena_ganancia)

#condicion simple
#si supera los 120 se llevara 2 productos gratis
if(total>120):
    print("por realizar esta compra se llevara dos productos totalmente gratis")
#fin_if
