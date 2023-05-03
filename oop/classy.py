class Classy:
    varia = 2
    def method(self, parm):
        print("method: ", parm)

    def print_vars(self):
        print(self.varia, self.var)        

if __name__ == "__main__":
    obj = Classy()
    obj.var = 3
    obj.method(1)    # method: 1
    obj.method(2)    # method: 2
    obj.method(3)    # method: 3
    obj.print_vars() # 2 3
