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

#condicion multiple
#si supera los 120 se llevara 2 productos gratis
if(total>120):
    print("por realizar esta compra se llevara dos productos totalmente gratis")
#fin_if

#si no logra superar los 120 solo se le agradece por su compra
if(total<120):
    print("gracias por su compra")
#fin_if

#felicitar al cliente
if(total>200):
    print("felicidades, es uno de nuestros mejores clientes")
#fin_if
