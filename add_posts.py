from os import system
system("cls")


def addPost(p1, p2, p3):
    new_post = {"title":p2, "body":p3}
    p1.insert(0,new_post)

###########################################################################
posts = [
    {
        "title": "About the importance of functional programming",
        "body": "Functional programming is ....."
    },
    {
        "title": "OOP programming brings classes and objects into the code",
        "body": "OOP is  ....."
    },
]
###########################################################################
title = input("Write a title: ")
body = input("Write a description: ")

addPost(posts, title, body)

print(posts)