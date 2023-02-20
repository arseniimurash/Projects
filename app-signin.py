from os import system
system("cls")
from funsignin import *

u = input("User name: ")
p = input("Password: ")

system("cls")
print(signIn(u, p))

