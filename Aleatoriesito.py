#Desarrollador: Christian D. Goyes
#Script: este programa le permite operar dos números random.
#randint => Genera números Z.
#uniform => Genera números R.
#libraries
import os
from  random  import randint, uniform 
#functions
def rand_integer():
    nz = randint(1,10)
    return nz
def rand_real():
    nr = uniform(1,10)
    return nr
def number_list():
    i = 1
    while i <=10 :
        x = randint(1,100)
        print(x)
        i=i+1
#main
os.system("cls")
z = rand_integer()
r = rand_real()
print("the Z number is : ", z)
print("the R number is : ", r)
print(":::::::::::::::::::::::::::")
number_list()


