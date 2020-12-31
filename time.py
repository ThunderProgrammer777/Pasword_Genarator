import math
a = int(input(" write the coefficient of x^2:"))
b = int(input("write the coefficient of x: "))
c = int(input("write constant (c):"))
disc = math.sqrt(b**2-(4*a*c))
print(disc)
x1 = ((-b+disc)/2*a)
x2 = ((-b-disc)/2*a)

print(f"x can be {x1} or {x2}.")
