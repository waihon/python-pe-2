class Classy:
    varia = 2
    def __init__(self, value):
        self.var = value
    
    def method(self, parm):
        print("method: ", parm)

    def print_vars(self):
        print(self.varia, self.var)
        self.other() # other        

    def other(self):
        print("other")

if __name__ == "__main__":
    obj = Classy("object")
    print(obj.var)   # object    
    obj.var = 3
    obj.method(1)    # method: 1
    obj.method(2)    # method: 2
    obj.method(3)    # method: 3
    obj.print_vars() # 2 3\nother
