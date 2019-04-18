print ("Los primeros 2 numeros del departamento indican el piso y los 2 restantes la ubicacion de este")
dep = int(input("Ingrese el numero del departamento que le interese: "))

dep = str(dep)
piso = int(dep[0:2])
num = int(dep[2:4])

if (num==0 or num==4):
    if (piso==1):
        print ("El precio es 80")
    elif (piso==20):
        print ("El precio es 320")
    else:
        print ("El precio es 200")
        
elif (num==3 or num==7):
    if (piso==20):
        print ("El precio es 460")
    elif (piso==1):
        print ("El precio es 115")
    else:
        print ("El precio es 288")
else:
    if (piso==20):
        print ("El precio es 400")
    elif (piso==1):
        print ("El precio es 100")
    else:
        print ("El precio es 250")
