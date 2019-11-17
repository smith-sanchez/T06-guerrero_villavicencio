import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
comprador,cantidad_de_pantalones,precio_por_pantalon="",0,0.0

#INPUT
comprador=os.sys.argv[1]
cantidad_de_pantalones=int(os.sys.argv[2])
precio_por_pantalon=float(os.sys.argv[3])

#PROCESSING
total=round(cantidad_de_pantalones*precio_por_pantalon)

#OUTPUT
print("##########################")
print("# BOLETA DE VENTA")
print("##########################")
print("#")
print("# comprador              :",comprador)
print("# cantidad de pantalones :",cantidad_de_pantalones)
print("# precio por pantalon    :s/",precio_por_pantalon)
print("total                    :s/",total)
print("##########################")

#condicion multiple
#si el comprador supera los 600 de compra tendra un viaje gratis a rio de janeiro
if(total>=700):
    print("se gano un viaje a rio de janeiro todo pagado")
#fin_if

#si es menor de 700 decirle que siga intentando
if(total<700):
    print("siga intentando")
#fin_if

#si su compra es igual a 700 de igual manera obtendra el vaije
if(total==700):
    print("que suerte, llego el limite y obtendra un viaje todo pagado")
#fin_if
