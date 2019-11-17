import  os
#BOLETA DE VENTA
#DECLARAR VARIBLES
cliente, cantidad,pu="",0,0.0

#INPUT
cliente=os.sys.argv[1]
cantidad=int(os.sys.argv[2])
pu=float(os.sys.argv[3])

#PROCESSING
total=round(cantidad*pu)

#OUTPUT
print("######################")
print("# BOLETA DE VENTA")
print("######################")
print("#")
print("# cliente             :",cliente)
print("# cantidad de laptops :",cantidad)
print("# precio unitario     :s/",pu)
print("total                 :s/",total)
print("######################")

#condicion multiple
#si se obtiene buena ganancia tendra la opcion de ganarse una entrada al concierto
if(total==3000):
    print("hoy es su dia, se gano una entrada para el concierto")
#fin_if

#si la compra es menor a 3000 no tendra las entradas
if(total<3000):
    print("no tendra la oportunidad de ir al concierto :(")
#fin_if

#agradecer al cliente
if(total>3000):
    print("buena compra, se lleva productos de calidad")
#fin_if
