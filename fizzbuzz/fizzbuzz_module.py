def fizzbuzz(number):
    if number % 15==0:
        return "FizzBuzz"
    elif number % 3==0:
        return "Fizz"
    elif number % 5==0:
        return "Buzz"
    else:
        return number


def main():
    for i in range(100):
        print(fizzbuzz(i))

if __name__ == '__main__':
    main()
