import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente,precio_mochila,cantidad="",0.0,0

#INPUT
cliente=os.sys.argv[1]
precio_mochila=float(os.sys.argv[2])
cantidad=int(os.sys.argv[3])

#procesing
total=round(precio_mochila*cantidad)

#vereficador
cliente_necesario=(total>120)

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
print("cliente necesario para el negocio?",cliente_necesario)

#condicion simple
#si el cliente supera 120 sera anotado como uno de nuestros mejores clientes
if(total>120):
    print("por su compra sera anotado en nuestra lista de mejores clientes")
#fin_if
