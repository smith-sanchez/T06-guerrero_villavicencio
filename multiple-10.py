import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente,precio_polo,precio_pantalon="",0.0,0.0

#INPUT
cliente=os.sys.argv[1]
precio_polo=float(os.sys.argv[2])
precio_pantalon=float(os.sys.argv[3])

#PROCESSING
total=round(precio_polo+precio_pantalon)

#OUTPUT
print("###################################")
print("# BOLETA DE VENTA")
print("###################################")
print("#")
print("# nombre del cliente        :",cliente)
print("# precio del polo           :",precio_polo)
print("# precio del  pantalon      :s/",precio_pantalon)
print("#total                      :s/",total)
print("###################################")

#condicion multiple
#si el cliente es favorable se le pagara al taxi de regreso a su casa
if(total>=450):
    print("como supero los 450 le pagaremos el taxi")
#fin_if

#si la compra supera los 500 se le dira una frase y se le pagare el taxi de regreso
if(total>500):
    print("hoy es su dia, le pagaremos el taxi de regreso")
#fin_if

#si la compra es inferior a 450 agredecer al cliente
if(total<450):
    print("Gracias, vuelva pronto")
#fin_if
