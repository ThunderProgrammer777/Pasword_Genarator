from PhoneDirectoryFunctions import Phone as ph



Choice = ("""
l = list of all numbers
a = add number
f = find a number
d = delete a number
q = quit
Your Choice = """)
choice=str(input(Choice))
while choice!='q':
    if choice=='l':
        ph.allnum()
    elif choice=='a':
        name = input("Enter the name: ")
        phone = int(input("Enter the phone number: "))
        ph.add(name,phone)
    elif choice=='f':
        na = input("Enter the name of the person whose number you want to find: ")
        ph.find(na)
    elif choice=='d':
        nam = input("Enter the name of the person whose number you want to delete: ")
        ph.remove(nam)
    choice=str(input(Choice))
