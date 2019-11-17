import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
frecuentador,precio_memoria,precio_chip="",0.0,0.0

#INPUT
frecuentador=os.sys.argv[1]
precio_memoria=float(os.sys.argv[2])
precio_chip=float(os.sys.argv[3])

#PROCESSING
total=round(precio_memoria+precio_chip)

#VERIFICADOR
frecuentador_comprensible=(total>15.5)

#OUTPUT
print("############################")
print("# BOLETA DE VENTA")
print("############################")
print("#")
print("# fecuentador         :",frecuentador)
print("# precio de memoria   :s/",precio_memoria)
print("# precio del chip     :s/",precio_chip)
print("total                 :s/",total)
print("############################")
print("el frecuentador es comprensible?",frecuentador_comprensible)

#condicion simple
#si el frecuentador supera los 15.5 tendra sorpresa
if(total>15.5):
    print("felicidades tendra una sorpresa")
#fin_if
