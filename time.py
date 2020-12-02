import string
import random

print("""Hey, I am Password generator and I will generate password for you.
  I will suggest  you five password and which one you like choose it :)
   but please tell me above information which i want from you ....""")


lower = string.ascii_lowercase
lower_chr = []
for low in lower:
    lower_chr.append(low)
upper = string.ascii_uppercase
upper_chr = []
for up in upper:
    upper_chr.append(up)
spec_char = ['!', '@', '#', '$', '%', '^', '&', '*']
final = []

password_length = int(input("How many characters do you want in your password: "))
num_len = int(input("How many (number) digits do you want in your password(If not want any number enter 0): "))
if num_len != 0:
    for i in range(0, num_len):
        n = random.randint(0, 9)

        final.append(n)
password = []
try_1 = []

char_len = str(input("Do you want any alphabet (yes or no): "))
if char_len != "no":
    lowerlen = int(input("How many small letters  do you want ( if not enter 0 ): "))
    upperlen = int(input("How many capital letters do you want ( If not enter 0 ): "))
    for i in range(lowerlen):
        n = random.randint(0, 25)
        final.append(lower_chr[n])
    for _ in range(upperlen):
        n = random.randint(0, 25)
        final.append(upper_chr[n])

spe_char = int(input("How many special characters do you want in your password(If not enter 0): "))
if spe_char != 0:
    for i in range(spe_char):
        n = random.randint(0, 7)
        final.append(spec_char[n])

for i in range(5):
    password.clear()
    try_1.clear()
    while len(try_1) != password_length:
        n = random.randint(0, password_length - 1)
        if n not in try_1:
            try_1.append(n)
            password.append(str(final[n]))
    fine = "".join(password)
    print(f"Your password is {fine}.")

print(" created by - SABHYATA SONI ")
