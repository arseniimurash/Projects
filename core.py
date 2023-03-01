class App:
    name = "The Game"
    version = "1.1.0"
    author = "Tom"
    email = "tom.app@example.com"
    year = "2023"
    rating = "5"


def appInfo():
    print(f"Name of the application: {App.name}\nVersion: {App.version}\nAuthor: {App.author}\nContacts: {App.email}\nRelease: {App.year}\nRating: {App.rating}\n")
