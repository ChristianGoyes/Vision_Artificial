
#Desarrollador: Christian D. Goyes

#Script: este programa le permite operar dos números random.

#libraries
import os 


os.system("cls")

print("Enter first number: ")
x = int(input())
y = int(input("Enter second number: ")) 

print("[1]. Add")
print("[2]. Subs")
print("[3]. Mult")
print("[4]. Div")
print("Please, enter any option (1-4): ")
op = input()

if op == '1' :
    print("ADD is: ", x + y)
elif op == '2' :
    print("SUBST is: ", x - y)
elif op == '3' :
    print("MULT is: ", x * y)
elif op == '4' :
    print("DIV is: ", x / y)
else :
    print("::: Invalid option :::") 