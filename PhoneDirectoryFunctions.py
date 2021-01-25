import json


class Phone:
    @staticmethod
    def add(name: str, phone: int):
        with open('phone.txt', 'r') as file:
            books = json.load(file)
        with open('phone.txt', 'w') as file:
            books.append({"name": name, "phone": phone})
            json.dump(books, file)

    @staticmethod
    def remove(name: str):
        with open('phone.txt', 'r') as file:
            books = json.load(file)
        for book in books:
            if book['name'] == name:
                books.remove(book)
        with open('phone.txt', 'w') as file:
            json.dump(books, file)

    @staticmethod
    def find(name: str):
        with open('phone.txt', 'r') as file:
            books = json.load(file)
            for book in books:
                if book['name'] == name:
                    print(f"{book['name']} Ph.{book['phone']}")

    @staticmethod
    def allnum():
        with open('phone.txt', 'r') as file:
            books = json.load(file)
            for book in books:
                print(f"{book['name']} Ph.{book['phone']}")
