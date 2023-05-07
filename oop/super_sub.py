class Super:
    sup_var = 1
    
    def __init__(self, name):
        self.name = name
        self.sup_ivar = 11

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    sub_var = 2
    
    def __init__(self, name):
        # The super() function creates a context in which
        # you don't have to (moreover, you mustn't) pass
        # the self argument to the method being invoked.
        super().__init__(name)
        self.sub_ivar = 12


if __name__ == "__main__":
    obj = Sub("Andy")
    
    print(obj)          # My name is Andy.
    print(obj.sub_var)  # 2
    print(obj.sup_var)  # 1
    print(obj.sub_ivar) # 12
    print(obj.sup_ivar) # 11
