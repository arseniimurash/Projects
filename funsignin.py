def signIn(u,p):
    users = [{"Tom":"123456"}, {"Mary":"654321"},{"Anna":"111111"}]
    for user in users:
        for key, value in user.items():      # здесь user, т.к. первый цикл спускается до словаря в этом списке, соответственно переменная, которая контактирует со словарем = user
            if key == u and value == p:
                return {key: value}
    print("Wrong password or user name!")
    return None
