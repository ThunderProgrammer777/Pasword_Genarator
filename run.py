from dealer_func import Dealer as ph
from dealer_func import password as pas

Choice1 = ("""
l = list of all car model
a = add number
f = find a car model
d = delete a car model
s = mark the car in stock or not
q = quit
Your Choice = """)
person=str(input("Who is login to this program customer or dealer: "))
if person=='dealer':
    passs = input("Enter the password: ")
    if passs == pas:
        choice = str(input(Choice1))
        while choice != 'q':
            if choice == 'l':
                ph.allnum()
            elif choice == 'a':
                name = input("Enter the name of the model of the car: ")
                brand = str(input("Enter the brand name: "))
                mileage = float(input("What is the mileage of car per litre in km: "))
                fuel = str(input("Enter the type of fuel can used in this model: "))
                fuel_capacity = float(input("What is the fuel capacity of this model in litre: "))
                seater = int(input("How many seat are present in this car model: "))
                engine = input("Enter the name of the engine present in the car model: ")
                price1 = float(input("Enter the minimum price of the model of the car in lakh: "))
                price2 = float(input("Enter the maximum price of the model of the car in lakh: "))
                stock = str(input("Is this model in stock?[yes/no]:"))
                ph.add(name, brand, mileage, fuel, fuel_capacity, seater, engine, price1, price2, stock)
            elif choice == 'f':
                na = input("Enter the name of the car model which you want to find: ")
                ph.find(na)
            elif choice == 'd':
                nam = input("Enter the name of the car which you want to remove: ")
                ph.remove(nam)
            elif choice == 's':
                ph.stock_of_car()
            choice = str(input(Choice1))
    else:
        print("Wrong Password!!!")
elif person=='customer':
    pass