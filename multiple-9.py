import  os
#BOLETA DE VENTA
#DECLARAR VARIABLES
nombre,precio_reloj,cantidad="",0.0,0

#INPUT
nombre=os.sys.argv[1]
precio_reloj=float(os.sys.argv[2])
cantidad=int(os.sys.argv[3])

#PROCESSING
total=round(cantidad*precio_reloj)

#OUTPUT
print("###################################")
print("# BOLETA DE VENTA")
print("###################################")
print("#")
print("# nombre del cliente        :",nombre)
print("# cantidad                  :",cantidad)
print("# precio por cada reloj     :s/",precio_reloj)
print("total                       :s/",total)
print("###################################")

#condicion multiple
#si el cliente supera su compra de 60 se llevara un reloj gratis
if(total==100):
    print("por su gran compra se llevara un reloj gratis")
#fin_if

#si la compra es menor a 90 no obtendra nada gratis
if(total<90):
    print("no obtendra el beneficio de llevarse un reloj gratis")
#fin_if

#si la compra es mayor a 100 tendra se le dara un reloj gratis y se le agradecera
if(total>100):
    print("obtuvo un reloj gratis, muchas gracias")
#fin_if
