from os import system
system("cls")


#########################################################
class Box:

    def __init__(self, value=None):         # С помощью __init__ задаем свойства (в данном случае value), self нужен, чтобы придать свойства самому объекту класса
            self.value = value

    def __lt__(self, other):                # С помощью методов сравнения помогаем определить поведение объектов
        return self.value < other.value     

    def __gt__(self, other):                # С помощью методов сравнения помогаем определить поведение объектов
        return self.value > other.value

    def __eq__(self, other):                # С помощью методов сравнения помогаем определить поведение объектов
        return self.value == other.value

    def isEmpty(self):
        if self.value == None:
            return True
        else:
            return False
#########################################################

# Задаем свойства

b1 = Box(1000)
b2 = Box(1000)


#########################################################

# Проверяем

if b1.isEmpty():
    print("The BOX1 is empty !")
if b2.isEmpty():
    print("The BOX2 is empty !")

if (b1 == b2) == True:
    print("True")
else:
    print("False")
    

