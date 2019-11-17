import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
consumidor,numero_de_galones,precio_por_galon="",0,0.0

#INPUT
consumidor=os.sys.argv[1]
numero_de_galones=int(os.sys.argv[2])
precio_por_galon=float(os.sys.argv[3])

#PROCESSING
total=round(numero_de_galones*precio_por_galon)

#VERIFICADOR
precio_bajo=(total<=120)

#OUTPUT
print("##########################")
print("# BOLETA DE VENTA")
print("##########################")
print("#")
print("# consumidor          :",consumidor)
print("# cantidad de galones :",numero_de_galones)
print("# precio por galon    :s/",precio_por_galon)
print("total                 :s/",total)
print("##########################")
print("¿se vendio a bajo precio?",precio_bajo)

#condicion doble
#si la compra es bajo solo decirle muchas gracias
if(total==80):
    print("muchas gracias")
#fin_if

#agradecer y hacerle saber al cliente que lleva buenos productos
else:
    print("buena compra, se lleva productos de calidad")
