import json

password = "xyz"


class Dealer:
    @staticmethod
    def add(name, brand, mileage, fuel1, fuel_capacity, seater, engine, price1, price2, stock):
        fuel2 = str(input("Is this car can run on any other fuel: "))
        with open('cars.txt', 'r') as file:
            car = json.load(file)
        with open('cars.txt', 'w') as file:
            if fuel2 == "no":
                car.append(
                    {"name": name, "brand": brand, "mileage": mileage, "fuel1": fuel1, "fuel_capacity": fuel_capacity,
                     "seater": seater, "engine": engine, "price1": price1, "price2": price2, "stock": stock})
                json.dump(car, file)
            elif fuel2 == "yes":
                fuel = input("On which other fuel does this model run: ")
                car.append(
                    {"name": name, "brand": brand, "mileage": mileage, "fuel1": fuel1, 'fuel2': fuel,
                     "fuel_capacity": fuel_capacity,
                     "seater": seater, "engine": engine, "price1": price1, "price2": price2, "stock": stock})
                json.dump(car, file)

    @staticmethod
    def stock_of_car():
        name = input("Enter the name of the car: ")
        st = input("Yes/No: ")
        with open('cars.txt', 'r') as file:
            cars = json.load(file)
            for car in cars:
                if car["name"] == name:
                    car['stock'] = st
        with open('cars.txt', 'w') as fo:
            json.dump(cars, fo)

    @staticmethod
    def remove(name: str):
        with open('cars.txt', 'r') as file:
            cars = json.load(file)
        for car in cars:
            if car['name'] == name:
                cars.remove(car)
        with open('cars.txt', 'w') as file:
            json.dump(cars, file)

    @staticmethod
    def find(name: str):
        with open('cars.txt', 'r') as file:
            cars = json.load(file)
            for car in cars:
                if car['name'] == name:
                    stock = car['stock'].capitalize()
                    print(
                        f"{car['name']} of {car['brand']} brand. Has mileage of {car['mileage']}km/l. It can run on {car['fuel1']}.Has a fuel capacity of {car['fuel_capacity']}l.It have {car['seater']} seats. It have {car['engine']} engine. Price is from {car['price1']} l to {car['price2']} l. Stock:{stock}")

    @staticmethod
    def allcar():
        with open('cars.txt', 'r') as file:
            cars = json.load(file)
            for car in cars:
                stock = car['stock'].capitalize()
                try:
                    print(
                        f"{car['name']} of {car['brand']} brand. Has mileage of {car['mileage']}km/l. It can run on {car['fuel1']} and {car['fuel2']}.Has a fuel capacity of {car['fuel_capacity']}l.It have {car['seater']} seats. It have {car['engine']} engine. Price is from {car['price1']} l to {car['price2']} l. Stock:{stock}")
                except:
                    print(
                        f"{car['name']} of {car['brand']} brand. Has mileage of {car['mileage']}km/l. It can run on {car['fuel1']}.Has a fuel capacity of {car['fuel_capacity']}l.It have {car['seater']} seats. It have {car['engine']} engine. Price is from {car['price1']} l to {car['price2']} l. Stock:{stock}")
