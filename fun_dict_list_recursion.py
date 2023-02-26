from os import system
system("cls")


# HW 1. Три способа возвести число в степень:

# 1.
def square1(value):
    value = value * value
    return value

# 2.
def square2(value):
    value = pow(value, 2)
    return value

# 3.
def square3(value):
    value = value ** 2
    return value


# HW 2. General mark:

def generalMark(value):
    # с помощью метода values() достаем из словаря все значения, далее превращаем их в list, а после суммируем sum() весь list
    avg = sum(list(value.values()))
    avg = round(avg / 3, 2) # округляем результат
    value['gen'] = avg # здесь добавляем новое значение в словарь
    return value


marks = {'sem_1': 9.0, 'sem_2': 8.0, 'exam': 9.0}
generalMark(marks)

print(marks)


# HW 4. Recursion.

def increaseInt(n):
    if n != 1:
        print (n)
        n -= 1
        return increaseInt(n)
    else:
        return n

n = 7
n = increaseInt(n)

print (n)