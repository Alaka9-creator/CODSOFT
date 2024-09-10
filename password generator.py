import random

def pass_gen(length):
        
    cl = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sl = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    pun = "*&$#@!"
    char = [random.choice(cl), random.choice(sl), random.choice(num), random.choice(pun)]
    password = cl + sl + num + pun
        
    for i in range (length-4):
        char.append(random.choice(password))
        random.shuffle(char)
        
    shuffle = ""
    for password in char:
        shuffle += password
    return shuffle

print("***WELCOME TO PASSWORD GENERATOR***")
print("This program generates strong and random passwords for user\n")
print("TIP: For a strong password, the length of the password must be above 4\n")
while True:
    length = int(input("\nEnter the length of the password: "))
    if length > 4 :
        result = pass_gen(length)
        print(f"Generated password is: {result}")
        print("\nHope it was useful :)")
        break
    else:
        print("\nTry Again !\nPlease ensure that the length of the password is above 4")
