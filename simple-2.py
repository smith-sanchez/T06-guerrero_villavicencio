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
disponibilidad_del_comprador=(total<300)

#OUTPUT
print("########################")
print("# BOLETA DE VENTA")
print("########################")
print("#")
print("# cliente                     :",cliente)
print("# cantidad de rectificadores  :",cantidad)
print("# precio de cada rectificador :s/",pu)
print("# total                       :s/",total)
print("########################")
print("¿disponibilidad del comprador?",disponibilidad_del_comprador)

#condicion simple
#si el comprador tiene la disponibilidad
if(total>=150):
    print("por su gran compra se llevo uno extra")
#fin_if
