Nombre=input("Ingrese el nombre del participante: ")
D=float(input("Ingrese la dificultad del piquero: "))
jueces=7
x=0
i=0
I=0
puntajes=[]
for i in range(0,jueces) :
    x=float(input("Ingrese puntaje del juez: "))
    x=x+I
    puntajes.append(x)
    if I==0:
        I=1/2
puntajes.sort()

puntajes.pop(-1)

puntajes.pop(0)


r=(puntajes[0]+puntajes[1]+puntajes[2]+puntajes[3]+puntajes[4])*(3/5)
r=r*D
print("El puntaje del participante",Nombre,"es de: ",r)