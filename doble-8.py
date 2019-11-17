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

#VERIFICADOR
buena_venta=(total>800)

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
print("¿se da una buena venta?",buena_venta)

#condicion doble
#si la venta es buena se llevara una entrada para la motocross
if(total>=900):
    print("felicidades, por su compra se ha ganado una entrada para la motocross")
#fin_if

#si la compra no es buena no obtendra las entradas
else:
    print("lo sentimos, su compra es baja y no tiene la opcion de llevarse una entrada para la motocross")
