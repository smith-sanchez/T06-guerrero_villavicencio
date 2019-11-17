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

#condicion multiple
#si la compra es bajo solo decirle muchas gracias
if(total==80):
    print("muchas gracias")
#fin_if

#si la compra es igual a 150 se le hechara 10 soles de gasolina a su vehiculo
if(total==150):
    print("le hecharemos 10 soles de gasolina a su vehiculo")
#fin_if

#si la compra supera los 100 tendra una super promocion
if(total>1000):
    print("tiene gasolina gratis para su vehiculo por una semana")
#fin_if
