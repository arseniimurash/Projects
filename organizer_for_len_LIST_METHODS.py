# METHODS FOR LIST: https://www.w3schools.com/python/python_ref_list.asp

from os import system
system('cls')

############### data ###############
tasks = [
    "Learn Python",     # 0
    "Become a DEV",     # 1
    "Buy a car"         # 2
]
############### data ###############

stop = True
while stop:
    ############### MENU ###############
    print("""🔢 MENU:
    1. Add a task
    2. Show tasks
    3. Remove task
    4. Clear TODO
    0. Exit
    """)
    step = input("Choose a number: ")

    ########### ADD task ###########
    if step == "1":
        system('cls')
        print()
        new_task = input("Add a task: ")
        if new_task not in tasks and new_task != "0":
            tasks.append(new_task)                          # append добавляет данные в конец списка
        else:
            print("This task already exists!")
        print("✅ TODO list (", len(tasks), "): ")          # len показывает длину списка
        for i in range(len(tasks)):                         # len говорит range идти по всей длине списка, т.е если добавить или убрать, то изменения отразятся автоматически
            print("\t","🟠",i, ">", tasks[i])              # \t это отступ
        print()
        print("⬜"*20)
        print()
        
    ########## print the tasks #########
    if step == "2":
        system('cls')
        print()
        print("✅ TODO list (", len(tasks), "): ")
        for i in range(len(tasks)):
            print("\t","🟠",i, ">", tasks[i])
        print()
        print("⬜"*20)
        print()
    ########## print the tasks #########

    ########## remove task #########
    if step == "3":
        system('cls')
        print()
        remove_task = int(input("What task do you want to remove?: "))
        tasks.pop(remove_task)                              # pop этот удалить опеределенный элемент списка по индексу
        print("✅ TODO list (", len(tasks), "): ")
        for i in range(len(tasks)):
            print("\t","🟠",i, ">", tasks[i])
        print()
        print("⬜"*20)
        print()
    ########## remove task #########

    ########## clear todo #########
    if step == "4":
        system('cls')
        print()
        clear_all_tasks = input("🔄 Are you sure to clear all tasks? (y/n): ")
        if clear_all_tasks == "y":
            tasks.clear()                                     # clear удаляет весь список
            print("✅ TODO list (", len(tasks), "): ")
            for i in range(len(tasks)):
                print("\t","🟠",i, ">", tasks[i])
            print()
            print("⬜"*20)
            print()
        else:
            print("OK! So choose a number in MENU 🔽")
            print()
    ########## clear todo #########

    ############# exit #############
    if step == "0":
        system('cls')
        stop = False
        print("Bye! Have a nice day! 👋")
        print()
    ############# exit #############


    ############### MENU ###############

