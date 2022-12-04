from os import system
system('cls')

############# DATA LISTS #############
students_first_name = []
students_last_name = []
students_age = []
student_mark = []
############# DATA LISTS #############

############# DATA INPUT #############
stop = True
while stop:
    new_data = input("""
📝 Enter student details in this format 🔽 
        |name surname age grade|
▶  Details: """)
    if new_data != "":
        new_data_list = new_data.split()                    # split() разбивает данные str и делает из них список (ориентируясь по пробелам): каждое значение после пробела = новая ячейка (индекс)
        if int(new_data_list[2]) in range(18, 31) and int(new_data_list[3]) in range(1, 11):     # in list value = str and it needs to convert in int that we can compare it in range
            students_first_name.append(new_data_list[0])
            students_last_name.append(new_data_list[1])
            students_age.append(new_data_list[2])
            student_mark.append(new_data_list[3])
            print()
            print("🆕 STUDENTS INFO:\n")
            for i in range(len(students_first_name)):
                print("\t", i, "➡ ", students_first_name[i], students_last_name[i], students_age[i], student_mark[i])
                print()
        else:
            print("This student can't be in database!")
    else:
        stop = False
    print("➖"*20)
############# DATA INPUT #############
    
