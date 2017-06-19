import string
import random
def passwordgen():
    list_lowercase = []
    list_uppercase = []
    list_syms = ["!","@","#","$","%","^","&","*","(",")","?"] # !@#$%^&*()?
    password = []
    length = 0
    while length < 8:
        length = int(input("Please enter the length of your new password (min. 8): "))
    for i in string.ascii_lowercase:
        list_lowercase.append(i)
    for i in string.ascii_uppercase:
        list_uppercase.append(i)
    for x in range(length):
        y = random.randint(1,4)
        if y == 1:
            password.append(list_lowercase[random.randint(0,len(list_lowercase)-1)])
        if y == 2:
            password.append(list_uppercase[random.randint(0,len(list_uppercase)-1)])
        if y == 3:
            password.append(random.randint(0,9))
        if y == 4:
            password.append(list_syms[random.randint(0,len(list_syms)-1)])
    return(''.join(map(str,password)))
  
def main():
    passwordgen()
    
    


if __name__ == '__main__':
    main()
