#Desarrollador: Christian D. Goyes
#Script: Este programa trata sobre una competencia donde
#        dos jugadores tiran de dos dados y el primero en
#        llegar a la meta ganara
#libraries
import os

from  random  import randint, uniform 

#functions
def Revueltos1():
    nz = randint(1,6)
    return nz 
     
def Menu1():
    os.system("cls")
    print ("|==============================|")
    print ("|            NIVELES           |")
    print ("|      1.PRINCIPIANTES (50)    |")
    print ("|      2.NORMAL        (75)    |")
    print ("|      3.DIFICIL       (150)   |")
    print ("|==============================|")
    print ("|   Preciona 0 para salir      |")
    print ("|==============================|")


def Menu_2():
    os.system("cls")
    print ("|==============================|")
    print ("|        JUEGO DE DADOS        |")
    print ("|     SELECCIONA LA CANTIDAD   |")
    print ("|        DE PARTICIPANTES      |")
    print ("|            (1 a 5)           |")
    print ("|==============================|")
    print ("|   Preciona 0 para salir      |")
    print ("|==============================|")
    

#main
i = 0

os.system("cls")
print ("|==============================|")
print ("|            SALUDOS           |")
print ("|==============================|")
op = input ()

os.system("cls")
print ("|==============================|")
print ("| BIENVENIDO AL JUEGO DE DADOS |")
print ("|==============================|")
op = input ()

os.system("cls")
print ("|==============================|")
print ("|        ENTRE JUGADORES       |")
print ("|     COMPETIRÁN QUIEN LLEGA   |")
print ("|       PRIMERO A LA META      |")
print ("|==============================|")
op = input ()


os.system("cls")
print ("|==============================|")
print ("|     SELECCIONEN EL NIVEl     |")
print ("|     AL QUE DESEAN ACCEDER    |")
print ("|==============================|")
op = input ()

while True:
        try:
            Menu1()
            print ("|==============================|")
            Nivel = int(input("|   SELECCIONA EL NIVEL (1-3)  |"))
            print ("|==============================|")
            if 0 <= Nivel <=3:
                break
            else:
                print ("|Digite un numero mayor o igual que 0    |")
        except ValueError:
            print ('Error: debe digitar un numero entero valido')

if  Nivel == 1 :
    Numerometa = 50
elif Nivel == 2 :
    Numerometa = 75
elif Nivel == 3 :
    Numerometa = 150

while True:
    try:
        Menu_2()
        print ("|==============================|")
        Part = int(input("|   SELECCIONA LA CANTIDAD DE JUGADORES (1-5)  |"))
        print ("|==============================|")
        if 0 <= Part <=5:
            break
        else:
            print ("|Digite un numero mayor o igual que 0    |")
    except ValueError:
        print ('Error: debe digitar un numero entero valido')
            
resultado=[]

for i in range(1, Part+1):
    NuevoDato = 0
    resultado.append(NuevoDato)
i = 0
        
while resultado[i] <= Numerometa:
    os.system("cls")
    print ("|==============================|")
    print ("| Tira enter para lanzar dados |")
    print ("|==============================|")
    input()
    d1 = Revueltos1()
    d2 = Revueltos1()
    print ("|==============================|")
    print ("|           Jugador",i+1,"          |")
    print ("|   Tu lanzamiento fue de      |")
    print ("|    Dado 1 :",d1,"Dado 2 :",d2,"    |")
    print ("|==============================|")
    print ("|  Total acumulado jugador ",i+1,"  |")
    resultado[i] = resultado[i] + d1 + d2
    print ("|         ACUMULADO :",resultado[i],"  |")
    print ("|==============================|")
    print ("|====ENTER PARA CONTINUAR======|")
    print ("|==============================|")

    input()
    if resultado[i] >= Numerometa:

        print ("|==============================|")
        print ("|         FELICITACIONES       |")
        print ("|        JUEGO COMPLETADO      |")
        print ("|        GANADOR JUGADOR ",i+1,"      |")
        print ("|==============================|")
        print ("|   Preciona ENTER para salir  |")
        print ("|==============================|")
        input()
        break
    i = i + 1
    if i == Part:
        i = 0

#=================================================================================================

os.system("cls")
print ("|==============================|")
print ("|         FIN DEL JUEGO        |")
print ("|==============================|")
op = input()

