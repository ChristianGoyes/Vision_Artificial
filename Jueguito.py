#Desarrollador: Christian D. Goyes
#Script: este programa le permite a dos jugadores ver quien lega primero a la meta 

#libraries
import os

from random import randint, uniform
#functions 
def Numeritoaleatorio():
    na = randint(1,6)
    return na
#main 

os.system("cls")

print("|     CARRERA DE NUMEROS    |")
print("|       (dos personas)      |")
print("|   Descripcion: uno a uno  |")
print("|   tiran los dados y hasta |")
print("|   que uno llegue primero  |")
print("| o supere la meta numerica |")
print("|    Selecciona el nivel    |")
print("|      1. Facil (50)        |")
print("|      2. Medio (75)        |")
print("|      3. Dificil (100)     |")
print("Please, enter any option (1-3): ")

NumeroMeta = 0

op = input()
if op == '1' :
    NumeroMeta=50
    print("Nivel facil, META: ",NumeroMeta)
elif op == '2' :
    NumeroMeta = 75
    print("Nivel Medio, META: ", NumeroMeta)
elif op == '3' :
    NumeroMeta = 100
    
else :
    print("::: Invalid option :::") 

os.system("cls")

print("|     CARRERA DE NUMEROS    |")
print("|       (dos personas)      |")
print("|         COMENZAMOS        |")
print("|   Para lanzar lo numeros  |")
print("|    presiona el numero 6   |")
print("| o supere la meta numerica |")
print("|   Nivel con meta: ", NumeroMeta ,"    |")
JUGADOR1 = 0
JUGADOR2 = 0
AcuJ1 = 0
AcuJ2 = 0
while True:
    print(":::=========================:::")
    print ("|   Tira el numero JUGADOR 1  |")
    JUGADOR1 = Numeritoaleatorio()
    AcuJ1 = AcuJ1 + JUGADOR1 
    print ("|        Tu numero es ",JUGADOR1 ,"     |")
    print ("|   Tu acumulado es : ", AcuJ1, "    |")
    print(":::-------------------------:::")
    print("|   Tira el numero JUGADOR 2  |")
    JUGADOR2 = Numeritoaleatorio()
    AcuJ2 = AcuJ2 + JUGADOR2 
    print ("|        Tu numero es ",JUGADOR2 ,"     |")
    print("|   Tu acumulado es : ", AcuJ2, "    |")

    if AcuJ1 >= NumeroMeta or AcuJ2 >= NumeroMeta:
        print(":::=========================:::")
        print("|        FIN DEL JUEGO        |")
        print("|     JUGADOR NUMERO 1 : ",AcuJ1,"  |")
        print("|     JUGADOR NUMERO 2 : ",AcuJ2,"  |")
        break 



