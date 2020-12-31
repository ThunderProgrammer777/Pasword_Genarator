import math
a = int(input("Write the coefficient of x^2:"))
b = int(input("Write the coefficient of x: "))
c = int(input("Write constant (c):"))
disc = math.sqrt(b**2-(4*a*c))
print(disc)
x1 = ((-b+disc)/2*a)
x2 = ((-b-disc)/2*a)

print(f"Roots are {x1} or {x2}.")
