ang1 = int(input("Ingrese uno de los angulos: "))
ang2 = int(input("Ingrese otro angulo del triangulo: "))
z = 180-(ang1+ang2)
if (ang1==90) or (ang2==90) or (z==90):
    print("El triangulo ingresado es un triangulo Rectangulo")
elif (ang1<90) and (ang2<90) and (z<90):
    print("El triangulo ingresado es un triangulo acutangulo")
elif (ang1>90) or (ang2>90) or (z>90):
    print ("El triangulo ingresado es un triangulo obstusangulo")