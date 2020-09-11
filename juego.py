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
def Revueltos2():
    nz = randint(1,6)
    return nz
def Revueltos3():
    nz = randint(1,6)
    return nz
def Revueltos4():
    nz = randint(1,6)
    return nz
    

#main
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
print ("|      ENTRE DOS JUGADORES     |")
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

os.system("cls")
print ("|==============================|")
print ("|            NIVELES           |")
print ("|      1.PRINCIPIANTES (50)    |")
print ("|      2.NORMAL        (75)    |")
print ("|      3.DIFICIL       (150)   |")
print ("|==============================|")
print ("|   SELECCIONA EL NIVEL (1-3)  |")
print ("|==============================|")
Numerometa = 0
op1 = input () 
if  op1 == '1' :
    Numerometa = 50
elif op1 == '2' :
    Numerometa = 75
elif op1 == '3' :
    Numerometa = 150
else :
    print("::: Invalid option :::") 

Sum_J1 = 0
Sum_J2 = 0

os.system("cls")
print ("|==============================|")
print ("|        JUEGO DE DADOS        |")
print ("|     NIVEL SELECCIONADO :",Numerometa,"  |")
print ("|    PARTICIPANTE 1 :",Sum_J1,"   |")
print ("|    PARTICIPANTE 2 :",Sum_J2,"   |")
print ('|       Presiona "ENTER"       |')
print ("|==============================|")
op = input ()


while Sum_J1 < Numerometa and Sum_J2 < Numerometa :
    DadoN1 = Revueltos1()
    DadoN2 = Revueltos2()
    DadoN3 = Revueltos3()
    DadoN4 = Revueltos4()
    os.system("cls")
    print ("|==============================|   ||P1|",Sum_J1,"||")
    print ("|         PARTICIPANTE 1       |   ||P2|",Sum_J2,"||")
    print ("|         ACUMULADO :",Sum_J1,"     |")
    print ('|     Presiona "ENTER" para    |')
    print ('|           tirar dados        |')
    print ("|==============================|")
    op = input ()
    os.system("cls")
    print ("|==============================|   ||P1|",Sum_J1,"||")
    print ("|         PARTICIPANTE 1       |   ||P2|",Sum_J2,"||")
    print ("|==============================|")
    print ("|  ||DADO 1 = ",DadoN1,"||            |")
    print ("|  ||DADO 2 = ",DadoN2,"||            |")
    Sum_J1 = Sum_J1 + DadoN1 + DadoN2
    print ("|  ||NUEVO ACUMULADO = ",Sum_J1,"||        |")
    print ("|==============================|")
    op = input ()

    os.system("cls")
    print ("|==============================|   ||P1|",Sum_J1,"||")
    print ("|         PARTICIPANTE 2       |   ||P2|",Sum_J2,"||")
    print ("|         ACUMULADO :",Sum_J2,"      |")
    print ('|     Presiona "ENTER" para    |')
    print ('|           tirar dados        |')
    print ("|==============================|")
    op = input ()
    os.system("cls")
    print ("|==============================|   ||P1|",Sum_J1,"||")
    print ("|         PARTICIPANTE 2       |   ||P2|",Sum_J2,"||")
    print ("|==============================|")
    print ("|  ||DADO 1 = ",DadoN3,"||            |")
    print ("|  ||DADO 2 = ",DadoN4,"||            |")
    Sum_J2 = Sum_J2 + DadoN3 + DadoN4
    print ("|  ||NUEVO ACUMULADO = ",Sum_J2,"||   |")
    print ("|==============================|")
    op = input ()

os.system("cls")
print ("|==============================|")
print ("|         FIN DEL JUEGO        |")
print ("|==============================|")
print ("|       EL GANADOR ES ....     |")
print ("|==============================|")
op = input()

if Sum_J1 > Sum_J2 :

    os.system("cls")
    print ("|==============================|   ||P1|",Sum_J1,"||")
    print ("|   FELICITACIONES JUGADOR 1   |   ||P2|",Sum_J2,"||")
    print ("|==============================|")
    print ("|     TU PUNTAJE  ES DE : ",Sum_J1,"      |")
    print ("|==============================|")
    op = input()

elif Sum_J2>Sum_J1 :
    os.system("cls")
    print ("|==============================|   ||P1|",Sum_J1,"||")
    print ("|   FELICITACIONES JUGADOR 2   |   ||P2|",Sum_J2,"||")
    print ("|==============================|")
    print ("|     TU PUNTAJE  ES DE : ",Sum_J2,"      |")
    print ("|==============================|")
    op = input()
else :
    os.system("cls")
    print ("|==============================|")
    print ("|   AMBOS JUGADORES EMPATARON  |")
    print ("|==============================|")
    print ("|     SU PUNTAJE  ES DE : ",Sum_J1,"  |")
    print ("|     SU PUNTAJE  ES DE : ",Sum_J2,"  |")
    print ("|==============================|")
    op = input()

os.system("cls")
print ("|==============================|")
print ("|           GAME OVER          |")
print ("|==============================|")