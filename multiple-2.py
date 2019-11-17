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
print("########################")
print("# BOLETA DE VENTA")
print("########################")
print("#")
print("# cliente                     :",cliente)
print("# cantidad de rectificadores  :",cantidad)
print("# precio de cada rectificador :s/",pu)
print("# total                       :s/",total)
print("########################")

#condicion multiple
#si el comprador tiene la disponibilidad
if(total>=150):
    print("por su gran compra se llevo uno extra")
#fin_if

#si el comprador no tiene la disponibiladad no llevara nada gratis
if(total<=80):
    print("no pudo llevarse nada gratis")
#fin_if

#agradecer al cliente
if(total==500):
    print("exelente compra,vuelva pronto")
#fin_if
