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

#VERIFICADOR
cliente_rendible=(total>60)

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
print("¿cliente es rendible?",cliente_rendible)

#condicion doble
#si el cliente supera su compra de 60 se llevara un reloj gratis
if(total==100):
    print("por su gran compra se llevara un reloj gratis")
#fin_if

#si la compra no alcanza el limite que vuelva intentarlo
else:
    print("no alcanzo el limite, siga intentando")
