import datetime


def years(age):
    result=int((100-age+2017))
    return result


def main():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    times = int(input("How many times you want to see it?: "))
    for i in range(times):    
        print("Dear %s! You'll be 100 year old in %d" % (name,years(age)),end='\n')
    


if __name__ == '__main__':
    main()
