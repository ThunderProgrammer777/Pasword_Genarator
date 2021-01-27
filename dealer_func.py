import json

password = ("xyz")

class Dealer:
    @staticmethod
    def add(name, brand,mileage,fuel1,fuel_capacity,seater,engine,price1,price2):
        fuel2=str(input("Is this car can run on any other fuel: "))
        with open('cars.txt', 'r') as file:
            car = json.load(file)
        with open('cars.txt', 'w') as file:
            if fuel2=="no":
                car.append({"name": name, "brand": brand, "mileage":mileage, "fuel1":fuel1, "fuel_capacity": fuel_capacity, "seater":seater, "engine":engine, "price1":price1, "price2":price2})
                json.dump(car, file)

    @staticmethod
    def remove(name: str):
        with open('cars.txt', 'r') as file:
            books = json.load(file)
        for book in books:
            if book['name'] == name:
                books.remove(book)
        with open('cars.txt', 'w') as file:
            json.dump(books, file)

    @staticmethod
    def find(name: str):
        with open('cars.txt', 'r') as file:
            books = json.load(file)
            for book in books:
                if book['name'] == name:
                    print(f"{book['name']} Ph.{book['phone']}")

    @staticmethod
    def allnum():
        with open('cars.txt', 'r') as file:
            books = json.load(file)
            for book in books:
                print(f"{book['name']} Ph.{book['phone']}")
