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

#condicion multiple
#si se obtiene mucha ganancia pariticipara del sorteo
if(total>30):
    print("por su compra participara del sorteo de un auto")
#fin_if

#si la compra es menor igual a 100 decir los beneficios que hubiese obtenido
if(total<=100):
    print("si su compra hubiese sido mayor a 100 se le entregara dos boletos para la participacion del auto")
#fin_if

#agradecer al cliente
if(total>150):
    print("gracias, vuelva pronto")
#fin_if
