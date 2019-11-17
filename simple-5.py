import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
comprador,cajas_de_chocolate,precio_por_caja="",0,0.0

#INPUT
comprador=os.sys.argv[1]
cajas_de_chocolate=int(os.sys.argv[2])
precio_por_caja=float(os.sys.argv[3])

#PRECESSING
total=round(cajas_de_chocolate*precio_por_caja)

#VERIFICADOR
mucha_ganancia=(total>1500)

#OUTPUT
print("###################################")
print("# BOLETA DE VENTA")
print("###################################")
print("#")
print("# comprador          :",comprador)
print("# cajas de chocolate :",cajas_de_chocolate)
print("# precio por caja    :s/",precio_por_caja)
print("total                :s/",total)
print("###################################")
print("¿se obtiene mucha ganancia?",mucha_ganancia)

#condicion simple
#si se obtiene mucha ganancia
if(total<=2000):
    print("por su gran compra se le hara un descuento de 100 soles")
#fin_if
