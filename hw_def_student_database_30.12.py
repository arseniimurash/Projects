from os import system

import random
# когда вызываем только опеределенную функцию (from ...), то пишем просто саму функцию (например, system())
# когда импортируем сразу весь модуль/библиотеку (import ...), то упоминаем через точку ("библиотека.функция" / random.randint)

from faker import Faker
# ЕСЛИ НЕОБХОДИМО ДОБАВИТЬ СТОРОННЮЮ БИБЛЕТОТЕКУ, ТО ЗАХОДИМ НА "pypi.org", НАХОДИМ НУЖНУЮ, КОПИРУЕМ КОМАНДУ ДЛЯ ТЕРМИНАЛА, 
# ОТКРЫВАЕМ ТЕРМИНАЛ (МОЖНО ПРЯМО В ПРОГРАММЕ), ВВОДИМ КОМАНДУ (В ДАННОМ СЛУЧАЕ "pip install Faker"), Python автоматически загружает и устанавливает библиотеку

from time import sleep

########################################
stud_names = []  # str
stud_grades = [] # int
stud_years  = [] # float
fake = Faker()   # в скобках можно указать локализацию по стране и тогда будут соответствующие имена или адреса, например: Faker('ru')
# создали такую переменную "fake = Faker()", т.к. так указано в документации к этой библитеке на сайте

### HW 1
def genStudents (amount = 10):  # =10 не влияет, количество задаем при вызове функции
    for i in range(amount): 
        stud_names.append(fake.name())
        stud_years.append(random.randint(1,5))  
        stud_grades.append(round(random.uniform(5.0, 10.0), 2))  # round(x,y) - x это что мы округляем, а y это сколько символов после запятой



def printStudents():
    for i in range(len(stud_names)):
        print("-"*42)
        print(f"{stud_names[i]:30} | {stud_years[i]:2} | {stud_grades[i]}")
    print("-"*42)
    print()
# при форматировании "f", когда прописываем переменные, можно поставить двоеточие ":", тем самым зарезервировать место после переменной перед следующей        


def printMenu():
    print("### STUDENTS DATABASE")
    print("1. Show student list")
    print("2. Add a student")
    print("3. Edit a student")
    print("4. Remove a student")
    print("5. Choose specific students")
    print("0. Exit")
    print("####################")
    print()
    option = int(input("Select a number: "))
    return option # когда будет выбрано число, функция вернет это значение, для этого сделаем переменную в цикле

def addStudent():
    s_name = input("Enter a new student name: ")
    s_year = int(input("Enter a new student year: "))
    s_grade = float(input("Enter a new student grade: "))

    stud_names.append(s_name)
    stud_years.append(s_year)
    stud_grades.append(s_grade)

def removeStudent():
    s_name = input("Enter the name of the student to delete: ")
    s_index = -1
    for i in range(len(stud_names)):
        if stud_names[i] == s_name:
            s_index = i   # запоминаем индекс студент в переменную (найденного по имени)
            break
    if s_index >= 0:
        stud_names.pop(s_index)
        stud_years.pop(s_index)
        stud_grades.pop(s_index)

### HW 2
def editStudent():
    s_name = input("Enter the name of the student to edit: ")
    s_index = -1
    for i in range(len(stud_names)):
        if stud_names[i] == s_name:
            s_index = i
            break
    if s_index >= 0:
        question = input("""
        What do you want to edit ?

        a. Year
        b. Grade

        Select a letter: """)
        if question == "a":
            print()
            new_year = int(input("Write a year: "))
            if new_year > 0 and new_year <= 5:
                stud_years.insert(s_index, new_year)
            else:
                print()
                print("Wrong year !")
                sleep(2)
        elif question == "b":
            print()
            new_grade = float(input("Write a grade: "))
            if new_grade > 0 and new_grade <= 10:
                stud_grades.insert(s_index, new_grade)
            else:
                print()
                print("Wrong grade !")
                sleep(2)
        else:
            print()
            print("Wrong command !")
            sleep(2)

### HW 3
def specificStudents():
    question = input("""
        What do you want to see ?

        a. The Best student
        b. Range of students by grade

        Select a letter: """)

    if question == "a":
        s_index = ""
        for i in range(len(stud_grades)):
            if stud_grades[i] == max(stud_grades):
                s_index = i
                break
        print()
        print(f"The Best student is:\n\n\t {stud_names[s_index]:20} | {stud_years[s_index]:2} | {stud_grades[s_index]}")
        print()
    elif question == "b":
        print()
        val_1 = float(input(" What grade to start with: "))
        val_2 = float(input(" What grade to end with: "))
        if (val_1 and val_2) in range(1,11):
            print()
            print("Selected students:")
            for x in range(len(stud_grades)):
                if stud_grades[x] >= val_1 and stud_grades[x] <= val_2:
                    print(f"\n\n\t {stud_names[x]:20} | {stud_years[x]:2} | {stud_grades[x]}")
        else:
            print()
            print("Wrong range !")
            print()
        print()
    else:
        print()
        print("Wrong command !")
        print()




########################################
genStudents(5)
while True:
    system('cls')
    option =  printMenu()
    if option == 1:
        printStudents()
        input("hit enter to continue") # для удобства, чтобы через Enter продолжать взаимодействие и цикл быстро не стирал результат
    elif option == 2:
        addStudent()
    elif option == 3:
        editStudent()
    elif option == 4:
        removeStudent()
    elif option == 5:
        specificStudents()
        input("hit enter to continue")
    elif option == 0:
        break
########################################
