import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente,precio,numero_producto="",0.0,0

#INPUT
cliente=os.sys.argv[1]
precio=float(os.sys.argv[2])
numero_libros=int(os.sys.argv[3])

#PROCESSING
total=round(numero_libros*precio)

#VERIFICADOR
gasto_necesario=(total>50)

#OUTPUT
print("############################")
print("# BOLETA DE VENTA")
print("############################")
print("#")
print("# el nombre el ciente es :",cliente)
print("# precio del libro es    :s/",precio)
print("# numero de libros       :",numero_libros)
print("total                    :s/",total)
print("############################")
print("el cliente gasto lo necesario?",gasto_necesario)

#condicion simple
#si supera los 50 obtendra viaje a Kuelap
if(total>=50):
    print("obtuvo su viaje a Kuelap")
#fin_if
