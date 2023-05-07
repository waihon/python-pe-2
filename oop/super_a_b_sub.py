class SuperA:
    var_a = 10
    def fun_a(self):
        return 11


class SuperB:
    var_b = 20
    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    # Inherits from class SueprA and SuperB
    pass


if __name__ == "__main__":
    obj = Sub()
    
    print(obj.var_a, obj.fun_a()) # 10 11
    print(obj.var_b, obj.fun_b()) # 20 21
