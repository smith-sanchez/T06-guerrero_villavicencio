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

#VERIFICADOR
buena_ganacia=(total>2000)

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
print("¿se obtiene buena ganancia?",buena_ganacia)

#condicion simple
#si se obtiene buena ganancia tendra la opcion de ganarse una entrada al concierto
if(total==3000):
    print("hoy es su dia, se gano una entrada para el concierto")
#fin_if
