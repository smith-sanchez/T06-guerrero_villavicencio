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

#condicion multipe
#si se obtiene mucha ganancia se hara un descuento
if(total<=2000):
    print("por su gran compra se le hara un descuento de 100 soles")
#fin_if

#si la compra es igual a 1300 pagara mitad de precio
if(total==1300):
    print("esta de suerte, paga la mitad del precio")
#fin_if

#si la compra es mayor a 2000 hacerle saber algo
if(total>2000):
    print("es uno de nuestros mejores clientes")
#fin_if
