def RUT():
    base = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7]
    rut = input("Ingrese su RUT (sin verificador):\n")
    rut = rut[::-1]
    suma = 0
    x = 0
    y = 0
    verificador = 12
    while x < len(rut):
        y = int(rut[x])*int(base[x])
        suma = suma + y
        x = x + 1
    print (suma)
    v = 11 - (suma % 11)
    
    if 0 < v < 10:
        verificador = v
    elif v == 11:
        verificador = 0
    elif v == 10:
        str(verificador)
        verificador = "K"
        
    print ("Su digito verificador es: ",verificador)   
    print ("Su RUT es: ",rut[::-1],"-",verificador)
    
RUT()