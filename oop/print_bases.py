class SuperOne:
    pass

class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass

def print_bases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')

    print(')')

if __name__ == "__main__":
    print_bases(SuperOne)
    print_bases(SuperTwo)
    print_bases(Sub)
