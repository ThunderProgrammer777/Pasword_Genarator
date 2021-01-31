import json

final = []


class CustomFind:
    def __init__(self, brand, mileage, fuel1, fuel2, fuel_capacity, seater, engine, price1):
        self.brand = brand
        self.mileage = mileage
        self.fuel1 = fuel1
        self.fuel2 = fuel2
        self.fuel_capacity = fuel_capacity
        self.seater = seater
        self.engine = engine
        self.price1 = price1

    def find(self):
        with open('cars.txt', 'r') as file:
            cars = json.load(file)
            for car in cars:
                if car['brand'] == self.brand:
                    final.append(car)
                if car['mileage'] == self.mileage:
                    if car in final:
                        pass
                    else:
                        final.append(car)
                if car['fuel1'] == self.fuel1:
                    if car in final:
                        pass
                    else:
                        final.append(car)
                if car['fuel_capacity'] == self.fuel_capacity:
                    if car in final:
                        pass
                    else:
                        final.append(car)
                if car['seater'] == self.seater:
                    if car in final:
                        pass
                    else:
                        final.append(car)
                if car['engine'] == self.engine:
                    if car in final:
                        pass
                    else:
                        final.append(car)
                if car['price1'] < self.price1 > car['price2']:
                    if car in final:
                        pass
                    else:
                        final.append(car)
                try:
                    if car['fuel2'] == self.fuel2:
                        if car in final:
                            pass
                        else:
                            final.append(car)
                except:
                    pass
        for car in final:
            stock = car['stock'].capitalize()
            if car['price1'] < self.price1 > car['price2']:
                try:
                    print(
                        f"{car['name']} of {car['brand']} brand. Has mileage of {car['mileage']}km/l. It can run on {car['fuel1']} and {car['fuel2']}.Has a fuel capacity of {car['fuel_capacity']}l.It have {car['seater']} seats. It have {car['engine']} engine. Price is from {car['price1']} l to {car['price2']} l. Stock:{stock}")
                except:
                    print(
                         f"{car['name']} of {car['brand']} brand. Has mileage of {car['mileage']}km/l. It can run on {car['fuel1']}.Has a fuel capacity of {car['fuel_capacity']}l.It have {car['seater']} seats. It have {car['engine']} engine. Price is from {car['price1']} l to {car['price2']} l. Stock:{stock}")
        if len(final) == 0:
            print("Sorry! We can't found car like your requirements [!]___[!] ")


"wddwdddd"
