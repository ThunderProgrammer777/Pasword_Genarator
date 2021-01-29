from car_dealer_func import Dealer as ph
from car_dealer_func import password as pas

Choice1 = ("""l = list of all car model
a = add number
f = find a car model
d = delete a car model
s = mark the car in stock or not
q = quit
Your Choice = """)

Choice2 = ("""l = list of all car model
f = find a car model
c = custom find 
q = quit
Your Choice = """)

person = str(input("Who is login to this program customer or car dealer: "))

if person == 'car dealer':
    passs = input("Enter the password: ")
    if passs == pas:
        choice1 = str(input(Choice1))
        while choice1 != 'q':
            if choice1 == 'l':
                ph.allcar()
            elif choice1 == 'a':
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
            elif choice1 == 'f':
                na = input("Enter the name of the car model which you want to find: ")
                ph.find(na)
            elif choice1 == 'd':
                nam = input("Enter the name of the car which you want to remove: ")
                ph.remove(nam)
            elif choice1 == 's':
                ph.stock_of_car()
            choice1 = str(input(Choice1))
    else:
        print("Wrong Password!!!")
elif person == 'customer':
    choice2 = str(input(Choice2))
    while choice2 != 'q':
        if choice2 == 'l':
            ph.allcar()
        elif choice2 == 'f':
            nn = input("Enter the name of the car model which you want to find: ")
            ph.find(nn)
        elif choice2 == 'c':
            pass
        elif choice2 != 'l' and choice2 != 'f' and choice2 != 'c' and choice2 != 'd':
            print("Sorry! No function found like that. [-]__[-]")
        choice2 = str(input(Choice2))
else:
    print("No person found like that [o]__[o]")