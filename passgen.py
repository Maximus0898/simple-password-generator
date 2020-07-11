import random

s = 'POIUYTREWQLKJHGFDSAMNBVCXZqwertyuiop[]asdfghjkl;zxcvbnm,./1234567890!@#$%^&*()_-=+'

command = ""
print("commands : generate, quit")
while True:
    command = input('>')
    if command.lower() == 'generate':
        passlen = int(input('Password length: '))
        password = "".join(random.sample(s,passlen))
        print(password)
    elif command.lower() == 'quit':
        break
    else:
        print("Sorry I don't understand that")
        print("Try once again")
