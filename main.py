import string
import random

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

password_length = int(input("How long password do you want: "))

num_len = int(input("How many number do you want in your password: "))
if num_len != 0:
    for y in range(0, num_len):
        n = random.randint(0, 9)
        final.append(n)

password = []
try_1 = []

char_len = int(input("How many character do you want in your password: "))
if char_len != 0:
    lowerlen = int(input("How many lowercase character do you want: "))
    upperlen = int(input("How many upper character do you want: "))
    for _ in range(lowerlen):
        n = random.randint(0, 25)
        final.append(lower_chr[n])
    for _ in range(upperlen):
        n = random.randint(0, 25)
        final.append(upper_chr[n])

spe_char = int(input("How many special characters do you want in your password: "))
if spe_char != 0:
    for _ in range(spe_char):
        n = random.randint(0, 7)
        final.append(spec_char[n])

for _ in range(5):
    password.clear()
    try_1.clear()
    while len(try_1) != password_length:
        n = random.randint(0, password_length - 1)
        if n not in try_1:
            try_1.append(n)
            password.append(str(final[n]))
    fine = "".join(password)
    print(f"Your password is {fine}.")
