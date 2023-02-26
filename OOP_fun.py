from os import system
system("cls")


class Container:
    is_empty = True
    value = None



def setContainerValue(c):
    if c.is_empty == True:
        c.value = 123
        c.is_empty = False
    return c



def unsetContainerValue(c):
    if c.is_empty == False:
        c.value = None
        c.is_empty = True
    return c


def printContainerValue(c):
    if c.is_empty == True:
        print ("Container is empty")
    elif c.is_empty == False:
        print(f"Container", c.value)


c = Container

setContainerValue(c)
printContainerValue(c)
unsetContainerValue(c)
printContainerValue(c)

#print(Container.is_empty)
#print(Container.value)
