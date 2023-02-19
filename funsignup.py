import re


# re - это модуль стандартной библиотеки Python, который предоставляет функции для работы с регулярными выражениями.
# Регулярные выражения - это мощный инструмент для работы с текстом, который позволяет искать и извлекать информацию из строк на основе шаблонов.
# Модуль re содержит функции для работы с регулярными выражениями, такие как match(), search(), findall(), split(), sub() и другие.





# используем методы 1-isalnum() и 2-isascii() для проверки на содержание только цифр и букв(1) и букв только из ACSII(2) - латинских.


##########################################################################################
def signUp(u, e, p):
    u = input("User name: ")
    if all(a.isalnum() and a.isascii() for a in u) and 5 <= len(u) <= 12:
        ##############################
        e = input("E-mail: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", e):
            ##############################
            p = input("Password: ")
            if len(p) >= 8:
                data = {"User": u, "E-mail": e, "Password": p}
            ##############################
            else:
                print("You need to enter a correct password with at least 8 characters.")
        else:
            print("You need to enter a correct e-mail address.")
    else:
        print("You need to enter from 5 to 12 characters using only latin letters and/or digits.")
    ##############################
    return data
##########################################################################################



