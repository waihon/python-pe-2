class Classy:
    def method(self, parm):
        print("method: ", parm)

if __name__ == "__main__":
    obj = Classy()
    obj.method(1) # method: 1
    obj.method(2) # method: 2
    obj.method(3) # method: 3
