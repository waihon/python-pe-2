class Classy:
    varia = 2
    def __init__(self, value=None):
        self.var = value
    
    def method(self, parm):
        print("method:", parm)

    def print_vars(self):
        print(self.varia, self.var)
        self.other()           # other        

    def other(self):
        print("other")

    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")

if __name__ == "__main__":
    obj = Classy("object")
    print(obj.var)             # object
    obj.var = 3
    obj.method(1)              # method: 1
    obj.method(2)              # method: 2
    obj.method(3)              # method: 3
    obj.print_vars()           # 2 3\nother

    obj_2 = Classy()
    print(obj_2.var)           # None

    obj.visible()              # visible  
    try:
        obj.__hidden()
    except:
        print("failed")        # failed
    obj._Classy__hidden()      # hidden

    print(obj.__dict__)        # {'var': 3}
    print(Classy.__dict__)
    """
    '__module__': '__main__',
    'varia': 2,
    '__init__': <function Classy.__init__ at 0x10ce2dee0>,
    'method': <function Classy.method at 0x10ce2ddc0>,
    'print_vars': <function Classy.print_vars at 0x10ce2df70>,
    'other': <function Classy.other at 0x10ce2dca0>,
    'visible': <function Classy.visible at 0x10ce2de50>,
    '_Classy__hidden': <function Classy.__hidden at 0x10ce64310>,
    '__dict__': <attribute '__dict__' of 'Classy' objects>,
    '__weakref__': <attribute '__weakref__' of 'Classy' objects>,
    '__doc__': None}    
    """

    print(Classy.__name__)     # Classy
    obj = Classy()
    print(type(obj).__name__)  # Classy
