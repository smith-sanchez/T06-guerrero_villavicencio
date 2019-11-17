import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente,precio_mochila,cantidad="",0.0,0

#INPUT
cliente=os.sys.argv[1]
precio_mochila=float(os.sys.argv[2])
cantidad=int(os.sys.argv[3])

#PROCESSING
total=round(precio_mochila*cantidad)

#OUTPUT
print("############################")
print("# BOLETA DE VENTA")
print("############################")
print("#")
print("# el nombre el ciente es  :",cliente)
print("# precio de la mochila es :s/",precio_mochila)
print("# numero de mochilas      :",cantidad)
print("total                     :s/",total)
print("############################")

#condicion multiple
#si el cliente supera 120 sera anotado como uno de nuestros mejores clientes
if(total>120):
    print("por su compra sera anotado en nuestra lista de mejores clientes")
#fin_if

#si no supera 120 sera anotado como un cliente de paso
if(total<120):
    print("cliente de paso")
#fin_if

#si su compra es menor a 50 solo se le dira gracias
if(total<30):
    print("gracias")
#fin_if
