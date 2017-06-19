def palindrome(string):
    list1 = []
    list2 = []
    for c in string:
        if not c==" ":
            list1.append(str.upper(c))
    for c in reversed(string):
        if not c==" ":
            list2.append(str.upper(c))
    if list1==list2:
        return True
    return False


def main():
    x = input("Please enter the text: ")
    print(palindrome(x))
    return


if __name__ == '__main__':
    main()
