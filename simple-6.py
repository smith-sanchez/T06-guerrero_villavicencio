import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
clientes,cantidad_de_platos,precio_por_plato="",0,0.0

#INPUT
clientes=os.sys.argv[1]
cantidad_de_platos=int(os.sys.argv[2])
precio_por_plato=float(os.sys.argv[3])

#PROCESSING
total=round(cantidad_de_platos*precio_por_plato)

#VERIFICADOR
mucha_ganancia=(total<=50)

#OUTPUT
print("#########################")
print("# BOLETA DE VENTA")
print("#########################")
print("#")
print("# clientes           :",clientes)
print("# cantidad de platos :",cantidad_de_platos)
print("# precio por plato   :s/",precio_por_plato)
print("total                :s/",total)
print("#########################")
print("¿se obtiene poca ganancia?",mucha_ganancia)

#condicion simple
#si se obtiene poca ganancia
if(total>30):
    print("por su compra participara del sorteo de un auto")
#fin_if
