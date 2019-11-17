import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente,cl,pl,cb,pb="",0,0.0,0,0.0

#INPUT
cliente=os.sys.argv[1]
cl=int(os.sys.argv[2])
pl=float(os.sys.argv[3])
cb=int(os.sys.argv[4])
pb=float(os.sys.argv[5])

#PROCESSING
total=round(cl*pl+cb*pb)

#OUTPUT
print("############################")
print("# BOLETA DE VENTA")
print("############################")
print("#")
print("# cliente                :",cliente)
print("# cantidad de lapiceros  :",cl)
print("# precio por lapicero    :s/",pl)
print("# cantidad de borradores :",cb)
print("# precio por borrador    :s/",pb)
print("total                    :s/",total)
print("############################")

#condicion multiple
#si la compra es buena se llevara una entrada para la motocross
if(total>=900):
    print("felicidades, por su compra se ha ganado una entrada para la motocross")
#fin_if

#si la compra es menor a 900 no obtendra las entradas
if(total<900):
    print("que lastima, tenia la opcion de llevarse una entrada para la motocroos")
#fin_if

#si la compra es superior a 1500 auntomaticamente se entregara 3 entradas
if(total>1500):
    print("¡que buena compra',le daremos 3 entradas para la motocroos")
#fin_if
