from os import system
system("cls")
from funsignup import *

u = ''
e = ''
p = ''

data = signUp(u, e, p)
system("cls")
for key, value in data.items():
    print(key, ':', value)
