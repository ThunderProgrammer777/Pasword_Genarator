def sr(num: int) -> int:
    number = 0
    while True:
        try0 = number ** 2
        if try0 != num:
            pass
        elif try0 == num:
            return number
            break
        number = number + 1


def cr(num: int) -> int:
    number = 0
    while True:
        try0 = number * number * number
        if try0 != num:
            pass
        elif try0 == num:
            return number
            break
        number = number + 1


def add():
    x = int(input("Enter Your First Number:"))
    y = int(input("Enter Your Second Number:"))
    print(x + y)


def sub():
    x = int(input("Enter Your First Number:"))
    y = int(input("Enter Your Second Number:"))
    print(x - y)


def mult():
    x = int(input("Enter Your First Number:"))
    y = int(input("Enter Your Second Number:"))
    print(x * y)


def div():
    x = int(input("Enter Your First Number:"))
    y = int(input("Enter Your Second Number:"))
    print(x / y)


def fac(num:int)->float:
    q = num
    for a in range(1, num):
        num = num * (a)
    return(num)

def avg(avg_list:list)->float:
    number = []
    average = sum(avg_list)/len(avg_list)
    return average


def si():
    print("""If you want simple interest enter si, rate enter r,time enter t or principle enter p""")
    function = str(input("Enter the function:"))
    if function == "si":
        t = float(input("Enter the Time [In Year]:"))
        r = float(input("Enter the Rate:"))
        p = float(input("Enter the Principle:"))
        si = (t * p * r) / 100
        print(si)
    elif function == "r":
        si = float(input("Enter Simple Interest:"))
        t = float(input("Enter the Time [In Year]:"))
        p = float(input("Enter the Principle:"))
        r = ((si * 100) / t) / p
        print(r)
    elif function == "p":
        si = float(input("Enter Simple Interest:"))
        t = float(input("Enter the Time [In Year]:"))
        r = float(input("Enter the Principle:"))
        p = ((si * 100) / t) / r
        print(p)
    elif function == "t":
        si = float(input("Enter Simple Interest:"))
        r = float(input("Enter the Time [In Year]:"))
        p = float(input("Enter the Principle:"))
        t = ((si * 100) / r) / p
        print(t)

def powr(number:int,power:int)->float:
    answer = number ** power
    return answer


def ci(principle: float, rate: float, time: float) -> float:
    amount = principle * (pow((1 + rate / 100), time))
    ci = amount - principle
    return ci

print(avg([20,60,20,42,10,15]))

