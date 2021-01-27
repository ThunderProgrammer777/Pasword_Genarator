from dealer_func import Dealer as ph

Choice = ("""
l = list of all numbers
a = add number
f = find a number
d = delete a number
q = quit
Your Choice = """)
choice = str(input(Choice))
while choice != 'q':
    if choice == 'l':
        ph.allnum()
    elif choice == 'a':
        name = input("Enter the name: ")
        brand = str(input("Enter the brand: "))
        mileage = float(input("What is the mileage of car per litre in km: "))
        fuel = str(input("Enter the type of fuel can used in this model: "))
        fuel_capacity = float(input("What is the fuel capacity of this model in litre: "))
        seater = int(input("How many seat are present in this car model: "))
        engine = input("Enter the name of the engine present in the car model: ")
        price1 = float(input("Enter the minimum price of the model of the car in lakh: "))
        price2 = float(input("Enter the maximum price of the model of the car in lakh: "))
        ph.add(name, brand,mileage,fuel,fuel_capacity,seater,engine,price1,price2)
    elif choice == 'f':
        na = input("Enter the name of the person whose number you want to find: ")
        ph.find(na)
    elif choice == 'd':
        nam = input("Enter the name of the person whose number you want to delete: ")
        ph.remove(nam)
    choice = str(input(Choice))
