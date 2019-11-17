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

#condicion multiple
#si el frecuentador supera los 15.5 tendra sorpresa
if(total>15.5):
    print("felicidades tendra una sorpresa")
#fin_if

#si el precio no supera los 15.5 no tendra sorpresa y solo se le agradece
if(total==10):
    print("usted no supero el minimo,se le agradece por su compra")
#fin_if

#si el precio es mucho mayor que 100 tendra dos sorpresas
if(total>100):
    print("que gran dia el suyo, tendra doble sorpresa")
#fin_if
