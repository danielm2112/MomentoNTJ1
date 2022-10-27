opcion=100
print("Supermercado Daniel`s")
print("1. Agregar producto: ")
print("2. Mostrar producto: ")
print("3. Buscar producto: ")
print("0. Salir")

producto={}

productos=[]

while(opcion !=0):
    opcion=int(input("Digite la opcion que desee: "))

    if(opcion==1):
        producto['codigo']=input("Digite el codigo del producto: ")
        producto['nombre']=input("Digite el nombre del producto: ")
        producto['precio']=input("Digite el precio del producto: ")
        productos.append(producto)
        

    elif(opcion==0):
        break
    elif(opcion==2):
        print(productos)
    elif(opcion==3):
        buscar=input("Que codigo deseas buscar: ")
        print("El codigo es: ",productos.index(buscar))
    else:
        print("Digite una opcion valida")   
else:
    print("")
