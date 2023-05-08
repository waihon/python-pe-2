class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


if __name__ == "__main__":
    one = One()
    two = Two()
    
    one.doanything() # do_it from One
    # The situation in which the subclass is able to modify its
    # superclass behavior is called polymorphism, which means
    # that one and the same class can take various forms depending
    # on the redefinitions done by any of its subclasses.
    two.doanything() # do_it from Two
