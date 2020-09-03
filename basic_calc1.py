#Developper: Christian D.Goyes
 

 import os
 os.system("cls")

print("Enter firs number: ")
 x = int(input())

 y = int(input("Enter second number"))

    print ("[1]. Add")
    print ("[2]. Sub")
    print ("[3]. Mult")
    print ("[4]. Div")
    print ("Plaease, enter any option (1-4): ")

    op = input()

    if op == '1' :
        print ("ADD is: ", x + y)
    elif op == '2' :
        print ("SUBST is: ", x - y)
    elif op == '3' :
        print ("MULT is: ", x * y)
    elif op == '4' :
        print ("DIV is: ", x / y)
    else :
        print ("::::::INVALID OPTION:::::::")
print("The add is: ", )
