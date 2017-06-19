def listoverlap(list1, list2):
    c = []
    for i in list1:
        if i in list2:
            if i in c:
                continue
            c.append(i)
    return c

import random
def main():
    a = [5]
    b = [5]
    for i in range(random.randint(5,15)):
        a.append(random.randint(0,100))
    for i in range(random.randint(5,15)):
        b.append(random.randint(0,100))
    print(listoverlap(a, b))
    return


if __name__ == '__main__':
    main()
